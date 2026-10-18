import urllib.request, os, sys
sys.stdout.reconfigure(encoding='utf-8')

AUDIO_DIR = "assets/devotional/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

TRACKS = [
    {
        "id": "01_suprabhatam",
        "file": "01_suprabhatam.mp3",
        "existing": "assets/devotional/suprabhata_seva_master.mp3"
    },
    {
        "id": "02_govinda_namalu",
        "file": "02_govinda_namalu.mp3",
        "url": "https://archive.org/download/ISongs.info01GovindaNamalu_201811/%5BiSongs.info%5D%2001%20-%20Govinda%20Namalu.mp3"
    },
    {
        "id": "03_vishnu_sahasranamam",
        "file": "03_vishnu_sahasranamam.mp3",
        "url": "https://archive.org/download/VishnuSahasranamam_201507/Vishnu%20Sahasranamam.mp3"
    },
    {
        "id": "04_kanakadhara_lakshmi",
        "file": "04_kanakadhara_lakshmi.mp3",
        "url": "https://archive.org/download/SriKanakadharaStotram_201508/Sri%20Kanakadhara%20Stotram%20-%20Sri%20Kanakadhara%20Stotram.mp3"
    },
    {
        "id": "05_hanuman_chalisa",
        "file": "05_hanuman_chalisa.mp3",
        "url": "https://archive.org/download/ShreeHanumanChalisa_201510/05%20Shree%20Hanuman%20Chalisa.mp3"
    },
    {
        "id": "06_aditya_hrudayam",
        "file": "06_aditya_hrudayam.mp3",
        "url": "https://archive.org/download/adityahrudayam_201912/02.%20Aditya%20Hrudayam.mp3"
    },
    {
        "id": "07_mangala_harathi",
        "file": "07_mangala_harathi.mp3",
        "url": "https://archive.org/download/ANNAMACHARYA_504/AdivoAlladivo006Rgsr.mp3"
    }
]

def download_tracks():
    for t in TRACKS:
        dst = os.path.join(AUDIO_DIR, t["file"])
        if "existing" in t and os.path.exists(t["existing"]):
            if not os.path.exists(dst):
                import shutil
                shutil.copy2(t["existing"], dst)
            print(f"✅ {t['id']}: Using existing track ({os.path.getsize(dst):,} bytes)")
            continue
        if os.path.exists(dst) and os.path.getsize(dst) > 100000:
            print(f"✅ {t['id']}: Already downloaded ({os.path.getsize(dst):,} bytes)")
            continue
        print(f"Downloading {t['id']} from archive.org...")
        req = urllib.request.Request(t["url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp, open(dst, "wb") as out:
            out.write(resp.read())
        print(f"  ✅ Saved {dst} ({os.path.getsize(dst):,} bytes)")

if __name__ == "__main__":
    download_tracks()
