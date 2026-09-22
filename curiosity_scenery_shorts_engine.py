"""
CURIOSITY SCENERY SHORTS ENGINE (v1.0)
====================================================================================
Combines mind-relieving, mesmerizing aesthetic scenery visuals with ultra-engaging
curiosity-hook scripts. Designed for maximum retention, re-watches, and automated
daily batch publishing to YouTube Shorts & Reels.
"""

import os
import sys
import re
import json
import random
import asyncio
import subprocess
import urllib.parse
from datetime import datetime, date

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import requests
import imageio_ffmpeg
import edge_tts
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR   = os.path.join(BASE_DIR, "assets")
SCENERY_DIR  = os.path.join(ASSETS_DIR, "scenery")
BGM_DIR      = os.path.join(ASSETS_DIR, "bgm")
TEMP_DIR     = os.path.join(BASE_DIR, "temp_curiosity")
TOKEN_FILE   = os.path.join(BASE_DIR, "token.json")
HISTORY_FILE = os.path.join(BASE_DIR, "curiosity_history.json")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(SCENERY_DIR, exist_ok=True)
os.makedirs(BGM_DIR, exist_ok=True)

# Load complete 30-day suite of 1 to 2 minute curiosity scripts
from monthly_curiosity_scripts_30days import MONTHLY_30_DAYS_SCRIPTS

CURIOSITY_STORIES = MONTHLY_30_DAYS_SCRIPTS


# Category → subfolder mapping (matches classify_scenery_images.py output)
CATEGORY_FOLDERS = {
    "nature":      os.path.join(SCENERY_DIR, "nature"),
    "space":       os.path.join(SCENERY_DIR, "space"),
    "fantasy":     os.path.join(SCENERY_DIR, "fantasy"),
    "spiritual":   os.path.join(SCENERY_DIR, "spiritual"),
    "dark_moody":  os.path.join(SCENERY_DIR, "dark_moody"),
    "anime_art":   os.path.join(SCENERY_DIR, "anime_art"),
    "animals":     os.path.join(SCENERY_DIR, "animals"),
    "abstract":    os.path.join(SCENERY_DIR, "abstract"),
    "urban":       os.path.join(SCENERY_DIR, "urban"),
    "ocean":       os.path.join(SCENERY_DIR, "ocean"),
    "uncategorized": os.path.join(SCENERY_DIR, "uncategorized"),
}

def _collect_images_from_folder(folder: str) -> list:
    """Returns list of full image paths from a given folder."""
    if not os.path.isdir(folder):
        return []
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ]

def get_scenery_background(keywords: list, category: str = "") -> str:
    """
    Picks a scenery image intelligently:
      1. From the story's assigned category subfolder (if available)
      2. Falls back to any subfolder if category folder is empty
      3. Generates a solid-color fallback if no images exist at all
    """
    # Try the category-specific folder first
    if category and category in CATEGORY_FOLDERS:
        cat_images = _collect_images_from_folder(CATEGORY_FOLDERS[category])
        if cat_images:
            return random.choice(cat_images)

    # Try uncategorized as secondary fallback
    uncat_images = _collect_images_from_folder(CATEGORY_FOLDERS.get("uncategorized", ""))

    # Collect ALL images across all subfolders
    all_images = []
    for folder in CATEGORY_FOLDERS.values():
        all_images.extend(_collect_images_from_folder(folder))

    # Also check root SCENERY_DIR for any unclassified images still there
    root_images = [
        os.path.join(SCENERY_DIR, f)
        for f in os.listdir(SCENERY_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        and os.path.isfile(os.path.join(SCENERY_DIR, f))
    ]
    all_images.extend(root_images)

    if all_images:
        return random.choice(all_images)

    # Last resort: generate solid-color background via ffmpeg
    fallback = os.path.join(TEMP_DIR, "fallback_scenery.jpg")
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([
        ffmpeg, "-y", "-f", "lavfi", "-i", "color=c=0x1a1a2e:size=1080x1920:rate=1",
        "-frames:v", "1", fallback
    ], capture_output=True)
    return fallback



async def synthesize_voice(text: str, output_path: str, voice: str = "en-US-ChristopherNeural"):
    communicate = edge_tts.Communicate(text, voice=voice, rate="+3%", pitch="+0Hz")
    with open(output_path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])

