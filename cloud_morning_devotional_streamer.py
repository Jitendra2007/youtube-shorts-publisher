import os, sys, time, json, subprocess, datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

sys.stdout.reconfigure(encoding='utf-8')

FALLBACK_STREAM_KEY = "fgvv-kfv1-jtbx-gmdd-9jy3"
RTMP_INGEST_URL = "rtmp://a.rtmp.youtube.com/live2"

DEVOTIONAL_PLAYLIST = [
    {
        "id": "01_suprabhatam",
        "name": "శ్రీ వేంకటేశ్వర సుప్రభాతం (Sri Venkateswara Suprabhatam)",
        "video": "assets/devotional/anim_01_suprabhatam.mp4",
        "audio": "assets/devotional/audio/01_suprabhatam.mp3"
    },
    {
        "id": "02_govinda_namalu",
        "name": "శ్రీ గోవింద నామాలు (Govinda Namalu - 108 Divine Chants)",
        "video": "assets/devotional/anim_02_govinda_namalu.mp4",
        "audio": "assets/devotional/audio/02_govinda_namalu.mp3"
    },
    {
        "id": "03_vishnu_sahasranamam",
        "name": "శ్రీ విష్ణు సహస్రనామ స్తోత్రం (Sri Vishnu Sahasranama Stotram)",
        "video": "assets/devotional/anim_03_vishnu_sahasranamam.mp4",
        "audio": "assets/devotional/audio/03_vishnu_sahasranamam.mp3"
    },
    {
        "id": "04_kanakadhara_lakshmi",
        "name": "శ్రీ కనకధారా & అష్టలక్ష్మి స్తోత్రాలు (Kanakadhara & Ashtalakshmi Stotram)",
        "video": "assets/devotional/anim_04_kanakadhara_lakshmi.mp4",
        "audio": "assets/devotional/audio/04_kanakadhara_lakshmi.mp3"
    },
    {
        "id": "05_hanuman_chalisa",
        "name": "శ్రీ హనుమాన్ చాలీసా & ఆంజనేయ దండకం (Hanuman Chalisa & Dandakam)",
        "video": "assets/devotional/anim_05_hanuman_chalisa.mp4",
        "audio": "assets/devotional/audio/05_hanuman_chalisa.mp3"
    },
    {
        "id": "06_aditya_hrudayam",
        "name": "ఆదిత్య హృదయ స్తోత్రం & గాయత్రీ మంత్రం (Aditya Hrudayam & Gayatri Mantra)",
        "video": "assets/devotional/anim_06_aditya_hrudayam.mp4",
        "audio": "assets/devotional/audio/06_aditya_hrudayam.mp3"
    },
    {
        "id": "07_mangala_harathi",
        "name": "తిరుమల శ్రీవారి దివ్య మంగళ హారతి (Tirumala Mangala Harathi & Keerthanas)",
        "video": "assets/devotional/anim_07_mangala_harathi.mp4",
        "audio": "assets/devotional/audio/07_mangala_harathi.mp3"
    }
]

def get_authenticated_service():
    if not os.path.exists("token.json"):
        print("❌ token.json not found!")
        return None
    with open("token.json", "r") as f:
        token_data = json.load(f)
    creds = Credentials.from_authorized_user_info(token_data)
    return build("youtube", "v3", credentials=creds)

