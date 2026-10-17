"""
MASTER VIRAL SUITE ELEVATOR & PUBLISHER
=======================================
Transforms top viral short clips (Peaky Blinders, John Wick, Interstellar, Red Notice)
into cinematic, high-retention 9:16 vertical masterpieces:
- Fast blurred-background scaling (0 black bars)
- Genre-tailored cinematic color grading & contrast curve
- Attention-grabbing top hook glassmorphic banner
- Studio audio remastering & bass/dialogue EQ
- Anti-fingerprint speed & hash perturbations (1.015x)
- YouTube upload as UNLISTED for safety verification
"""

import sys
import os
import json
import subprocess
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

BASE_DIR = Path(__file__).parent
TEMP_DIR = BASE_DIR / "temp_viral_suite"
TOKEN_FILE = BASE_DIR / "token.json"
REGISTRY_FILE = BASE_DIR / "uploaded_videos_registry.json"

VIRAL_CONFIGS = [
    {
        "id_key": "viral_peaky_blinders_cold_respect",
        "raw_file": "peaky_blinders_raw.mp4",
        "output_file": "peaky_blinders_cinematic_master.mp4",
        "banner_file": "peaky_blinders_banner.png",
        "tag_line": "PEAKY BLINDERS • COLD RESPECT",
        "hook_line": "HE REALIZED WHO HE WAS TALKING TO 💀",
        "accent_color": (212, 175, 55),      # Gold
        "fg_width": 1080,
        "fg_height": 1080,
        "fg_y": 420,
        "banner_y": 140,
        "color_eq": "contrast=1.12:brightness=-0.02:saturation=0.92",
        "audio_eq": "equalizer=f=80:width_type=o:width=2:g=1.5,equalizer=f=3200:width_type=o:width=1.5:g=1.2",
        "title": "He Realized Who He Was Talking To 💀🔥 #shorts #peakyblinders #attitude #sigma",
        "description": (
            "The moment they realized Tommy Shelby isn't someone you threaten. Coldest scene in Peaky Blinders history.\n\n"
            "Remastered with cinematic film grading & enhanced sound design.\n\n"
            "#shorts #peakyblinders #tommyshelby #cillianmurphy #attitude #sigma #badass #cinematic #moviescene"
        ),
        "tags": ["peaky blinders", "tommy shelby", "cillian murphy", "sigma", "attitude status", "badass", "cinematic edit", "cold respect", "movies", "hollywood"],
        "category_id": "1"  # Film & Animation
    },
    {
        "id_key": "viral_john_wick_rule_of_respect",
        "raw_file": "john_wick_raw.mp4",
        "output_file": "john_wick_neon_master.mp4",
        "banner_file": "john_wick_banner.png",
        "tag_line": "JOHN WICK • RULE OF RESPECT",
        "hook_line": "THEY REALIZED WHO JUST WALKED IN... 💀🔥",
        "accent_color": (0, 212, 255),        # Neon Cyan
        "fg_width": 1080,
        "fg_height": 1080,
        "fg_y": 420,
        "banner_y": 140,
        "color_eq": "contrast=1.16:brightness=0.01:saturation=1.12",
        "audio_eq": "equalizer=f=90:width_type=o:width=2:g=1.6,equalizer=f=3500:width_type=o:width=1.5:g=1.3",
        "title": "They Realized Who Just Walked In... 💀🔥 #shorts #johnwick #keanureeves #badass",
        "description": (
            "The entire room freezes the second John Wick steps in. Baba Yaga's presence speaks for itself.\n\n"
            "Remastered in high-contrast neon-noir 60fps with studio sound remastering.\n\n"
            "#shorts #johnwick #keanureeves #babayaga #action #badass #sigma #continental #movies"
        ),
        "tags": ["john wick", "keanu reeves", "baba yaga", "continental", "badass", "action movie", "sigma", "cinematic", "shorts"],
        "category_id": "1"
    },
    {
        "id_key": "viral_interstellar_heartbreaking_promise",
        "raw_file": "interstellar_raw.mp4",
        "output_file": "interstellar_celestial_master.mp4",
        "banner_file": "interstellar_banner.png",
        "tag_line": "INTERSTELLAR • TIME DILATION",
        "hook_line": "THE MOST HEARTBREAKING PROMISE ⏳🚀",
        "accent_color": (180, 210, 255),      # Celestial Platinum
        "fg_width": 1080,
        "fg_height": 1200,
        "fg_y": 360,
        "banner_y": 120,
        "color_eq": "contrast=1.14:brightness=-0.01:saturation=1.05",
        "audio_eq": "equalizer=f=75:width_type=o:width=2:g=1.4,equalizer=f=4000:width_type=o:width=1.5:g=1.1",
        "title": "The Most Heartbreaking Promise In Cinema ⏳🚀 #shorts #interstellar #movie #emotional",
        "description": (
            "'Do not go gentle into that good night.' The tear-jerking promise between Cooper and Murph before leaving Earth.\n\n"
            "Remastered with IMAX deep celestial color grading and enhanced Hans Zimmer soundscape.\n\n"
            "#shorts #interstellar #christophernolan #hanszimmer #matthewmcconaughey #emotional #cinema #space #physics"
        ),
        "tags": ["interstellar", "christopher nolan", "hanszimmer", "matthew mcconaughey", "space movie", "emotional scene", "time dilation", "science", "cinema"],
        "category_id": "1"
    },
    {
        "id_key": "viral_red_notice_egg_heist_comedy",
        "raw_file": "red_notice_egg_raw.mp4",
        "output_file": "red_notice_egg_comedy_master.mp4",
        "banner_file": "red_notice_banner.png",
        "tag_line": "RED NOTICE • CLEOPATRA'S EGG",
        "hook_line": "HE THOUGHT IT WAS GOING TO BE EASY 💀🤣",
        "accent_color": (255, 180, 50),       # Gold Amber
        "fg_width": 1080,
        "fg_height": 1200,
        "fg_y": 360,
        "banner_y": 120,
        "color_eq": "contrast=1.10:brightness=0.02:saturation=1.15",
        "audio_eq": "equalizer=f=85:width_type=o:width=2:g=1.5,equalizer=f=3400:width_type=o:width=1.5:g=1.3",
        "title": "He Thought It Was Going To Be Easy 💀🤣 #shorts #rednotice #funny #moviescene",
        "description": (
            "Ryan Reynolds and The Rock stealing Cleopatra's legendary golden egg. Pure comedy chemistry.\n\n"
            "Remastered with vibrant blockbuster Hollywood saturation and crisp dialogue punch.\n\n"
            "#shorts #rednotice #ryanreynolds #therock #dwaynejohnson #galgadot #funny #comedy #heist #movie"
        ),
        "tags": ["red notice", "ryan reynolds", "the rock", "dwayne johnson", "gal gadot", "funny moments", "comedy", "heist movie", "hollywood"],
        "category_id": "1"
    }
]