def get_audio_duration(path: str) -> float:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    res = subprocess.run([ffmpeg, "-i", path], capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            t = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t.split(":")
            return float(h)*3600 + float(m)*60 + float(s)
    return 20.0

def render_scenery_short(bg_image: str, audio_path: str, narration_text: str,
                          duration: float, output_path: str, motion_style: str = "ken_burns",
                          formula: str = "", equation_name: str = ""):
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    words = narration_text.split()
    chunks = [" ".join(words[i:i+5]) for i in range(0, len(words), 5)]
    chunk_dur = duration / max(len(chunks), 1)

    drawtext_filters = []
    for idx, chk in enumerate(chunks):
        t_start = idx * chunk_dur
        t_end = (idx + 1) * chunk_dur
        cleaned_chk = chk.replace("'", "").replace('"', '').replace("—", "-").replace(":", " - ")
        safe_chk = re.sub(r"[^a-zA-Z0-9\s.,!-]", "", cleaned_chk).strip()
        drawtext_filters.append(
            f"drawtext=font='Arial':text='{safe_chk}':fontsize=52:fontcolor=yellow:"
            f"bordercolor=black:borderw=4:x=(w-text_w)/2:y=(h-text_h)/2+240:"
            f"enable='between(t,{t_start:.2f},{t_end:.2f})'"
        )

    subtitle_filter = "," + ",".join(drawtext_filters) if drawtext_filters else ""

    # Climax / Twist Revelation timestamp (approx 68% into the story)
    t_twist = duration * 0.68
    # 1. Blackout frame drop (0.14s blackout) + 2. Shock white flash (0.08s flash)
    blackout_flash = (
        f",drawbox=x=0:y=0:w=iw:h=ih:color=black@1.0:t=fill:enable='between(t,{t_twist:.2f},{t_twist+0.14:.2f})'"
        f",drawbox=x=0:y=0:w=iw:h=ih:color=white@0.85:t=fill:enable='between(t,{t_twist+0.14:.2f},{t_twist+0.22:.2f})'"
    )

    # Persistent Equation HUD Display (From beginning to the end)
    eq_overlay = ""
    if formula:
        safe_name = re.sub(r"[^a-zA-Z0-9\s.,!+-]", "", equation_name.replace(":", " - ")).strip()
        # Clean ASCII representation for maximum FFmpeg stability
        cleaned_formula = formula.replace("^2", "2").replace("^3", "3").replace("^", "").replace("*", " x ").replace(":", " - ")
        safe_form = re.sub(r"[^a-zA-Z0-9\s.,!+=/ -]", "", cleaned_formula).strip()
        eq_overlay = (
            f",drawbox=x=(w-920)/2:y=230:w=920:h=180:color=black@0.72:t=fill"
            f",drawbox=x=(w-920)/2:y=230:w=920:h=180:color=cyan@0.85:t=4"
            f",drawtext=font='Arial':text='{safe_name}':fontsize=36:fontcolor=cyan:bordercolor=black:borderw=3:x=(w-text_w)/2:y=255"
            f",drawtext=font='Arial':text='{safe_form}':fontsize=58:fontcolor=white:bordercolor=black:borderw=4:x=(w-text_w)/2:y=310"
        )

    # Common End Subscribe Banner (Final 7 seconds)
    t_cta_start = max(0.0, duration - 7.0)
    subscribe_cta = (
        f",drawbox=x=(w-820)/2:y=1640:w=820:h=120:color=red@0.90:t=fill:enable='between(t,{t_cta_start:.2f},{duration:.2f})'"
        f",drawbox=x=(w-820)/2:y=1640:w=820:h=120:color=white@0.95:t=3:enable='between(t,{t_cta_start:.2f},{duration:.2f})'"
        f",drawtext=font='Arial':text='LIKE & SUBSCRIBE FOR MORE':fontsize=44:fontcolor=white:bordercolor=black:borderw=3:x=(w-text_w)/2:y=1676:enable='between(t,{t_cta_start:.2f},{duration:.2f})'"
    )

    # Dynamic Motion Architectures:
    if motion_style == "beat_pulse":
        vf = (
            f"scale=1440:2560:force_original_aspect_ratio=increase,"
            f"crop=1080:1920:'(iw-1080)*(0.5+0.2*sin(t/2))':'(ih-1920)/2',"
            f"zoompan=z='1.05+0.10*abs(sin(on/25))':d={int(duration*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,"
            f"eq=contrast=1.18:brightness=0.03:saturation=1.35,"
            f"vignette=PI/4"
            f"{eq_overlay}"
            f"{subtitle_filter}"
            f"{subscribe_cta}"
        )
    elif motion_style == "glitch_pop":
        vf = (
            f"scale=1440:2560:force_original_aspect_ratio=increase,"
            f"crop=1080:1920:'(iw-1080)*(0.5+0.15*cos(t/{duration}))':'(ih-1920)/2',"
            f"zoompan=z='min(pzoom+0.0008,1.30)':d={int(duration*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,"
            f"eq=contrast=1.22:brightness=0.04:saturation=1.40,"
            f"vignette=PI/3.5"
            f"{eq_overlay}"
            f"{subtitle_filter}"
            f"{subscribe_cta}"
        )
    else:  # Default: ken_burns (Drift & Deep Zoom)
        vf = (
            f"scale=1440:2560:force_original_aspect_ratio=increase,"
            f"crop=1080:1920:'(iw-1080)*(0.5+0.3*sin(t/{duration}))':'(ih-1920)/2',"
            f"zoompan=z='min(pzoom+0.0005,1.25)':d={int(duration*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,"
            f"eq=contrast=1.15:brightness=0.02:saturation=1.28,"
            f"vignette=PI/3.5"
            f"{eq_overlay}"
            f"{subtitle_filter}"
            f"{subscribe_cta}"
        )

    cmd = [
        ffmpeg, "-y",
        "-loop", "1", "-i", bg_image,
        "-i", audio_path,
        "-vf", vf,
        "-t", str(duration),
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "44100",
        output_path
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def get_category_bgm(category: str) -> str:
    """
    Selects background music matching the specific vibe of the facts:
    1. psychology_mystery: dark_moody, abstract, mind glitches
    2. space_tech: space, cosmos, futuristic tech, physics
    3. nature_history_lofi: nature, ocean, history, animals, spiritual, fantasy
    """
    cat_map = {
        "dark_moody": "psychology_mystery",
        "abstract": "psychology_mystery",
        "mind": "psychology_mystery",
        "space": "space_tech",
        "tech": "space_tech",
        "futuristic": "space_tech",
        "nature": "nature_history_lofi",
        "ocean": "nature_history_lofi",
        "history": "nature_history_lofi",
        "spiritual": "nature_history_lofi",
        "fantasy": "nature_history_lofi",
        "animals": "nature_history_lofi",
    }
    target_folder_name = cat_map.get(category.lower(), "psychology_mystery")
    target_dir = os.path.join(BGM_DIR, target_folder_name)
    
    if os.path.isdir(target_dir):
        tracks = [
            os.path.join(target_dir, f)
            for f in os.listdir(target_dir)
            if f.lower().endswith((".mp3", ".wav", ".aac", ".m4a"))
        ]
        if tracks:
            return random.choice(tracks)
            
    all_bgm = []
    for root, _, files in os.walk(BGM_DIR):
        for f in files:
            if f.lower().endswith((".mp3", ".wav", ".aac", ".m4a")):
                all_bgm.append(os.path.join(root, f))
                
    if all_bgm:
        return random.choice(all_bgm)
    return ""

def assemble_final_with_bgm(video_path: str, output_path: str, category: str = "", duration: float = 60.0):
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    bgm = get_category_bgm(category)
    t_twist = duration * 0.48  # Mid-video pattern interrupt around 45-50% mark
    fade_out_start = max(0.0, duration - 1.0)

    if bgm and os.path.exists(bgm):
        # Audio Ducking Standard:
        # 1. Voice at 100% volume
        # 2. BGM ducked to 18% (volume=0.18) with 1s fade-in and 1s fade-out
        # 3. 0.25s silence at the mid-video pattern interrupt / twist reveal
        filter_complex = (
            f"[0:a]volume=1.0[voice];"
            f"[1:a]volume=0.18,"
            f"afade=t=in:st=0:d=1,"
            f"afade=t=out:st={fade_out_start:.2f}:d=1,"
            f"volume=enable='between(t,{t_twist:.2f},{t_twist+0.25:.2f})':volume=0.0,"
            f"aloop=loop=-1:size=2e+09[bgm];"
            f"[voice][bgm]amix=inputs=2:duration=first[aout]"
        )
        cmd = [
            ffmpeg, "-y",
            "-i", video_path,
            "-i", bgm,
            "-filter_complex", filter_complex,
            "-map", "0:v",
            "-map", "[aout]",
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            output_path
        ]
    else:
        cmd = [ffmpeg, "-y", "-i", video_path, "-c", "copy", output_path]

    subprocess.run(cmd, check=True, capture_output=True)

def get_youtube_service():
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        token_data = json.load(f)
    creds = Credentials.from_authorized_user_info(token_data)
    return build("youtube", "v3", credentials=creds)

def upload_to_youtube(video_path: str, title: str, description: str, tags: list) -> str:
    print("[UPLOAD] Connecting to YouTube API v3...")
    yt = get_youtube_service()
    body = {
        "snippet": {
            "title": title[:95],
            "description": description,
            "tags": tags,
            "categoryId": "27"
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/mp4")
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    res = req.execute()
    vid_id = res.get("id")
    url = f"https://youtube.com/shorts/{vid_id}"
    print(f"\n{'='*60}")
    print(f"✅ LIVE CURIOSITY SCENERY SHORT: {url}")
    print(f"{'='*60}\n")
    return url

async def process_story_async(story: dict) -> str:
    story_id = story["id"]
    print(f"\n{'='*60}")
    print(f"  RENDERING CURIOSITY SCENERY SHORT: {story['title']}")
    print(f"{'='*60}")

    bg_path = get_scenery_background(story.get("scenery_keywords", []), category=story.get("category", ""))
    print(f"  [SCENERY VISUAL] Category: [{story.get('category', 'any')}] | Image: {os.path.basename(bg_path)}")

    audio_path = os.path.join(TEMP_DIR, f"{story_id}_narration.mp3")
    voice = random.choice(["en-US-ChristopherNeural", "en-US-GuyNeural", "en-US-EricNeural"])
    await synthesize_voice(story["narration"], audio_path, voice)
    duration = get_audio_duration(audio_path) + 0.8

    raw_video = os.path.join(TEMP_DIR, f"{story_id}_raw.mp4")
    render_scenery_short(
        bg_path, audio_path, story["narration"], duration, raw_video,
        motion_style=story.get("motion_style", "ken_burns"),
        formula=story.get("formula", ""),
        equation_name=story.get("equation_name", "")
    )

    final_path = os.path.join(BASE_DIR, f"final_curiosity_{story_id}.mp4")
    assemble_final_with_bgm(raw_video, final_path, category=story.get("category", ""), duration=duration)
    print(f"[COMPLETE] Rendered Curiosity Short: {final_path}")
    return final_path

def _build_infinite_story_queue() -> list:
    """Returns a shuffled infinite-style queue by cycling stories without immediate repeats."""
    pool = list(CURIOSITY_STORIES)
    queue = []
    last_id = None
    while len(queue) < len(pool) * 10:       # pre-build 10 full cycles
        random.shuffle(pool)
        for s in pool:
            if s["id"] != last_id:
                queue.append(s)
                last_id = s["id"]
    return queue


def run_curiosity_pipeline(limit: int = 1, upload: bool = True):
    """Run exactly `limit` shorts (default 1). Use run_nonstop_30min() for the full marathon."""
    selected_stories = random.sample(CURIOSITY_STORIES, min(limit, len(CURIOSITY_STORIES)))
    urls = []
    for story in selected_stories:
        final_video = asyncio.run(process_story_async(story))
        if upload:
            description = (
                f"{story['title']}\n\n"
                "Mind-bending facts & deep life curiosities revealed every single day. "
                "Subscribe for one daily thought that changes how you see reality.\n\n"
                + " ".join(f"#{t}" for t in story["tags"])
            )
            try:
                url = upload_to_youtube(final_video, story["youtube_title"], description, story["tags"])
                urls.append(url)
            except Exception as e:
                print(f"[UPLOAD ERROR] {e}")
                urls.append(final_video)
        else:
            urls.append(final_video)
    return urls


def run_nonstop_30min(target_minutes: float = 30.0, upload: bool = True):
    """
    MAIN AUTOMATION MARATHON
    ========================
    Renders and uploads YouTube Shorts non-stop until the total cumulative
    video duration reaches `target_minutes` (default = 30 minutes).

    Each short is rendered → uploaded sequentially so YouTube receives a
    continuous stream of fresh content for the full 30-minute window.
    """
    target_seconds = target_minutes * 60
    story_queue    = _build_infinite_story_queue()
    queue_idx      = 0

    total_duration = 0.0
    short_count    = 0
    uploaded_urls  = []

    print("\n" + "=" * 70)
    print(f"  🚀  NON-STOP 30-MINUTE SHORTS AUTOMATION STARTED")
    print(f"  🎯  Target: {target_minutes} minutes of total content")
    print("=" * 70 + "\n")

    while total_duration < target_seconds:
        if queue_idx >= len(story_queue):
            # Rebuild queue if somehow exhausted (shouldn't happen with 10 cycles)
            story_queue = _build_infinite_story_queue()
            queue_idx   = 0

        story      = story_queue[queue_idx]
        queue_idx += 1
        short_count += 1

        print(f"\n{'─'*70}")
        print(f"  📹  SHORT #{short_count}  |  Total so far: {total_duration/60:.1f} min  |  Goal: {target_minutes} min")
        print(f"  🎬  Story: {story['title']}")
        print(f"{'─'*70}")

        try:
            final_video = asyncio.run(process_story_async(story))

            # Measure actual rendered duration
            vid_duration = get_audio_duration(final_video)
            total_duration += vid_duration

            print(f"  ⏱️  Short duration: {vid_duration:.1f}s  |  Cumulative: {total_duration/60:.2f} / {target_minutes} min")

            if upload:
                description = (
                    f"{story['title']}\n\n"
                    "Mind-bending facts & deep life curiosities revealed every single day. "
                    "Subscribe for one daily thought that changes how you see reality.\n\n"
                    + " ".join(f"#{t}" for t in story["tags"])
                )
                try:
                    url = upload_to_youtube(
                        final_video,
                        story["youtube_title"],
                        description,
                        story["tags"]
                    )
                    uploaded_urls.append(url)
                    print(f"  ✅  Uploaded: {url}")
                except Exception as upload_err:
                    print(f"  ⚠️  Upload failed (video saved locally): {upload_err}")
                    uploaded_urls.append(final_video)
            else:
                uploaded_urls.append(final_video)

        except Exception as render_err:
            print(f"  ❌  Render error on '{story['title']}': {render_err}")
            # Skip and continue — don't let one failure stop the marathon
            continue

        # Remaining time banner
        remaining = max(0, target_seconds - total_duration)
        print(f"  ⏳  Remaining to reach goal: {remaining/60:.1f} min")

    # ─── FINAL SUMMARY ───────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print(f"  🏁  MARATHON COMPLETE!")
    print(f"  📊  Total Shorts Rendered & Uploaded : {short_count}")
    print(f"  🕒  Total Content Duration           : {total_duration/60:.2f} minutes")
    print(f"  🔗  URLs Published:")
    for i, u in enumerate(uploaded_urls, 1):
        print(f"       {i:>3}. {u}")
    print("=" * 70 + "\n")

    return uploaded_urls


def run_math_day_batch(day: int = 1, upload: bool = False) -> list:
    """
    Renders all 10 equations for a specific day from the 30-Day Math Curriculum.
    Persistent Equation HUD is rendered from beginning to end.
    """
    try:
        from master_30days_math_curriculum_300eq import get_30day_math_batch, format_math_narration
    except ImportError:
        print("❌ master_30days_math_curriculum_300eq module not found.")
        return []

    eq_batch = get_30day_math_batch(day)
    print("\n" + "=" * 70)
    print(f"  📚  RENDERING DAY {day:02d} MATHEMATICS SHORTS BATCH (10 EQUATIONS)")
    print(f"  🎯  Curriculum Level: {eq_batch[0].get('grade_level', 'General')}")
    print("=" * 70 + "\n")

    rendered_files = []
    for idx, eq in enumerate(eq_batch, 1):
        story = {
            "id": f"math_day{day:02d}_eq{eq['day_eq_num']:02d}_{eq['equation_name'].lower().replace(' ', '_').replace('/', '_')[:24]}",
            "title": f"Day {day} ({eq['grade_level']}): {eq['equation_name']} — {eq['formula']}",
            "youtube_title": f"{eq['equation_name']} Explained: {eq['formula']} 🧮 #shorts #math #science #education",
            "tags": ["math", "equations", "education", "science", "shorts", "learn", "physics"],
            "category": eq.get("category", "abstract"),
            "motion_style": eq.get("motion_style", "beat_pulse"),
            "bgm_vibe": eq.get("bgm_vibe", "space_tech"),
            "scenery_keywords": [eq.get("category", "space"), "abstract"],
            "formula": eq.get("formula", ""),
            "equation_name": eq.get("equation_name", ""),
            "narration": format_math_narration(eq)
        }

        print(f"\n{'─'*70}")
        print(f"  [{idx:02d}/10] Rendering: {story['title']}")
        print(f"  Formula HUD : [{story['formula']}]")
        print(f"{'─'*70}")

        try:
            video_path = asyncio.run(process_story_async(story))
            rendered_files.append(video_path)
            if upload:
                desc = (
                    f"{story['title']}\n\n"
                    f"Equation: {eq['formula']}\n"
                    f"Discovered by: {eq['founder']}\n\n"
                    "Daily 30-Day Mathematics Master Curriculum. "
                    "Subscribe to unlock all 300 essential equations!\n\n"
                    + " ".join(f"#{t}" for t in story["tags"])
                )
                try:
                    upload_url = upload_to_youtube(video_path, story["youtube_title"], desc, story["tags"])
                    print(f"  ✅  Uploaded: {upload_url}")
                except Exception as up_err:
                    print(f"  ⚠️  Upload error: {up_err}")
        except Exception as e:
            print(f"  ❌  Error rendering {story['title']}: {e}")

    print("\n" + "=" * 70)
    print(f"  🏁  DAY {day:02d} MATHEMATICS BATCH COMPLETE: {len(rendered_files)}/10 Rendered")
    print("=" * 70 + "\n")
def run_production_scripts_day_batch(day: int = 1, upload: bool = False) -> list:
    """
    Renders all 15 high-retention production track scripts for a specific day
    directly from scritps.txt.
    """
    try:
        from load_production_scripts import get_scripts_for_day
    except ImportError:
        print("❌ load_production_scripts module not found.")
        return []

    day_scripts = get_scripts_for_day(day)
    if not day_scripts:
        print(f"⚠️ No scripts found for Day {day} in scritps.txt")
        return []

    print("\n" + "=" * 70)
    print(f"  🎬  RENDERING DAY {day:02d} PRODUCTION SCRIPTS (15 SHORTS / TRACKS)")
    print(f"  📊  Loaded {len(day_scripts)} production scripts from scritps.txt")
    print("=" * 70 + "\n")

    rendered_files = []
    for idx, story in enumerate(day_scripts, 1):
        print(f"\n{'─'*70}")
        print(f"  [{idx:02d}/{len(day_scripts)}] Rendering: {story['title']}")
        print(f"  Vibe: [{story.get('bgm_vibe', 'psychology_mystery')}] | Voice: [{story.get('voice_style', 'default')}]")
        if story.get("formula"):
            print(f"  Formula HUD : [{story['formula']}]")
        print(f"{'─'*70}")

        try:
            video_path = asyncio.run(process_story_async(story))
            rendered_files.append(video_path)
            if upload:
                desc = (
                    f"{story['title']}\n\n"
                    "Daily High-Retention Mind-Expanding Shorts.\n"
                    "Subscribe for one daily thought that changes how you see reality!\n\n"
                    + " ".join(f"#{t}" for t in story["tags"])
                )
                try:
                    upload_url = upload_to_youtube(video_path, story["youtube_title"], desc, story["tags"])
                    print(f"  ✅  Uploaded: {upload_url}")
                except Exception as up_err:
                    print(f"  ⚠️  Upload error: {up_err}")
        except Exception as e:
            print(f"  ❌  Error rendering {story['title']}: {e}")

    print("\n" + "=" * 70)
    print(f"  🏁  DAY {day:02d} PRODUCTION SCRIPTS COMPLETE: {len(rendered_files)}/{len(day_scripts)} Rendered")
    print("=" * 70 + "\n")
    return rendered_files


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Curiosity Scenery & Mathematics Shorts Engine")
    parser.add_argument(
        "--mode",
        choices=["single", "marathon", "math", "production"],
        default="production",
        help="'production' = render 15 tracks from scritps.txt. 'math' = 10-equation day batch. 'single' = 1 short. 'marathon' = 30-min stream."
    )
    parser.add_argument(
        "--day",
        type=int,
        default=1,
        help="Day number (1-31) for production/math mode (default: 1)"
    )
    parser.add_argument(
        "--minutes",
        type=float,
        default=30.0,
        help="Target total minutes of content for marathon mode (default: 30)"
    )
    parser.add_argument(
        "--no-upload",
        action="store_true",
        help="Render only, skip YouTube upload"
    )
    args = parser.parse_args()

    do_upload = not args.no_upload

    if args.mode == "production":
        print(f"[MODE] Production Scripts (scritps.txt) — Day {args.day} (15 Tracks)")
        run_production_scripts_day_batch(day=args.day, upload=do_upload)
    elif args.mode == "math":
        print(f"[MODE] Mathematics Curriculum — Day {args.day} Batch (10 Shorts)")
        run_math_day_batch(day=args.day, upload=do_upload)
    elif args.mode == "single":
        print("[MODE] Single curiosity short render")
        run_curiosity_pipeline(limit=1, upload=do_upload)
    else:
        print(f"[MODE] Marathon — target {args.minutes} minutes of shorts")
        run_nonstop_30min(target_minutes=args.minutes, upload=do_upload)