def ensure_broadcast_active(youtube):
    now_ist = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    date_str = now_ist.strftime("%d %B %Y")
    
    title = f"🔴 శ్రీ వేంకటేశ్వర సుప్రభాతం | Sri Venkateswara Suprabhatam & Morning Bhakti Live | {date_str}"
    description = f"""శ్రీ వేంకటేశ్వర స్వామివారి దివ్య ప్రాతఃకాల పూజ & సుప్రభాత సేవ ప్రత్యక్ష ప్రసారం 🪔

☀️ Daily Morning Devotional Live (5:00 AM - 8:30 AM IST)
సకల శుభములు కలిగించే తిరుమల వేంకటేశ్వర సుప్రభాతం, గోవింద నామాలు, శ్రీ విష్ణు సహస్రనామ స్తోత్రం, కనకధారా స్తోత్రం, హనుమాన్ చాలీసా, ఆదిత్య హృదయం, మరియు మంగళ హారతి.

🙏 DAILY MORNING LINEUP (సమయాలు):
05:00 AM - శ్రీ వేంకటేశ్వర సుప్రభాతం (Sri Venkateswara Suprabhata Seva)
05:25 AM - శ్రీ గోవింద నామాలు (Govinda Namalu - 108 Divine Chants)
05:45 AM - శ్రీ విష్ణు సహస్రనామ స్తోత్రం (Sri Vishnu Sahasranamam 1,000 Holy Names)
06:25 AM - శ్రీ కనకధారా & అష్టలక్ష్మి స్తోత్రం (Kanakadhara & Ashtalakshmi Stotram)
06:55 AM - శ్రీ హనుమాన్ చాలీసా & ఆంజనేయ దండకం (Hanuman Chalisa & Dandakam)
07:25 AM - ఆదిత్య హృదయ స్తోత్రం & గాయత్రీ మంత్రం (Aditya Hrudayam & Gayatri Mantra)
08:00 AM - తిరుమల శ్రీవారి దివ్య మంగళ హారతి & అన్నమయ్య సంకీర్తనలు (Mangala Harathi)

సర్వే జనాః సుఖినో భవన్తు • ఓం నమో వేంకటేశాయ!

#Suprabhatam #VenkateswaraSuprabhatam #GovindaNamalu #VishnuSahasranamam #KanakadharaStotram #HanumanChalisa #AdityaHrudayam #TeluguBhakti #TirumalaLive #MorningPrayers"""

    try:
        # Check active live streams
        streams_res = youtube.liveStreams().list(part="id,snippet,cdn", mine=True).execute()
        stream_key = FALLBACK_STREAM_KEY
        if streams_res.get("items"):
            stream_key = streams_res["items"][0]["cdn"]["ingestionInfo"]["streamName"]
            print(f"📡 Found Channel Stream Key from YouTube API: {stream_key[:8]}****")
        else:
            print(f"📡 Using Dedicated Channel Stream Key: {stream_key[:8]}****")

        # Check existing live broadcasts
        broadcasts_res = youtube.liveBroadcasts().list(part="id,snippet,status", broadcastStatus="upcoming", maxResults=5).execute()
        broadcast_id = None
        for b in broadcasts_res.get("items", []):
            if "సుప్రభాతం" in b["snippet"]["title"] or "Suprabhatam" in b["snippet"]["title"]:
                broadcast_id = b["id"]
                print(f"✅ Found existing upcoming broadcast: {broadcast_id} ({b['snippet']['title']})")
                break
                
        if not broadcast_id:
            # Create a fresh broadcast for today
            print(f"Creating new scheduled YouTube Live Broadcast for {date_str}...")
            start_time = datetime.datetime.utcnow().isoformat() + "Z"
            end_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=3, minutes=35)).isoformat() + "Z"
            
            new_b = youtube.liveBroadcasts().insert(
                part="snippet,status,contentDetails",
                body={
                    "snippet": {
                        "title": title,
                        "description": description,
                        "scheduledStartTime": start_time,
                        "scheduledEndTime": end_time
                    },
                    "status": {
                        "privacyStatus": "public",
                        "selfDeclaredMadeForKids": False
                    },
                    "contentDetails": {
                        "enableAutoStart": True,
                        "enableAutoStop": True,
                        "recordFromStart": True
                    }
                }
            ).execute()
            broadcast_id = new_b["id"]
            print(f"🎉 Created Broadcast: {broadcast_id}")
            
            # Bind broadcast to stream
            if streams_res.get("items"):
                sid = streams_res["items"][0]["id"]
                youtube.liveBroadcasts().bind(id=broadcast_id, part="id,contentDetails", streamId=sid).execute()
                print(f"🔗 Bound Broadcast {broadcast_id} to Stream {sid}")

        return broadcast_id, stream_key
    except Exception as e:
        print(f"⚠️ YouTube API check notice: {e}. Falling back to direct RTMP streaming.")
        return None, FALLBACK_STREAM_KEY