def generate_banner(config: dict, output_path: Path):
    """Generates an ultra-crisp glassmorphic hook card."""
    img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    banner_y = config["banner_y"]
    card_height = 175
    x0, y0 = 60, banner_y
    x1, y1 = 1020, banner_y + card_height

    # Semi-transparent dark pill with glow accent border
    bg_rgba = (14, 16, 24, 235)
    accent = config["accent_color"]
    border_rgba = (accent[0], accent[1], accent[2], 210)

    draw.rounded_rectangle([x0, y0, x1, y1], radius=32, fill=bg_rgba, outline=border_rgba, width=3)

    font_tag = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 28)
    font_hook = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 40)

    # Line 1: Tag
    draw.text((540, banner_y + 48), config["tag_line"], font=font_tag, fill=accent, anchor="mm")
    # Line 2: Hook with drop shadow
    hook_y = banner_y + 115
    draw.text((542, hook_y + 2), config["hook_line"], font=font_hook, fill=(0, 0, 0, 180), anchor="mm")
    draw.text((540, hook_y), config["hook_line"], font=font_hook, fill=(255, 255, 255, 255), anchor="mm")

    img.save(str(output_path), "PNG")
    print(f"   🎨 Hook Banner saved: {output_path.name}")

def render_video(config: dict) -> Path:
    """Renders the enhanced vertical short using FFmpeg."""
    raw_path = TEMP_DIR / config["raw_file"]
    banner_path = TEMP_DIR / config["banner_file"]
    out_path = TEMP_DIR / config["output_file"]

    if out_path.exists() and out_path.stat().st_size > 1000000:
        print(f"   ⚡ Master video already rendered: {out_path.name}")
        return out_path

    # Generate banner first
    generate_banner(config, banner_path)

    print(f"   🎬 Encoding master vertical short: {config['output_file']}...")
    fg_w = config["fg_width"]
    fg_h = config["fg_height"]
    fg_y = config["fg_y"]
    c_eq = config["color_eq"]
    a_eq = config["audio_eq"]

    filter_complex = (
        f"[0:v]scale=64:114,scale=1080:1920:flags=bilinear,setsar=1,eq=contrast=0.92:brightness=-0.16[bg]; "
        f"[0:v]scale={fg_w}:{fg_h},setsar=1,eq={c_eq},setpts=PTS/1.015[fg]; "
        f"[bg][fg]overlay=0:{fg_y}[comp]; "
        f"[comp][1:v]overlay=0:0:shortest=1,setsar=1[v]; "
        f"[0:a]atempo=1.015,{a_eq}[a]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", str(raw_path),
        "-loop", "1", "-i", str(banner_path),
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k",
        str(out_path)
    ]

    t0 = time.time()
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"❌ FFmpeg error: {result.stderr[-500:]}")
        raise RuntimeError(f"FFmpeg failed for {config['output_file']}")

    elapsed = time.time() - t0
    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"   ✅ Rendered {out_path.name} in {elapsed:.1f}s ({size_mb:.2f} MB)")
    return out_path

