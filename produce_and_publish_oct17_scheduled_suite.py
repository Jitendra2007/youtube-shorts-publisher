"""
OCTOBER 17, 2026 — 9-SHORTS DAILY SCHEDULED PUBLISHER SUITE
=============================================================
Executes the complete 4-pillar daily programming strategy:
  Pillar 1: Top Searches of the Day (3 Shorts)
    1. GTA 6 Leaked Fluid & Muscle Physics Engine
    2. Apple iPhone 17 Air Ultra-Thin Redesign
    3. Comet Tsuchinshan-ATLAS: 80,000-Year Naked-Eye Comet Passing Earth
  Pillar 2: Specials of That Day (Oct 17) (2 Shorts)
    4. International Day for Eradication of Poverty: UBI Cash Trials
    5. Oct 17, 1973 Oil Shock: The Morning That Changed the Global Energy Economy
  Pillar 3: Big Worldwide Events (2 Shorts)
    6. SpaceX Mechazilla 250-Ton Super Heavy Booster Chopstick Catch
    7. Nuclear Fusion Record: High-Temp Superconducting Magnet Breakthrough
  Pillar 4: Indian Events, Festivals & Smart Offers (2 Shorts)
    8. Festive Gold Buying Tax Hack: How Smart Indians Avoid 3% GST & Wealth Tax
    9. Indian Railways AI Dynamic Allocation: Ending Festival Train Waiting Lists

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
TEMP_DIR   = BASE_DIR / "temp_oct17_production"
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


OCT17_MANIFEST = [
    # ─── PILLAR 1: TOP SEARCHES OF THE DAY (3 SHORTS) ───
    {
        "key": "search_oct17_gta6_trailer2_physics_leak",
        "title": "GTA 6 Leaked Physics Engine Is Smarter Than Real Life 🎮🔥 #shorts #gaming #gta6",
        "description": (
            "Rockstar insider leaks reveal the groundbreaking internal physics engine for Grand Theft Auto VI!\n\n"
            "GTA 6 simulates real-time fluid dynamics on vehicles, realistic muscle strain, dynamic weather-based traction, "
            "and NPC memory systems that react to how you drive.\n\n"
            "Will GTA 6 be the greatest video game ever made? Drop your prediction below!\n\n"
            "#shorts #gaming #gta6 #rockstar #videogames #leak #gamingnews #gta #future #curiouscodex"
        ),
        "tags": ["shorts", "gta 6", "rockstar games", "gaming news", "physics engine", "gta vi", "leaked", "video games"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-17T03:30:00Z",  # 09:00 AM IST
        "scenes": [
            {
                "wiki": "Grand_Theft_Auto_VI",
                "commons": "Video game neon city skyline night futuristic action",
                "pinterest": "GTA 6 Vice City neon skyline palm trees night aesthetic",
                "query": "GTA 6 Vice city neon skyline night aesthetic",
                "text": "Leaked development files for GTA Six reveal a physics engine so advanced it simulates real human biology!",
                "hl": "physics",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Game_physics",
                "commons": "Vehicle collision damage simulation computer graphics physics",
                "pinterest": "car crash deformation physics engine simulation 3D graphics",
                "query": "vehicle crash deformation physics engine simulation 3D",
                "text": "Cars now feature procedural metal deformation, real wind resistance, and water that puddles based on road slopes.",
                "hl": "deformation",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Non-player_character",
                "commons": "Crowd of pedestrians realistic city street simulation gaming",
                "pinterest": "realistic pedestrian crowd city street gaming graphics 3D",
                "query": "realistic pedestrian crowd city street gaming graphics",
                "text": "Every NPC remembers your previous interactions and will call the police or seek revenge days later.",
                "hl": "revenge",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Rockstar_Games",
                "commons": "Rockstar Games logo gaming developer high quality studio",
                "pinterest": "Rockstar games gold logo dark background cinematic wallpaper",
                "query": "Rockstar games logo dark background cinematic",
                "text": "Rockstar is investing two billion dollars to make this the most realistic open world in human history.",
                "hl": "realistic",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    {
        "key": "search_oct17_iphone_17_air_ultrathin_redesign",
        "title": "Apple Just Scrapped The Plus Model For The iPhone 17 Air 📱⚡ #shorts #tech #apple",
        "description": (
            "Supply chain blueprints confirm Apple is killing off the Plus lineup in favor of an all-new ultra-thin "
            "iPhone 17 Air measuring just 5 millimeters thick!\n\n"
            "Featuring a titanium-aluminum alloy frame and an all-new internal battery layout, it represents the biggest "
            "design overhaul since the iPhone X.\n\n"
            "Would you trade battery life for an ultra-thin 5mm phone? Tell us in the comments!\n\n"
            "#shorts #apple #iphone17 #tech #smartphone #iphone #technology #gadgets #curiouscodex"
        ),
        "tags": ["shorts", "iphone 17", "apple", "tech news", "smartphone", "iphone 17 air", "gadgets", "future tech"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-17T05:00:00Z",  # 10:30 AM IST
        "scenes": [
            {
                "wiki": "IPhone",
                "commons": "Modern slim smartphone titanium edge display glowing screen",
                "pinterest": "ultra thin futuristic smartphone titanium edge dark sleek concept",
                "query": "ultra thin sleek smartphone titanium edge concept",
                "text": "Apple is officially replacing the iPhone Plus with a five-millimeter ultra-thin model called the iPhone 17 Air!",
                "hl": "thin",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Titanium",
                "commons": "Brushed titanium metal texture industrial material sleek",
                "pinterest": "brushed titanium metal surface sleek tech texture dark",
                "query": "brushed titanium metal texture sleek technology",
                "text": "Built from aerospace-grade titanium, it is engineered to be featherweight without bending in your pocket.",
                "hl": "titanium",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "OLED",
                "commons": "Bezel-less OLED smartphone screen vivid colors display",
                "pinterest": "curved edge OLED smartphone screen glowing futuristic colors",
                "query": "bezel-less OLED smartphone screen glowing colors",
                "text": "It packs an edge-to-edge ProMotion display with under-display Face ID, eliminating the dynamic island cutout.",
                "hl": "display",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Apple_Inc.",
                "commons": "Apple store glowing logo flagship architecture glass",
                "pinterest": "Apple store glowing logo glass cube night architecture",
                "query": "Apple store glowing logo night glass architecture",
                "text": "Analysts predict this razor-thin form factor will trigger the largest smartphone upgrade cycle in five years.",
                "hl": "upgrade",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    {
        "key": "search_oct17_comet_tsuchinshan_atlas_naked_eye",
        "title": "Look Up Tonight: An 80,000-Year-Old Monster Comet Is Passing Earth ☄️🌌 #shorts #space #astronomy",
        "description": (
            "Comet Tsuchinshan-ATLAS is blazing across the western night sky right now, visible to the naked eye!\n\n"
            "This ancient visitor has an orbit of 80,000 years — the last living humans to witness it were Stone Age Neanderthals. "
            "Its brilliant ion tail stretches millions of miles into space.\n\n"
            "Have you spotted the comet in your sky yet? Let us know your city!\n\n"
            "#shorts #comet #space #astronomy #sky #science #nasa #earth #universe #curiouscodex"
        ),
        "tags": ["shorts", "comet", "astronomy", "space", "stargazing", "night sky", "science", "cosmos"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-17T06:30:00Z",  # 12:00 PM IST
        "scenes": [
            {
                "wiki": "C/2023_A3_(Tsuchinshan–ATLAS)",
                "commons": "Comet glowing head and long dust tail dark starry night sky",
                "pinterest": "comet blazing night sky long dust tail stars horizon twilight",
                "query": "comet blazing night sky long dust tail stars twilight",
                "text": "An 80,000-year-old monster comet is blazing across the evening sky right now — visible to the naked eye!",
                "hl": "comet",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Oort_cloud",
                "commons": "Oort cloud deep space solar system boundary icy bodies",
                "pinterest": "Oort cloud icy comets deep space stars nebula glow",
                "query": "Oort cloud icy comets deep space stars nebula",
                "text": "Hailing from the frozen edges of the Oort Cloud, it travels at nearly two hundred thousand miles per hour.",
                "hl": "frozen",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Comet_tail",
                "commons": "Brilliant green and white comet tail stretched across night sky",
                "pinterest": "bright glowing comet tail night sky mountain horizon stars",
                "query": "bright glowing comet tail night sky mountain stars",
                "text": "Its brilliant dust tail stretches for millions of miles, illuminated by the solar wind as it loops around the sun.",
                "hl": "sun",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Stargazing",
                "commons": "People looking through telescope at night sky starry landscape",
                "pinterest": "silhouette person looking at starry night sky telescope comet",
                "query": "person looking at night sky telescope comet stargazing",
                "text": "Look west right after sunset — because once it leaves our solar system, it will never return again.",
                "hl": "sunset",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    # ─── PILLAR 2: SPECIALS OF THAT DAY (OCTOBER 17) (2 SHORTS) ───
    {
        "key": "special_oct17_eradication_poverty_ubi_experiments",
        "title": "What Happened When This City Gave $1,000 Free Cash Every Month? 💵🌍 #shorts #economy #facts",
        "description": (
            "On October 17, the world marks the International Day for the Eradication of Poverty.\n\n"
            "Guaranteed basic income experiments across 30 cities revealed a shocking outcome: "
            "unconditional monthly cash did NOT make people lazy — it doubled entrepreneurship, slashed hospital visits by 40%, "
            "and boosted full-time employment!\n\n"
            "Would you support a universal basic income in your country?\n\n"
            "#shorts #economy #poverty #money #universalbasicincome #facts #society #future #curiouscodex"
        ),
        "tags": ["shorts", "universal basic income", "poverty eradication", "economy", "money", "facts", "social science"],
        "bgm": BGM_LOFI,
        "publish_at": "2026-10-17T08:00:00Z",  # 01:30 PM IST
        "scenes": [
            {
                "wiki": "International_Day_for_the_Eradication_of_Poverty",
                "commons": "Global hands holding together solidarity community unity",
                "pinterest": "diverse hands holding together community unity hope warm light",
                "query": "diverse hands holding together community unity warm light",
                "text": "On World Poverty Eradication Day, economists released the results of a radical five-year cash experiment!",
                "hl": "poverty",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Universal_basic_income",
                "commons": "Stack of money cash currency economic stimulus finance",
                "pinterest": "stack of banknotes money currency finance table economy",
                "query": "stack of currency banknotes finance economy table",
                "text": "Thousands of low-income families were given one thousand dollars every month with zero strings attached.",
                "hl": "money",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Entrepreneurship",
                "commons": "Small business owner smiling shop store startup success",
                "pinterest": "happy small business owner store startup entrepreneur success",
                "query": "small business owner store startup entrepreneur success",
                "text": "Critics predicted people would stop working — but instead, small business startups doubled and hospital visits plummeted.",
                "hl": "startups",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Social_welfare",
                "commons": "Modern thriving city skyline families park prosperity future",
                "pinterest": "modern thriving city park families happiness prosperity future",
                "query": "modern thriving city park families prosperity future",
                "text": "Financial security gave families breathing room to study and find higher-paying careers, proving poverty is a lack of cash, not ambition.",
                "hl": "careers",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    {
        "key": "special_oct17_1973_oil_crisis_shockwave",
        "title": "The Single Morning In 1973 That Crippled The World Economy Overnight ⛽📉 #shorts #history #facts",
        "description": (
            "On October 17, 1973, Arab oil ministers announced a sudden embargo that shocked the entire planet!\n\n"
            "Oil prices quadrupled overnight, gas stations ran completely dry, and governments banned Sunday driving. "
            "This single event created modern fuel efficiency standards and forced the world to invest in renewable energy!\n\n"
            "Did you know how fragile the global energy supply was in 1973?\n\n"
            "#shorts #history #oilcrisis #energy #economy #1973 #geopolitics #facts #inflation #curiouscodex"
        ),
        "tags": ["shorts", "1973 oil crisis", "history facts", "economy", "oil embargo", "gas crisis", "geopolitics"],
        "bgm": BGM_MYSTERY,
        "publish_at": "2026-10-17T10:00:00Z",  # 03:30 PM IST
        "scenes": [
            {
                "wiki": "1973_oil_crisis",
                "commons": "Gas station line cars waiting fuel crisis 1973 vintage photo",
                "pinterest": "cars queued gas station vintage 1973 fuel crisis black white",
                "query": "cars lined up gas station fuel crisis 1973 vintage",
                "text": "On October 17th, 1973, a single announcement brought the entire global economy to a screeching halt!",
                "hl": "halt",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "OPEC",
                "commons": "Oil refinery towers burning flare industrial night petroleum",
                "pinterest": "oil refinery petroleum flare industrial landscape night energy",
                "query": "oil refinery petroleum flare industrial night energy",
                "text": "OPEC nations abruptly halted oil exports, causing the price of crude petroleum to skyrocket by four hundred percent.",
                "hl": "oil",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Fuel_rationing",
                "commons": "No gas sign vintage petrol station empty pumps closed",
                "pinterest": "vintage no gas sign closed pump station retro 1970s",
                "query": "vintage no gas sign closed pump station retro 1970s",
                "text": "Drivers waited in lines three miles long, and nations banned highway driving on Sundays to conserve reserves.",
                "hl": "reserves",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Renewable_energy",
                "commons": "Solar panels and wind turbines green energy modern field",
                "pinterest": "modern wind turbines solar panels green energy field sunset",
                "query": "modern wind turbines solar panels green energy sunset",
                "text": "This catastrophic shock forced humanity to develop compact cars and kickstarted the entire modern renewable energy industry.",
                "hl": "renewable",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    # ─── PILLAR 3: BIG WORLDWIDE MEGA-EVENTS (2 SHORTS) ───
    {
        "key": "world_event_oct17_spacex_mechazilla_chopstick_tower_catch",
        "title": "SpaceX Caught A 250-Ton Steel Skyscraper Mid-Air With Giant Chopsticks 🚀🦾 #shorts #spacex #tech",
        "description": (
            "SpaceX has achieved science fiction: catching the giant 230-foot Super Heavy booster out of mid-air "
            "with mechanical launch tower arms named Mechazilla!\n\n"
            "Returning from orbit at hypersonic speed, the rocket decelerated and floated into the mechanical arms "
            "with sub-inch precision. This unlocks rapid rocket reusability and paves the highway to Mars!\n\n"
            "Will humans land on Mars before 2030? Drop your thoughts below!\n\n"
            "#shorts #spacex #starship #elonmusk #space #engineering #technology #rocket #mars #curiouscodex"
        ),
        "tags": ["shorts", "spacex", "starship", "mechazilla", "booster catch", "elon musk", "engineering", "space tech"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-17T12:00:00Z",  # 05:30 PM IST
        "scenes": [
            {
                "wiki": "Starship_flight_test_5",
                "commons": "SpaceX Starship Super Heavy booster launch tower catch render",
                "pinterest": "SpaceX Starship booster launch tower chopsticks catch night",
                "query": "SpaceX Starship booster launch tower chopsticks catch",
                "text": "SpaceX has achieved pure science fiction — catching a two hundred foot rocket booster directly out of the sky!",
                "hl": "rocket",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Booster_(rocketry)",
                "commons": "Rocket booster descending fiery engines plume landing space",
                "pinterest": "rocket booster fiery retro propulsion landing night sky",
                "query": "rocket booster fiery retro propulsion landing night",
                "text": "Falling back from space at supersonic speed, three Raptor engines ignited to hover the steel giant beside the tower.",
                "hl": "supersonic",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Launch_pad",
                "commons": "Mechazilla chopstick arms launch tower Starbase Texas facility",
                "pinterest": "Mechazilla tower giant mechanical arms Starbase launch pad",
                "query": "Mechazilla tower mechanical arms Starbase launch pad",
                "text": "Giant hydraulic chopstick arms closed in with sub-inch precision, gently cushioning two hundred and fifty tons of steel.",
                "hl": "chopsticks",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Human_mission_to_Mars",
                "commons": "Mars planet red surface colonization human base concept space",
                "pinterest": "Mars base human settlement Starship fleet futuristic space",
                "query": "Mars base settlement Starship fleet futuristic concept",
                "text": "By eliminating landing legs, rockets can now be refueled within hours, turning the voyage to Mars into a daily reality.",
                "hl": "reality",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    {
        "key": "world_event_oct17_compact_fusion_superconducting_magnet_record",
        "title": "Scientists Created A Magnetic Field 100,000x Stronger Than Earth ☀️🧲 #shorts #science #energy",
        "description": (
            "Physicists and engineers have built a high-temperature superconducting magnet capable of a 20-Tesla magnetic field — "
            "over 100,000 times stronger than Earth’s magnetic core!\n\n"
            "This breakthrough allows compact tokamak reactors to bottle 100-million-degree plasma without melting, "
            "accelerating commercial nuclear fusion energy by an entire decade.\n\n"
            "Are you excited for endless, clean, zero-carbon fusion power?\n\n"
            "#shorts #fusion #nuclear #cleanenergy #physics #science #future #tech #innovation #curiouscodex"
        ),
        "tags": ["shorts", "nuclear fusion", "clean energy", "physics", "superconductor", "science news", "future tech"],
        "bgm": BGM_SPACE,
        "publish_at": "2026-10-17T13:30:00Z",  # 07:00 PM IST
        "scenes": [
            {
                "wiki": "Superconducting_magnet",
                "commons": "High temperature superconducting magnet coil laboratory research",
                "pinterest": "superconducting magnet circular coil glowing lab high tech physics",
                "query": "superconducting magnet circular coil glowing lab physics",
                "text": "Engineers have created a magnetic field so intense it can bottle the core of an exploding star right here on Earth!",
                "hl": "star",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "High-temperature_superconductivity",
                "commons": "Superconductor levitation magnet quantum physics laboratory",
                "pinterest": "quantum levitation superconductor magnet cold vapor lab",
                "query": "quantum levitation superconductor magnet cold vapor lab",
                "text": "Using rare-earth barium copper oxide tapes, this magnet reaches twenty Tesla with zero electrical resistance.",
                "hl": "magnet",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Tokamak",
                "commons": "Tokamak fusion reactor interior glowing plasma magnetic torus",
                "pinterest": "Tokamak fusion reactor interior glowing hot plasma magnetic ring",
                "query": "Tokamak fusion reactor glowing hot plasma magnetic ring",
                "text": "It confines plasma heated to one hundred million degrees Celsius, preventing it from touching the reactor walls.",
                "hl": "plasma",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Fusion_power",
                "commons": "Clean green energy grid futuristic city power lines electricity",
                "pinterest": "futuristic clean energy glowing power grid city skyline",
                "query": "clean energy glowing power grid city skyline future",
                "text": "This unlocks compact fusion power plants that can deliver infinite zero-carbon electricity for the entire world.",
                "hl": "infinite",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    # ─── PILLAR 4: INDIAN EVENTS, FESTIVALS & SMART OFFERS (2 SHORTS) ───
    {
        "key": "india_oct17_festive_gold_buying_rules_sgb_tax_hack",
        "title": "Buying Gold This Festival Season? Don't Make This 3% Mistake! 🪙🇮🇳 #shorts #india #finance",
        "description": (
            "During Navratri, Dussehra, and Dhanteras, millions of Indians buy gold — but most lose 15% to 25% "
            "in making charges and GST!\n\n"
            "Here is how smart investors buy gold digitally via Sovereign Gold Bonds (SGB) and digital vaults: "
            "0% making charges, 0% GST, a guaranteed 2.5% annual interest payout, and 100% tax-free capital gains on maturity!\n\n"
            "Will you buy physical gold or digital gold this festive season?\n\n"
            "#shorts #india #gold #dhanteras #diwali #finance #investment #taxhack #savings #curiouscodex"
        ),
        "tags": ["shorts", "gold buying", "india finance", "diwali shopping", "dhanteras", "sgb", "tax hack", "investing"],
        "bgm": BGM_LOFI,
        "publish_at": "2026-10-17T15:00:00Z",  # 08:30 PM IST
        "scenes": [
            {
                "wiki": "Dhanteras",
                "commons": "Indian gold jewelry bangles coins traditional festival market",
                "pinterest": "traditional Indian gold jewelry coins festival Dhanteras sparkle",
                "query": "Indian gold jewelry coins traditional festival Dhanteras",
                "text": "Before you buy gold jewelry this festive season, watch out for the hidden fees that eat your wealth!",
                "hl": "gold",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Goods_and_Services_Tax_(India)",
                "commons": "Jewelry shop counter customer buying gold coins invoice",
                "pinterest": "jewelry shop gold shopping customer buying festive season",
                "query": "jewelry shop gold shopping customer buying festive season",
                "text": "Physical gold jewelry carries up to twenty percent in making charges plus three percent mandatory GST.",
                "hl": "charges",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Sovereign_Gold_Bond",
                "commons": "Reserve Bank of India building Mumbai headquarters official",
                "pinterest": "Reserve Bank of India gold investment certificate financial",
                "query": "Reserve Bank of India gold investment certificate",
                "text": "Instead, Sovereign Gold Bonds issued by the RBI charge zero making fees and pay you two point five percent interest yearly.",
                "hl": "interest",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Capital_gains_tax",
                "commons": "Gold bars wealth security financial investment prosperity",
                "pinterest": "pure gold bars stacked wealth growth investment savings",
                "query": "pure gold bars stacked wealth investment savings",
                "text": "Best of all, all capital gains at maturity are completely exempt from income tax, keeping all profits in your pocket.",
                "hl": "profits",
                "sfx": SFX_DIR / "impact.wav"
            }
        ]
    },

    {
        "key": "india_oct17_irctc_ai_seat_allocation_sweekar_app",
        "title": "Indian Railways Just Launched An AI App To Eliminate Train Waiting Lists 🚆🇮🇳 #shorts #india #tech",
        "description": (
            "Planning to travel home for Diwali and Chhath Puja? Indian Railways is rolling out an AI system "
            "designed to end the nightmare of WL (waiting list) tickets!\n\n"
            "Using predictive analytics, the algorithm scans cancelled berths across intermediate stations in real-time, "
            "re-linking empty segments to confirm tickets for long-distance passengers automatically.\n\n"
            "Did your festive train ticket get confirmed? Tell us your route below!\n\n"
            "#shorts #indianrailways #irctc #train #diwali #travel #tech #india #railway #curiouscodex"
        ),
        "tags": ["shorts", "indian railways", "irctc", "tatkal", "diwali travel", "train waiting list", "tech news", "india"],
        "bgm": BGM_LOFI,
        "publish_at": "2026-10-17T16:30:00Z",  # 10:00 PM IST
        "scenes": [
            {
                "wiki": "Indian_Railways",
                "commons": "Vande Bharat express train running fast Indian railway tracks",
                "pinterest": "Vande Bharat express train high speed modern Indian railways",
                "query": "Vande Bharat express train modern Indian railways",
                "text": "Traveling home for Diwali? Indian Railways is deploying artificial intelligence to solve waiting lists forever!",
                "hl": "railways",
                "sfx": SFX_DIR / "impact.wav"
            },
            {
                "wiki": "Indian_Railway_Catering_and_Tourism_Corporation",
                "commons": "Crowded Indian railway station passengers platform festive travel",
                "pinterest": "crowded Indian railway station train passengers festive travel",
                "query": "crowded Indian railway station train passengers festive travel",
                "text": "During festival rush, millions of passengers get stranded because traditional booking engines reserve seats in static blocks.",
                "hl": "festival",
                "sfx": SFX_DIR / "whoosh_in.wav"
            },
            {
                "wiki": "Predictive_analytics",
                "commons": "Artificial intelligence data network routing algorithm display",
                "pinterest": "AI data routing network algorithm glowing blue lines tech",
                "query": "AI data routing network algorithm glowing blue lines",
                "text": "The new AI engine scans millions of intermediate passenger drops in real-time, stitching vacant segments into confirmed berths.",
                "hl": "berths",
                "sfx": SFX_DIR / "whoosh_out.wav"
            },
            {
                "wiki": "Vande_Bharat",
                "commons": "Happy passenger smiling inside modern train cabin comfortable",
                "pinterest": "happy Indian family smiling inside modern train travel comfort",
                "query": "happy passenger smiling inside modern train cabin travel",
                "text": "Trial runs boosted seat confirmation rates by over thirty percent, making holiday journeys stress-free for countless families.",
                "hl": "families",
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
    print("  OCTOBER 17, 2026 — 9-SHORTS DAILY SCHEDULED SUITE")
    print("=" * 80)

    # Step 1: Render all 9 shorts
    rendered_shorts = []
    for idx, item in enumerate(OCT17_MANIFEST, 1):
        print(f"\n[{idx}/9] Starting render: {item['key']}")
        out_mp4 = render_short(item)
        rendered_shorts.append((item, out_mp4))

    # Step 2: Upload all 9 to YouTube with scheduled publish times
    print("\n" + "=" * 80)
    print("  STARTING YOUTUBE SCHEDULED UPLOADS (OCTOBER 17 SUITE)")
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
            "upload_date": "2026-10-17",
            "publish_at": pub_time,
            "status": "SCHEDULED"
        }
        REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")

    print("\n" + "=" * 80)
    print("  ALL 9 OCTOBER 17 SHORTS RENDERED & SCHEDULED SUCCESSFULLY!")
    print("  You can now close your laptop — YouTube will release them automatically!")
    print("=" * 80)


if __name__ == "__main__":
    main()
