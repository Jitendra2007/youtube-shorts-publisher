"""
OCTOBER 18, 2026 — 9-SHORTS DAILY SCHEDULED PUBLISHER SUITE
=============================================================
Executes the complete 4-pillar daily programming strategy for October 18, 2026:
  Pillar 1: Top Searches of the Day (3 Shorts)
    1. DeepSeek-V3 Open-Weights AI Disruption
    2. Windows 12 Modular Core & Floating UI Leak
    3. NASA James Webb Detects Ocean Atmosphere on Super-Earth K2-18b
  Pillar 2: Specials of That Day (Oct 18) (2 Shorts)
    4. Alaska Day (Oct 18): How USA Bought 586,000 Sq Miles for 2 Cents An Acre
    5. Thomas Edison Legacy (Died Oct 18, 1931): The Secret 100-Year Battery
  Pillar 3: Big Worldwide Events (2 Shorts)
    6. SpaceX Starship In-Orbit Cryogenic Refueling Breakthrough
    7. CRISPR Gene Therapy Restores Vision in Human Blindness Trial
  Pillar 4: Indian Events, Festivals & Smart Offers (2 Shorts)
    8. Diwali 2026 Wealth Guide: Gold vs Silver 10-Year Return Statistics
    9. UPI ATM Without Debit Card: How Indians Withdraw Cash via QR Code

Key Enhancement:
  - Staggered Scheduled Publishing (publishAt): All 9 upload immediately in private mode,
    then YouTube's cloud automatically publishes each at peak Indian viewer hours throughout the day!
"""

import os, sys, re, json, asyncio, subprocess, time
from datetime import datetime, timezone
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import imageio_ffmpeg, edge_tts
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from media_processor import fetch_accurate_scene_image, format_to_vertical_9x16

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output_shorts" / "today_special_days_present_events"
TEMP_DIR   = BASE_DIR / "temp_oct18_production"
ASSETS_DIR = BASE_DIR / "assets"
SFX_DIR    = ASSETS_DIR / "sfx"
BGM_DIR    = ASSETS_DIR / "bgm"
TOKEN_FILE = BASE_DIR / "token.json"
REGISTRY_FILE = BASE_DIR / "uploaded_videos_registry.json"

BGM_SPACE   = BGM_DIR / "space_tech" / "space_exploration_synth.mp3"
BGM_MYSTERY = BGM_DIR / "psychology_mystery" / "ambient_mystery_drone.mp3"
BGM_LOFI    = BGM_DIR / "nature_history_lofi" / "warm_lofi_pad.mp3"