def upload_to_youtube(config: dict, video_path: Path, youtube) -> dict:
    """Uploads video to YouTube as UNLISTED and registers it."""
    clean_title = config["title"].replace("<", "").replace(">", "")[:100]
    clean_desc = config["description"].replace("<", "").replace(">", "")

    body = {
        "snippet": {
            "title": clean_title,
            "description": clean_desc,
            "tags": config["tags"][:20],
            "categoryId": config.get("category_id", "1")
        },
        "status": {
            "privacyStatus": "unlisted",
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(str(video_path), mimetype="video/mp4", resumable=True, chunksize=1024*1024*4)
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    print(f"   📤 Uploading {video_path.name} ({video_path.stat().st_size:,} bytes) as UNLISTED...")
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"      Progress: {int(status.progress() * 100)}%")

    video_id = resp["id"]
    video_url = f"https://youtu.be/{video_id}"
    print(f"   🌟 Upload Success! Video ID: {video_id} | URL: {video_url}")

    # Register in uploaded_videos_registry.json
    registry = json.loads(REGISTRY_FILE.read_text(encoding="utf-8")) if REGISTRY_FILE.exists() else {}
    registry[config["id_key"]] = {
        "title": config["title"],
        "video_id": video_id,
        "url": video_url,
        "file": str(video_path.name),
        "upload_date": "2026-10-17",
        "status": "UNLISTED_VERIFICATION"
    }
    REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")
    print(f"   📝 Logged in {REGISTRY_FILE.name}")
    return {"id": video_id, "url": video_url, "title": config["title"]}

def main():
    print("=" * 75)
    print("🔥 MASTER VIRAL 4-PACK ELEVATION & YOUTUBE PUBLISHER")
    print("=" * 75)

    if not TOKEN_FILE.exists():
        print(f"❌ Token file missing: {TOKEN_FILE}")
        return

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        token_data = json.load(f)
    creds = Credentials.from_authorized_user_info(token_data)
    youtube = build("youtube", "v3", credentials=creds)

    uploaded_summary = []

    for i, cfg in enumerate(VIRAL_CONFIGS, 1):
        print(f"\n[{i}/4] PROCESSING: {cfg['title'][:50]}...")
        # 1. Render
        video_path = render_video(cfg)
        # 2. Upload
        upload_info = upload_to_youtube(cfg, video_path, youtube)
        uploaded_summary.append(upload_info)

    print("\n" + "=" * 75)
    print("🎉 ALL 4 VIRAL SHORTS SUCCESSFULLY ELEVATED AND UPLOADED!")
    print("=" * 75)
    for item in uploaded_summary:
        print(f"• {item['title']}")
        print(f"  URL: {item['url']}  (ID: {item['id']})")
    print("=" * 75)

if __name__ == "__main__":
    main()
