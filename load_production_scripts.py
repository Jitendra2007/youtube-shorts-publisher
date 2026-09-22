"""
PARSER & LOADER FOR 31-DAY MASTER PRODUCTION SCRIPTS (scritps.txt)
==================================================================
Extracts all 15-slot daily production scripts with vocal styles, HUD formulas,
SFX cues, BGM vibes, and seamless loop triggers.
"""

import os
import re
import json

SCRIPTS_FILE = os.path.join(os.path.dirname(__file__), "information", "scritps.txt")
if not os.path.exists(SCRIPTS_FILE):
    # Fallback to local repo information path
    SCRIPTS_FILE = os.path.join(r"C:\Users\tsapa\Desktop\CODEX\youtube_shorts_publisher_deploy\information\scritps.txt")

def parse_all_production_scripts(filepath: str = SCRIPTS_FILE) -> list:
    """Parses all production scripts from scritps.txt into structured dictionaries."""
    if not os.path.exists(filepath):
        print(f"⚠️ File not found: {filepath}")
        return []

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Split by "Script " headers
    # E.g. "Script 1.01 — Dark Psychology: The Pratfall Effect"
    script_pattern = re.compile(r"Script\s+(\d+)\.(\d+)\s+[—\-]\s+([^:\n]+)[:\n]([^\n]+)?", re.IGNORECASE)
    
    # Extract blocks
    raw_blocks = re.split(r"(?=Script\s+\d+\.\d+\s+[—\-])", content)
    
    parsed_scripts = []
    for block in raw_blocks:
        match = script_pattern.search(block)
        if not match:
            continue
            
        day_num = int(match.group(1))
        slot_num = int(match.group(2))
        category = match.group(3).strip()
        title_suffix = match.group(4).strip() if match.group(4) else category
        title = f"Day {day_num} Slot {slot_num:02d}: {category} — {title_suffix}"

        # Extract Voice Style
        voice_style = "mysterious"
        voice_m = re.search(r"Voice Style:\s*([^\n]+)", block, re.IGNORECASE)
        if voice_m:
            voice_style = voice_m.group(1).strip()

        # Extract BGM
        bgm_vibe = "psychology_mystery"
        bgm_m = re.search(r"BGM:\s*([^\n]+)", block, re.IGNORECASE)
        if bgm_m:
            bgm_text = bgm_m.group(1).lower()
            if "space" in bgm_text or "tech" in bgm_text:
                bgm_vibe = "space_tech"
            elif "lo-fi" in bgm_text or "nature" in bgm_text or "piano" in bgm_text:
                bgm_vibe = "nature_history_lofi"
            else:
                bgm_vibe = "psychology_mystery"

        # Extract Formula HUD if present
        formula = ""
        formula_m = re.search(r"Formula HUD(?:\s*\(Top-Third\))?:\s*([^\n]+)", block, re.IGNORECASE)
        if formula_m:
            formula = formula_m.group(1).strip()
            # Clean up latex / messy formatting
            formula = re.sub(r"[\\_^{}]", "", formula).strip()

        # Extract narration text (remove SFX brackets like [SFX: ...], voice style lines, etc.)
        lines = block.split("\n")
        narration_lines = []
        capture = False
        for l in lines:
            line_str = l.strip()
            # Skip metadata headers
            if line_str.startswith("Script ") or line_str.startswith("Voice Style:") or line_str.startswith("BGM:") or line_str.startswith("Target Duration:") or line_str.startswith("Formula HUD"):
                continue
            if line_str.startswith("*[Seamless Loop"):
                break
            
            # Clean SFX tags: [SFX: ...]
            clean_l = re.sub(r"\[SFX:[^\]]+\]", "", line_str).strip()
            # Strip quotes around spoken dialogue
            clean_l = clean_l.strip('"').strip("'")
            if clean_l and not clean_l.startswith("chevron_right"):
                narration_lines.append(clean_l)

        narration = " ".join(narration_lines).strip()
        # Ensure proper punctuation spacing
        narration = re.sub(r"\s+", " ", narration)

        # Scenery Category mapping
        scenery_cat = "dark_moody"
        cat_lower = category.lower()
        if "ocean" in cat_lower or "nature" in cat_lower:
            scenery_cat = "nature"
        elif "space" in cat_lower or "cosmic" in cat_lower:
            scenery_cat = "space"
        elif "math" in cat_lower or "physics" in cat_lower:
            scenery_cat = "abstract"
        elif "ancient" in cat_lower or "history" in cat_lower:
            scenery_cat = "fantasy"
        elif "tech" in cat_lower or "matrix" in cat_lower:
            scenery_cat = "space"

        parsed_scripts.append({
            "day": day_num,
            "slot": slot_num,
            "id": f"day{day_num:02d}_slot{slot_num:02d}_{category.lower().replace(' ', '_')[:20]}",
            "category": scenery_cat,
            "category_name": category,
            "title": title,
            "youtube_title": f"{title_suffix} 🧠 #shorts #{category.replace(' ', '').lower()} #curiosity #facts",
            "tags": ["shorts", "curiosity", "facts", "science", "mindblowing", category.lower().replace(" ", "")],
            "formula": formula,
            "equation_name": category if formula else "",
            "motion_style": "beat_pulse" if slot_num % 2 == 0 else "ken_burns",
            "bgm_vibe": bgm_vibe,
            "voice_style": voice_style,
            "narration": narration
        })

    return parsed_scripts

def get_scripts_for_day(day: int, filepath: str = SCRIPTS_FILE) -> list:
    """Returns all scripts for a specific day (1-31)."""
    all_s = parse_all_production_scripts(filepath)
    return [s for s in all_s if s["day"] == day]

if __name__ == "__main__":
    scripts = parse_all_production_scripts()
    print("=" * 80)
    print(f"  MASTER PRODUCTION SCRIPTS PARSER: Loaded {len(scripts)} High-Retention Scripts")
    print("=" * 80)
    for s in scripts[:15]:
        print(f"  [Day {s['day']:02d} | Slot {s['slot']:02d}] {s['title']:<55} | Words: {len(s['narration'].split()):>3}w | Vibe: {s['bgm_vibe']}")
    print("=" * 80)