for d in [OUTPUT_DIR, TEMP_DIR]:
    d.mkdir(parents=True, exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/impact.ttf" if Path("C:/Windows/Fonts/impact.ttf").exists() else "C:/Windows/Fonts/arialbd.ttf"
VOICE = "en-US-AvaNeural"


def get_audio_duration(path: Path) -> float:
    res = subprocess.run(
        [FFMPEG, "-i", str(path), "-f", "null", "-"],
        stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, text=True, errors="replace"
    )
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        h, mn, s = m.groups()
        return int(h)*3600 + int(mn)*60 + float(s)
    return 3.5


def create_lower_third_frame(bg_image_path: Path, text: str, highlight_word: str) -> Image.Image:
    target_w, target_h = 1080, 1920
    try:
        im = Image.open(bg_image_path).convert("RGB")
    except Exception:
        im = Image.new("RGB", (target_w, target_h), (12, 16, 28))

    if im.size != (target_w, target_h):
        im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 74)
    line_h = 92

    words = text.split()
    lines, curr = [], []
    for w in words:
        test = " ".join(curr + [w])
        bbox = draw.textbbox((0, 0), test, font=font)
        if (bbox[2] - bbox[0]) < 920:
            curr.append(w)
        else:
            if curr: lines.append(" ".join(curr))
            curr = [w]
    if curr: lines.append(" ".join(curr))

    total_text_h = len(lines) * line_h
    start_y = 1460 - (total_text_h // 2)

    bar_margin = 35
    bar_top = start_y - 25
    bar_bottom = start_y + total_text_h + 20
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rounded_rectangle([bar_margin, bar_top, target_w - bar_margin, bar_bottom], radius=20, fill=(0, 0, 0, 150))
    im.paste(overlay, (0, 0), overlay)
    draw = ImageDraw.Draw(im)

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        x = (target_w - lw) // 2
        line_words = line.split()
        cur_x = x
        for w in line_words:
            w_box = draw.textbbox((0, 0), w, font=font)
            w_len = w_box[2] - w_box[0]
            clean_w = re.sub(r"[^\w]", "", w).lower()
            clean_hl = re.sub(r"[^\w]", "", highlight_word).lower()
            color = (255, 235, 59) if clean_w == clean_hl else (255, 255, 255)
            draw.text((cur_x+3, start_y+3), w, font=font, fill=(0, 0, 0))
            draw.text((cur_x, start_y), w, font=font, fill=color)
            sp_box = draw.textbbox((0, 0), " ", font=font)
            cur_x += w_len + (sp_box[2] - sp_box[0])
        start_y += line_h
    return im


async def synthesize_speech(text: str, out_path: Path):
    communicate = edge_tts.Communicate(text, VOICE, rate="+8%", pitch="+1Hz")
    await communicate.save(str(out_path))


def build_scene_clip(img_path: Path, voice_path: Path, sfx_path: Path, output_clip: Path, is_first: bool = False):
    dur = max(get_audio_duration(voice_path), 3.0)
    pan_w = 1200
    pan_h = int(pan_w * (1920/1080))
    x_expr = f"'(iw-ow)*(1-t/{dur:.2f})'" if is_first else f"'(iw-ow)*(t/{dur:.2f})'"

    filter_complex = (
        f"[0:v]scale={pan_w}:{pan_h},crop=1080:1920:x={x_expr}:y=(in_h-out_h)/2[v];"
    )

    inputs = ["-loop", "1", "-i", str(img_path), "-i", str(voice_path)]
    if sfx_path and sfx_path.exists():
        inputs.extend(["-i", str(sfx_path)])
        filter_complex += "[1:a]volume=1.0[voice];[2:a]volume=0.22[sfx];[voice][sfx]amix=inputs=2:duration=first[aout]"
        audio_map = "[aout]"
    else:
        filter_complex += "[1:a]volume=1.0[aout]"
        audio_map = "[aout]"

    cmd = [
        FFMPEG, "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", audio_map,
        "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-t", str(dur),
        str(output_clip)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)


def safe_filter_concat_with_bgm(clips: list, bgm_path: Path, final_out: Path):
    total_dur = sum(get_audio_duration(c) for c in clips)
    inputs = []
    for c in clips:
        inputs.extend(["-i", str(c)])
    inputs.extend(["-stream_loop", "-1", "-i", str(bgm_path)])

    n = len(clips)
    audio_norm  = "".join(f"[{i}:a]aresample=44100,asetpts=N/SR/TB[a{i}];" for i in range(n))
    video_concat = "".join(f"[{i}:v]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vcat];"
    audio_concat = "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[acat];"
    mix_filter   = (
        f"[acat]volume=1.0[voice];"
        f"[{n}:a]volume=0.08,atrim=0:{total_dur:.3f},"
        f"afade=t=in:st=0:d=1.5,"
        f"afade=t=out:st={max(0, total_dur - 2.5):.3f}:d=2.5,"
        f"aresample=44100[bgm];"
        f"[voice][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]"
    )
    full_filter = audio_norm + video_concat + audio_concat + mix_filter

    cmd = [
        FFMPEG, "-y", *inputs,
        "-filter_complex", full_filter,
        "-map", "[vcat]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-t", str(total_dur),
        str(final_out)
    ]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if result.returncode != 0:
        err = result.stderr.decode("utf-8", errors="replace")[-3000:]
        raise RuntimeError(f"FFmpeg gapless concat FAILED:\n{err}")


OCT18_MANIFEST = [
    # ─── PILLAR 1: TOP SEARCHES OF THE DAY (3 SHORTS) ───
    {
        "key": "search_oct18_deepseek_v3_open_weights_disruption",
        "title": "This Open Source AI Just Embarrassed Silicon Valley 🧠⚡ #shorts #ai #tech",
        "description": (
            "A breakthrough open-weights AI model called DeepSeek-V3 just matched OpenAI and Anthropic's top models at a fraction of the cost!\n\n"
            "Using Multi-Head Latent Attention and Mixture of Experts, this architecture trained on only 2,048 GPUs compared to the 100,000 GPU clusters in the US.\n\n"
            "Will open source AI win the ultimate intelligence race? Drop your thoughts below!\n\n"
            "#shorts #ai #deepseek #artificialintelligence #tech #technology #coding #siliconvalley #curiouscodex"
        ),
        "tags": ["shorts", "artificial intelligence", "deepseek", "ai news", "open source", "tech news", "machine learning", "curiouscodex"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-18T04:00:00Z",  # 09:30 AM IST
        "scenes": [
            {
                "wiki": "Deep_learning",
                "commons": "Futuristic artificial intelligence neural network glowing nodes data center",
                "pinterest": "futuristic AI neural network glowing cyan nodes cyber core wallpaper",
                "query": "artificial intelligence glowing neural network cyan tech",
                "text": "An open source artificial intelligence just matched Silicon Valley's top proprietary models at one tenth of the cost!",
                "hl": "intelligence",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Graphics_processing_unit",
                "commons": "High tech server room glowing racks modern data center computing",
                "pinterest": "futuristic data center server racks glowing blue neon lighting",
                "query": "futuristic supercomputer GPU server room blue neon",
                "text": "While tech giants spent hundreds of millions on massive GPU clusters, this architecture was trained in just two months.",
                "hl": "clusters",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Mixture_of_experts",
                "commons": "Complex computer chip motherboard glowing microchip technology",
                "pinterest": "quantum computer chip glowing circuit traces microscopic futuristic",
                "query": "futuristic processor chip glowing gold circuits technology",
                "text": "By activating only a small fraction of its six hundred billion parameters per token, it achieves blistering inference speeds.",
                "hl": "speeds",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Open-source_software",
                "commons": "World connected digital glowing holographic network globe",
                "pinterest": "holographic digital globe network connections futuristic science",
                "query": "digital glowing globe network connections cyber tech",
                "text": "For the first time, independent researchers across the world hold state of the art frontier intelligence right on their laptops.",
                "hl": "intelligence",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },
    {
        "key": "search_oct18_windows_12_modular_core_leak",
        "title": "Windows 12 Just Leaked: Microsoft Changed Everything 💻👀 #shorts #tech #windows",
        "description": (
            "Internal Microsoft leaks reveal the brand-new architectural redesign for Windows 12!\n\n"
            "Code-named Next Valley, Windows 12 separates the operating system into state-separated modular partitions, featuring a floating taskbar, dynamic AI search, and instant updates.\n\n"
            "Are you excited for the next era of PC computing? Subscribe for more daily tech leaks!\n\n"
            "#shorts #windows #windows12 #microsoft #tech #pcgaming #software #gadgets #curiouscodex"
        ),
        "tags": ["shorts", "windows 12", "microsoft", "tech news", "pc", "software", "windows", "curiouscodex"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-18T05:30:00Z",  # 11:00 AM IST
        "scenes": [
            {
                "wiki": "Microsoft_Windows",
                "commons": "Modern sleek laptop illuminated keyboard floating futuristic desktop interface",
                "pinterest": "futuristic glass laptop glowing desktop interface cyber aesthetics",
                "query": "futuristic laptop glowing sleek keyboard glass display",
                "text": "Leaked internal builds from Microsoft reveal Windows Twelve is undergoing the biggest architectural overhaul in two decades!",
                "hl": "overhaul",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Graphical_user_interface",
                "commons": "Futuristic clean minimalist software interface modern design glassmorphism",
                "pinterest": "minimalist futuristic UI glassmorphism modern desktop aesthetic",
                "query": "futuristic UI interface modern glassmorphism design",
                "text": "The iconic desktop now features a floating pill shaped taskbar and dynamic system widgets that adapt to your daily habits.",
                "hl": "floating",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Operating_system",
                "commons": "Computer motherboard glowing circuits high speed memory architecture",
                "pinterest": "futuristic computer motherboard glowing traces high tech hardware",
                "query": "futuristic computer motherboard glowing circuits microchip",
                "text": "Behind the scenes, state separation completely isolates system files, preventing corrupt updates and malware crashes permanently.",
                "hl": "isolates",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Personal_computer",
                "commons": "Futuristic workstation dual monitors glowing ambient lights workspace",
                "pinterest": "clean minimalist desk setup glowing ambient lighting ultrawide monitor",
                "query": "clean minimalist computer desk setup glowing ambient lights",
                "text": "Early performance benchmarks show up to thirty percent better battery life and near instant system boot times.",
                "hl": "battery",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },
    {
        "key": "search_oct18_jwst_exoplanet_ocean_k218b",
        "title": "NASA's Telescope Found Ocean Signals On An Alien Super-Earth 🔭🌊 #shorts #space #nasa",
        "description": (
            "The James Webb Space Telescope has detected carbon-bearing molecules and ocean atmosphere signals on exoplanet K2-18b!\n\n"
            "Located 120 light-years away in the habitable zone of Leo, K2-18b is 8.6 times the mass of Earth and may be a Hycean world with a liquid water ocean.\n\n"
            "Could alien life already be swimming in its oceans? Comment your thoughts below!\n\n"
            "#shorts #space #nasa #astronomy #jameswebb #science #universe #alien #curiouscodex"
        ),
        "tags": ["shorts", "space", "james webb", "nasa", "exoplanet", "astronomy", "alien life", "science", "curiouscodex"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-18T07:00:00Z",  # 12:30 PM IST
        "scenes": [
            {
                "wiki": "K2-18b",
                "commons": "Artist impression of an exoplanet ocean world with atmosphere and star",
                "pinterest": "artist impression alien planet ocean water atmosphere starry cosmos",
                "query": "alien super earth exoplanet ocean atmosphere space",
                "text": "One hundred and twenty light years away, NASA's James Webb Space Telescope just observed signs of an ocean covered super Earth!",
                "hl": "ocean",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "James_Webb_Space_Telescope",
                "commons": "James Webb Space Telescope in deep space with golden hexagonal mirrors",
                "pinterest": "James Webb space telescope golden mirrors deep cosmos stars",
                "query": "James Webb space telescope gold mirrors deep cosmos",
                "text": "By analyzing starlight filtering through the planet's atmosphere, Webb detected methane, carbon dioxide, and dimethyl sulfide.",
                "hl": "atmosphere",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Hycean_planet",
                "commons": "Deep blue ocean surface on distant alien planet under starlit sky",
                "pinterest": "vast deep blue ocean planet surface under alien starry sky",
                "query": "alien ocean planet vast water surface starlit sky",
                "text": "On Earth, this specific chemical signature is only produced by living marine organisms like phytoplankton in ocean waters.",
                "hl": "organisms",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Extraterrestrial_life",
                "commons": "Glowing spiral galaxy in deep space with billions of stars cosmic wonder",
                "pinterest": "epic spiral galaxy deep space nebula glowing stars universe",
                "query": "deep space glowing spiral galaxy cosmic wonder stars",
                "text": "Scientists believe this could be our very first glimpse of an alien biological world in the vast cosmic ocean.",
                "hl": "biological",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    # ─── PILLAR 2: SPECIALS OF THAT DAY (OCT 18) (2 SHORTS) ───
    {
        "key": "special_oct18_alaska_purchase_2_cents_acre",
        "title": "How America Bought Alaska for Just 2 Cents An Acre ❄️🇺🇸 #shorts #history #facts",
        "description": (
            "On October 18, 1867, Russia formally transferred 586,000 square miles of Alaska to the United States!\n\n"
            "At the time, newspapers mocked Secretary of State William Seward, calling it 'Seward's Folly' and an iceberg wasteland. "
            "Then Americans discovered billions of dollars in gold, oil, and untouched natural resources.\n\n"
            "Was this the greatest land deal in world history? Subscribe to Curious Codex for daily historical wonders!\n\n"
            "#shorts #history #alaska #facts #usa #russia #money #education #curiouscodex"
        ),
        "tags": ["shorts", "history", "alaska", "alaska day", "usa", "facts", "money", "historical facts", "curiouscodex"],
        "bgm": BGM_LOFI,
        "publish_at": "2026-10-18T08:30:00Z",  # 02:00 PM IST
        "scenes": [
            {
                "wiki": "Alaska_Purchase",
                "commons": "Signing of the Alaska treaty 1867 historical painting historical figures",
                "pinterest": "historical painting signing treaty 19th century vintage sepia",
                "query": "signing of Alaska treaty 1867 historical painting",
                "text": "On this exact day in eighteen sixty-seven, the United States bought Alaska from Russia for just two cents an acre!",
                "hl": "bought",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "William_H._Seward",
                "commons": "Historical portrait of Secretary of State William H Seward 19th century",
                "pinterest": "vintage 19th century historical statesman portrait photography",
                "query": "vintage portrait 19th century statesman sepia photo",
                "text": "Newspapers ruthlessly mocked the deal as Seward's Folly, claiming America had purchased nothing but giant polar bears and ice.",
                "hl": "mocked",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Klondike_Gold_Rush",
                "commons": "Historical gold miners panning for gold in Alaska Yukon gold rush vintage",
                "pinterest": "gold rush miners historic vintage photography panning river",
                "query": "Klondike gold rush miners historical vintage photo",
                "text": "Just three decades later, prospectors discovered gold nuggets the size of fists, paying back the purchase price many times over.",
                "hl": "gold",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Alaska",
                "commons": "Stunning snow-capped Alaska mountain landscape with emerald river reflection",
                "pinterest": "Alaska snowy mountains emerald lake pine forest epic landscape",
                "query": "Alaska snowy mountains emerald lake landscape majestic",
                "text": "Today, Alaska's trillion dollar oil and strategic minerals make it the most profitable land bargain in modern human history.",
                "hl": "profitable",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },
    {
        "key": "special_oct18_thomas_edison_100_year_battery",
        "title": "Thomas Edison Died Today in 1931 Leaving A 100-Year Battery Secret 💡🔋 #shorts #science #history",
        "description": (
            "Prolific inventor Thomas Alva Edison passed away on October 18, 1931 with 1,093 patents to his name!\n\n"
            "Among his greatest unsung inventions was the nickel-iron alkaline battery — an indestructible energy cell that literally works for over 100 years without degradation!\n\n"
            "Why aren't we using this today? Find out and subscribe for daily science breakthroughs!\n\n"
            "#shorts #science #thomasedison #edison #history #inventor #battery #tech #curiouscodex"
        ),
        "tags": ["shorts", "thomas edison", "science", "inventions", "history", "battery", "technology", "curiouscodex"],
        "bgm": BGM_MYSTERY,
        "publish_at": "2026-10-18T10:00:00Z",  # 03:30 PM IST
        "scenes": [
            {
                "wiki": "Thomas_Edison",
                "commons": "Thomas Edison in laboratory vintage historic black and white portrait",
                "pinterest": "Thomas Edison vintage laboratory portrait black and white historic",
                "query": "Thomas Edison laboratory historic vintage portrait",
                "text": "Thomas Edison passed away on this day in nineteen thirty-one, but his most overlooked invention could solve our energy crisis today!",
                "hl": "invention",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Nickel%E2%80%93iron_battery",
                "commons": "Vintage Edison storage battery alkaline cell historical engineering artifact",
                "pinterest": "antique electrical battery apparatus vintage brass glass laboratory",
                "query": "vintage electrical battery Edison cell historic laboratory",
                "text": "Edison created a rechargeable nickel-iron battery so indestructible that units built a century ago still hold electrical charge today.",
                "hl": "indestructible",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Lithium-ion_battery",
                "commons": "Modern battery cells manufacturing laboratory electric vehicle power",
                "pinterest": "modern lithium battery cells glowing green energy technology",
                "query": "modern battery technology glowing energy storage cells",
                "text": "Unlike modern lithium batteries that degrade after three years, Edison's iron chemistry thrives on overcharging and extreme temperatures.",
                "hl": "chemistry",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Renewable_energy",
                "commons": "Massive solar panel farm with modern wind turbines green energy landscape",
                "pinterest": "futuristic solar panels wind turbines sunset green energy landscape",
                "query": "solar panels wind turbines green renewable energy landscape",
                "text": "Now, renewable energy researchers are dusting off his hundred year old patents to build lifetime storage for solar and wind grids.",
                "hl": "lifetime",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    # ─── PILLAR 3: BIG WORLDWIDE EVENTS (2 SHORTS) ───
    {
        "key": "world_event_oct18_starship_orbital_refueling_breakthrough",
        "title": "SpaceX Just Solved The Hardest Engineering Problem In History 🚀🌌 #shorts #spacex #elonmusk",
        "description": (
            "SpaceX has completed critical in-space cryogenic propellant transfer tests, unlocking the missing key for human Mars colonization!\n\n"
            "Launching Starship into orbit requires burning 90% of its fuel. By docking two Starships in orbit and pumping super-chilled liquid methane and oxygen, Starship can travel anywhere in the Solar System.\n\n"
            "Will humans walk on Mars before 2030? Comment your prediction below!\n\n"
            "#shorts #spacex #starship #elonmusk #mars #space #rocket #astronomy #science #curiouscodex"
        ),
        "tags": ["shorts", "spacex", "starship", "elon musk", "mars", "space exploration", "rocket", "science", "curiouscodex"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-18T11:30:00Z",  # 05:00 PM IST
        "scenes": [
            {
                "wiki": "SpaceX_Starship",
                "commons": "SpaceX Starship stainless steel rocket glowing engines launch pad",
                "pinterest": "SpaceX Starship launch stainless steel rocket glowing exhaust epic",
                "query": "SpaceX Starship rocket stainless steel launch glowing fire",
                "text": "SpaceX has just mastered the single most critical breakthrough needed to send human civilization to the surface of Mars!",
                "hl": "breakthrough",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Orbital_refueling",
                "commons": "Two futuristic spacecraft docking together in Earth orbit space render",
                "pinterest": "two spaceships docking in orbit above planet Earth sci-fi render",
                "query": "two spacecraft docking in Earth orbit space render",
                "text": "Because reaching orbit consumes nearly all fuel, Starship must rendezvous with a tanker ship to refill its cryogenic propellant tanks.",
                "hl": "refill",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Liquid_propellant_rocket",
                "commons": "Extreme cold cryogenic liquid nitrogen vapor plume rocket testing facility",
                "pinterest": "cryogenic liquid vapor rocket engine test fire intense thrust",
                "query": "cryogenic liquid oxygen vapor rocket test facility",
                "text": "Pumping liquid oxygen and super-cooled methane at minus two hundred degrees in zero gravity was once thought impossible.",
                "hl": "impossible",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Human_mission_to_Mars",
                "commons": "Planet Mars glowing red surface with starry space background high detail",
                "pinterest": "planet Mars red surface starry space exploration cinematic wallpaper",
                "query": "planet Mars red surface starry cosmos space background",
                "text": "With full tanks in orbit, a single Starship can carry one hundred humans and a hundred tons of cargo directly to the Red Planet.",
                "hl": "cargo",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },
    {
        "key": "world_event_oct18_crispr_human_blindness_restoration",
        "title": "Doctors Used Gene-Editing To Restore Human Sight From Total Darkness 👁️🧬 #shorts #science #health",
        "description": (
            "Clinical trial milestones confirm that in vivo CRISPR gene editing has successfully restored vision in patients with congenital blindness!\n\n"
            "Using microscopic molecular scissors injected directly behind the retina, scientists corrected the mutated CEP290 gene, allowing dormant light-sensing cells to turn back on.\n\n"
            "We are living in the golden age of medical science. Subscribe for daily breakthroughs!\n\n"
            "#shorts #science #medicine #crispr #genetherapy #health #doctor #biology #tech #curiouscodex"
        ),
        "tags": ["shorts", "crispr", "gene editing", "medicine", "health", "science news", "biology", "curiouscodex"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-18T13:00:00Z",  # 06:30 PM IST
        "scenes": [
            {
                "wiki": "CRISPR",
                "commons": "Stylized glowing DNA double helix strand molecular biology medical science",
                "pinterest": "glowing DNA double helix molecular biotechnology blue neon wallpaper",
                "query": "glowing DNA double helix biotechnology blue neon",
                "text": "Medical researchers have achieved what was once considered a miracle, using gene editing to restore vision in blind patients!",
                "hl": "restore",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Retina",
                "commons": "Human eye closeup glowing iris pupil detailed medical photography",
                "pinterest": "extreme closeup human eye glowing iris pupil detailed macro photography",
                "query": "macro closeup human eye glowing iris pupil detailed",
                "text": "Patients suffering from genetic retinal dystrophy lived in near total darkness because a single mutated gene disabled their photoreceptors.",
                "hl": "photoreceptors",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Gene_therapy",
                "commons": "Microscopic needle injecting gene therapy cell biological research",
                "pinterest": "microscopic cell injection laboratory biotechnology research 3D",
                "query": "microscopic cell injection biotechnology medical laboratory",
                "text": "Surgeons delivered microscopic CRISPR molecular scissors directly under the retina, repairing the genetic defect inside living cells.",
                "hl": "repairing",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Visual_perception",
                "commons": "Smiling person looking at colorful sunset city skyline bright vision",
                "pinterest": "person looking at vibrant sunset city skyline happy freedom aesthetic",
                "query": "happy person looking at colorful vibrant sunset vision",
                "text": "Weeks later, dormant retinal cells revived, allowing patients to see colors, faces, and sunlight for the first time in their lives.",
                "hl": "sunlight",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    # ─── PILLAR 4: INDIAN EVENTS, FESTIVALS & SMART OFFERS (2 SHORTS) ───
    {
        "key": "india_oct18_diwali_gold_vs_silver_wealth_comparison",
        "title": "Gold vs Silver This Diwali: The 10-Year Return Shocked Everyone 🪙📈 #shorts #india #finance",
        "description": (
            "Before buying gold or silver this Dhanteras and Diwali, look at the historical data!\n\n"
            "While 24K gold has delivered a steady 11% compound annual growth rate in India, industrial demand for silver from solar panels and EV batteries is surging demand by over 30%.\n\n"
            "Which precious metal are you accumulating this festive season? Comment below and share with your family!\n\n"
            "#shorts #india #diwali #dhanteras #gold #silver #investment #finance #money #curiouscodex"
        ),
        "tags": ["shorts", "diwali", "dhanteras", "gold investment", "silver", "personal finance", "india", "curiouscodex"],
        "bgm": BGM_LOFI,
        "publish_at": "2026-10-18T14:30:00Z",  # 08:00 PM IST
        "scenes": [
            {
                "wiki": "Dhanteras",
                "commons": "Traditional Indian golden coins and jewelry on festive decorative plate Diwali",
                "pinterest": "festive Indian gold coins jewelry traditional Dhanteras Diwali aesthetic",
                "query": "traditional Indian gold coins jewelry festive Diwali plate",
                "text": "Before you rush to buy gold this festive season, the historical returns between gold and silver might shock you!",
                "hl": "shock",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Gold_as_an_investment",
                "commons": "Shiny pure gold bullion bars stacked high wealth luxury financial",
                "pinterest": "pure gold bullion bars stacked wealth banking investment aesthetic",
                "query": "pure gold bullion bars stacked financial wealth",
                "text": "Over the past decade, Indian gold has compounded at eleven percent annually, flawlessly beating inflation year after year.",
                "hl": "inflation",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Silver_as_an_investment",
                "commons": "Pure silver bullion ingots and coins gleaming metallic finish",
                "pinterest": "pure silver bullion bars shining ingots precious metal wealth",
                "query": "pure silver bullion bars shining precious metal wealth",
                "text": "However, silver is facing massive industrial deficits because every single electric car and solar panel requires ounces of silver.",
                "hl": "deficits",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Diwali",
                "commons": "Illuminated festive Diwali oil lamps diyas glowing celebration golden light",
                "pinterest": "Diwali glowing traditional clay diyas golden light festive night",
                "query": "Diwali glowing clay diyas traditional golden light celebration",
                "text": "Smart Indian investors are now balancing both metals, capturing the safety of gold alongside the explosive growth of silver.",
                "hl": "growth",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },
    {
        "key": "india_oct18_upi_atm_cardless_cash_withdrawal",
        "title": "Forgot Your ATM Card? Indian ATMs Now Give Cash via UPI QR Code! 🏧📲 #shorts #india #tech",
        "description": (
            "Did you know Indian ATMs now let you withdraw cash in 15 seconds without carrying any physical debit card?\n\n"
            "Using Interoperable Cardless Cash Withdrawal (ICCW), you simply select UPI Cash on the screen, scan the dynamic QR code with Google Pay, PhonePe, or BHIM, and collect your currency notes with zero skimming risk.\n\n"
            "Have you used this feature yet? Share this smart tip with your friends!\n\n"
            "#shorts #india #upi #atm #banking #technology #googlepay #phonepe #finance #curiouscodex"
        ),
        "tags": ["shorts", "upi", "atm", "banking", "india tech", "google pay", "phonepe", "cash", "curiouscodex"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-18T16:00:00Z",  # 09:30 PM IST
        "scenes": [
            {
                "wiki": "Automated_teller_machine",
                "commons": "Person using modern ATM machine screen cash withdrawal transaction",
                "pinterest": "person standing at modern ATM illuminated screen cash withdrawal",
                "query": "person using modern ATM machine cash withdrawal screen",
                "text": "You never have to carry a plastic ATM card in India again thanks to this new nationwide banking feature!",
                "hl": "banking",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Unified_Payments_Interface",
                "commons": "Smartphone scanning QR code payment modern digital transaction technology",
                "pinterest": "smartphone scanning glowing QR code digital payment fintech aesthetic",
                "query": "smartphone scanning dynamic QR code digital payment",
                "text": "At any updated ATM, simply tap UPI Cash on the screen to generate a dynamic one-time QR code.",
                "hl": "dynamic",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "QR_code",
                "commons": "Hand holding smartphone confirming mobile payment successful checkmark",
                "pinterest": "smartphone screen showing green successful payment confirmation UI",
                "query": "smartphone screen successful mobile payment confirmation green",
                "text": "Scan it with PhonePe, Google Pay, or Paytm, enter your UPI pin, and the cash dispenses instantly.",
                "hl": "instantly",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Indian_rupee",
                "commons": "Crisp new Indian rupee banknotes 500 currency notes stacked neatly",
                "pinterest": "new Indian five hundred rupee banknotes currency wealth finance",
                "query": "crisp Indian five hundred rupee currency notes stacked",
                "text": "Because there is no physical card to swipe, card skimming and pin cloning scams are eliminated completely.",
                "hl": "eliminated",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    }
]


def render_short(item: dict) -> Path:
    key   = item["key"]
    title = item["title"]
    bgm   = item["bgm"]
    final_out = OUTPUT_DIR / f"{key}_viral_master.mp4"

    if final_out.exists() and final_out.stat().st_size > 1000000:
        print(f"  ⚡ Already rendered: {final_out.name}")
        return final_out

    print(f"\n{'='*75}\n  RENDERING: {title}\n{'='*75}")
    short_temp = TEMP_DIR / key
    short_temp.mkdir(parents=True, exist_ok=True)

    clip_paths = []
    for i, sc in enumerate(item["scenes"], 1):
        print(f"  [Scene {i}/4] {sc['text'][:55]}...")
        clean_img  = short_temp / f"clean_{i}.jpg"
        framed_img = short_temp / f"frame_{i}.jpg"
        voice_path = short_temp / f"voice_{i}.mp3"
        clip_path  = short_temp / f"clip_{i}.mp4"

        # 1. Image
        if not framed_img.exists():
            raw_img_file = fetch_accurate_scene_image(
                wiki_title=sc.get("wiki"),
                commons_query=sc.get("commons"),
                pinterest_query=sc.get("pinterest"),
                fallback_query=sc.get("query"),
                dest_name=f"{key}_scene_{i}"
            )
            format_to_vertical_9x16(raw_img_file, clean_img)
            frame = create_lower_third_frame(clean_img, sc["text"], sc["hl"])
            frame.save(framed_img, "JPEG", quality=95)

        # 2. Voice
        if not voice_path.exists():
            asyncio.run(synthesize_speech(sc["text"], voice_path))

        # 3. Clip
        sfx = sc.get("sfx")
        build_scene_clip(framed_img, voice_path, sfx, clip_path, is_first=(i==1))
        clip_paths.append(clip_path)

    # 4. Gapless Concat
    print(f"  --> Concat 4 clips with GAPLESS filter & BGM...")
    safe_filter_concat_with_bgm(clip_paths, bgm, final_out)
    print(f"  --> Master render complete: {final_out.name} ({final_out.stat().st_size//1024} KB)")
    return final_out


def get_youtube_service():
    if not TOKEN_FILE.exists():
        raise FileNotFoundError(f"token.json not found at {TOKEN_FILE}")
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    creds = Credentials.from_authorized_user_info(data)
    return build("youtube", "v3", credentials=creds)


def upload_scheduled_short(youtube, video_path: Path, title: str, description: str, tags: list, publish_at_iso: str) -> str:
    clean_title = title.replace("<", "").replace(">", "")[:100]
    clean_desc  = description.replace("<", "").replace(">", "")
    
    # YouTube API Rule: If publishAt is set, privacyStatus MUST be 'private'
    body = {
        "snippet": {
            "title": clean_title,
            "description": clean_desc,
            "tags": tags[:25],
            "categoryId": "27"  # Education
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_at_iso,
            "selfDeclaredMadeForKids": False
        }
    }
    media = MediaFileUpload(str(video_path), mimetype="video/mp4", resumable=True, chunksize=4*1024*1024)
    req   = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"      [{pct:3d}%] uploading...")
    return resp["id"]


def main():
    print("=" * 80)
    print("  OCTOBER 18, 2026 — 9-SHORTS DAILY SCHEDULED SUITE")
    print("=" * 80)

    # Step 1: Render all 9 shorts
    rendered_shorts = []
    for idx, item in enumerate(OCT18_MANIFEST, 1):
        print(f"\n[{idx}/9] Starting render: {item['key']}")
        out_mp4 = render_short(item)
        rendered_shorts.append((item, out_mp4))

    # Step 2: Upload all 9 to YouTube with scheduled publish times
    print("\n" + "=" * 80)
    print("  STARTING YOUTUBE SCHEDULED UPLOADS (OCTOBER 18 SUITE)")
    print("=" * 80)

    youtube = get_youtube_service()

    registry = {}
    if REGISTRY_FILE.exists():
        try:
            registry = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
        except Exception:
            registry = {}

    for idx, (item, out_mp4) in enumerate(rendered_shorts, 1):
        key = item["key"]
        title = item["title"]
        pub_time = item["publish_at"]
        print(f"\n--> [{idx}/9] Uploading Scheduled Short: {title[:55]}...")
        print(f"    Target Publish Time (UTC): {pub_time}")

        vid_id = upload_scheduled_short(
            youtube=youtube,
            video_path=out_mp4,
            title=title,
            description=item["description"],
            tags=item["tags"],
            publish_at_iso=pub_time
        )
        live_url = f"https://youtu.be/{vid_id}"
        print(f"    SUCCESS (SCHEDULED): {live_url}")

        registry[key] = {
            "title": title,
            "video_id": vid_id,
            "url": live_url,
            "file": out_mp4.name,
            "upload_date": "2026-10-18",
            "publish_at": pub_time,
            "status": "SCHEDULED"
        }
        REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")

    print("\n" + "=" * 80)
    print("  ALL 9 OCTOBER 18 SHORTS RENDERED & SCHEDULED SUCCESSFULLY!")
    print("  YouTube's cloud will automatically release each short at peak hours today!")
    print("=" * 80)


if __name__ == "__main__":
    main()
