import os
import sys
import json
import time
import argparse
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

BASE_DIR = Path(__file__).parent
REGISTRY_FILE = BASE_DIR / "uploaded_videos_registry.json"
QUEUE_DIRS = [
    BASE_DIR / "cloud_queue_masters",
    BASE_DIR / "temp_new_18_suite" / "rendered_masters",
    BASE_DIR
]
MANIFEST_FILE = BASE_DIR / "cloud_candidates_manifest.json"
TOKEN_FILE = BASE_DIR / "token.json"

def get_youtube_client():
    # If running in GitHub Actions with env secret YOUTUBE_TOKEN_JSON
    token_json_str = os.environ.get("YOUTUBE_TOKEN_JSON")
    if token_json_str:
        print("🔑 Using YouTube credentials from GitHub Actions Secret (YOUTUBE_TOKEN_JSON)...")
        token_data = json.loads(token_json_str)
    elif TOKEN_FILE.exists():
        print(f"🔑 Using YouTube credentials from local file: {TOKEN_FILE}...")
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            token_data = json.load(f)
    else:
        raise RuntimeError("No YouTube token available! Set YOUTUBE_TOKEN_JSON secret or provide token.json")

    creds = Credentials.from_authorized_user_info(token_data)
    return build("youtube", "v3", credentials=creds)

def load_registry():
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_registry(reg):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False)

def upload_video(youtube, cfg, video_path):
    print(f"\n🚀 [CLOUD DISPATCH] Uploading: {cfg['title'][:60]}...", flush=True)
    body = {
        "snippet": {
            "title": cfg["title"],
            "description": cfg["desc"],
            "tags": cfg["tags"],
            "categoryId": str(cfg.get("category", "24"))
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }
    media = MediaFileUpload(str(video_path), mimetype="video/mp4", resumable=True)
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    res = req.execute()
    new_vid = res["id"]
    pub_url = f"https://youtube.com/shorts/{new_vid}"
    print(f"  🎉 PUBLISHED! Live URL: {pub_url}", flush=True)

    # Anti-Claim Sentry Guard check
    try:
        time.sleep(3)
        chk = youtube.videos().list(part="contentDetails,status", id=new_vid).execute()
        items = chk.get("items", [])
        if items:
            cd = items[0].get("contentDetails", {})
            if "regionRestriction" in cd:
                blocked = cd["regionRestriction"].get("blocked", [])
                print(f"  ⚠️ REGIONAL BLOCK DETECTED {blocked}! Deleting...", flush=True)
                youtube.videos().delete(id=new_vid).execute()
                return None
            else:
                print(f"  🛡️ SENTRY GUARD: 100% CLEAN - No regional restrictions!", flush=True)
    except Exception as e:
        print(f"  Sentry note: {e}", flush=True)

    return new_vid, pub_url

def dispatch_batch(batch_size=10):
    print("=" * 70)
    print(f"🚀 GIT CLOUD DISPATCHER: DEPLOYING NEXT BATCH OF {batch_size} SHORTS")
    print("=" * 70)

    youtube = get_youtube_client()
    reg = load_registry()
    already_uploaded = {v.get("source_id") or v.get("source_raw_id") for v in reg.values()}

    if not MANIFEST_FILE.exists():
        print(f"❌ Manifest missing: {MANIFEST_FILE}")
        return

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        candidates = json.load(f)

    uploaded_in_run = 0

    for cfg in candidates:
        if uploaded_in_run >= batch_size:
            print(f"🏁 Reached scheduled batch target of {batch_size} shorts. Finishing run.")
            break

        cid = cfg["id"]
        if cid in already_uploaded:
            continue

        master_path = None
        for qd in QUEUE_DIRS:
            candidate_p = qd / f"{cid}_FULL_ANIMATED_MASTER.mp4"
            if candidate_p.exists() and candidate_p.stat().st_size > 1000000:
                master_path = candidate_p
                break

        if not master_path:
            print(f"⚠️ Master video not ready yet for {cid}: {cid}_FULL_ANIMATED_MASTER.mp4")
            continue

        res = upload_video(youtube, cfg, master_path)
        if res:
            new_vid, pub_url = res
            reg[new_vid] = {
                "title": cfg["title"],
                "published_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "source_id": cid,
                "format": "clean_board_3d_ppt_wordart_stings",
                "cloud_deployed": True
            }
            save_registry(reg)
            already_uploaded.add(cid)
            uploaded_in_run += 1

            if uploaded_in_run < batch_size:
                print("  ⏳ Cooldown 45s between drops for optimal algorithmic indexing...", flush=True)
                time.sleep(45)

    print(f"\n✨ CLOUD RUN FINISHED: {uploaded_in_run} shorts published successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Git Cloud Shorts Dispatcher")
    parser.add_argument("--batch-size", type=int, default=10, help="Number of shorts to publish in this drop")
    args = parser.parse_args()
    dispatch_batch(batch_size=args.batch_size)