def build_muxed_segments(staging_dir="temp_stream_staging"):
    os.makedirs(staging_dir, exist_ok=True)
    generated_segments = []
    
    print("\n📦 Pre-muxing 7 devotional segments for seamless concat streaming...")
    for seg in DEVOTIONAL_PLAYLIST:
        out_mp4 = os.path.join(staging_dir, f"{seg['id']}.mp4")
        if not os.path.exists(out_mp4) or os.path.getsize(out_mp4) < 1000000:
            print(f"  Muxing {seg['id']} ({seg['name']})...")
            cmd = [
                "ffmpeg", "-y",
                "-stream_loop", "-1", "-i", seg["video"],
                "-i", seg["audio"],
                "-shortest",
                "-c:v", "copy",
                "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
                out_mp4
            ]
            subprocess.check_call(cmd)
            print(f"  ✅ Finished {seg['id']} -> {os.path.getsize(out_mp4):,} bytes")
        else:
            print(f"  ✅ Cached {seg['id']} -> {os.path.getsize(out_mp4):,} bytes")
        generated_segments.append(out_mp4)
        
    return generated_segments

def generate_concat_manifest(segments, staging_dir="temp_stream_staging", cycles=2):
    manifest_path = os.path.join(staging_dir, "master_playlist.txt")
    with open(manifest_path, "w", encoding="utf-8") as f:
        for c in range(cycles):
            for s in segments:
                clean_path = os.path.abspath(s).replace("\\", "/")
                f.write(f"file '{clean_path}'\n")
    print(f"\n📋 Master playlist generated with {len(segments) * cycles} segments ({cycles} full devotional cycles)!")
    return manifest_path

def start_rtmp_stream(manifest_path, stream_key, max_minutes=215):
    rtmp_url = f"{RTMP_INGEST_URL}/{stream_key}"
    print(f"\n🚀 STARTING LIVE RTMP BROADCAST STREAM TO YOUTUBE...")
    print(f"📡 Target Ingest: {RTMP_INGEST_URL}/[PROTECTED_KEY]")
    print(f"⏰ Maximum Broadcast Duration: {max_minutes} minutes (05:00 AM - 08:35 AM IST)")
    
    # FFmpeg command streaming with real-time flag and zero re-encoding
    cmd = [
        "ffmpeg", "-re",
        "-f", "concat", "-safe", "0", "-i", manifest_path,
        "-t", str(max_minutes * 60),
        "-c", "copy",
        "-flvflags", "no_duration_filesize",
        "-f", "flv", rtmp_url
    ]
    
    print("Executing streaming command...")
    proc = subprocess.Popen(cmd)
    try:
        proc.wait()
        print("\n✅ Stream completed successfully according to schedule!")
    except KeyboardInterrupt:
        print("\n⚠️ Streaming interrupted by user. Stopping FFmpeg...")
        proc.terminate()
        proc.wait()

def main():
    print("="*75)
    print("🕉️  TIRUMALA MORNING DEVOTIONAL 24/7 CLOUD STREAMING ENGINE")
    print("   Starting Schedule: 05:00 AM - 08:30 AM IST Daily")
    print("="*75)
    
    youtube = get_authenticated_service()
    broadcast_id, stream_key = None, FALLBACK_STREAM_KEY
    if youtube:
        broadcast_id, stream_key = ensure_broadcast_active(youtube)
    else:
        print(f"Using Direct Stream Key: {stream_key[:8]}****")
        
    segments = build_muxed_segments()
    manifest = generate_concat_manifest(segments, cycles=2)
    start_rtmp_stream(manifest, stream_key, max_minutes=215)

if __name__ == "__main__":
    main()
