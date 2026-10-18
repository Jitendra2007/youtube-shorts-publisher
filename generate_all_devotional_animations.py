import asyncio, os, shutil
from playwright.async_api import async_playwright

SEGMENTS = [
    {
        "id": "01_suprabhatam",
        "bg_image": "assets/devotional/01_suprabhatam_balaji.jpg",
        "title": "శ్రీ వేంకటేశ్వర సుప్రభాతం",
        "subtitle": "కౌసల్యా సుప్రజా రామ పూర్వా సంధ్యా ప్రవర్తతే • ఉత్తిష్ఠ నరశార్దూల కర్తవ్యం దైవమాహ్నికమ్",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • ప్రాతఃకాల సుప్రభాత సేవ",
        "ticker": "|| కౌసల్యా సుప్రజా రామ పూర్వా సంధ్యా ప్రవర్తతే • ఉత్తిష్ఠ నరశార్దూల కర్తవ్యం దైవమాహ్నికమ్ • ఓం నమో వేంకటేశాయ • సర్వే జనాః సుఖినో భవన్తు ||",
        "effect": "rose_petals_gold_dust",
        "output": "assets/devotional/anim_01_suprabhatam.mp4"
    },
    {
        "id": "02_govinda_namalu",
        "bg_image": "assets/devotional/02_govinda_namalu.jpg",
        "title": "శ్రీ గోవింద నామాలు",
        "subtitle": "గోవిందా హరి గోవిందా • వేంకటరమణ గోవిందా • సంకటహరణ గోవిందా • శ్రీనివాస గోవిందా",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • శ్రీ తిరుమల గోవింద నామావళి",
        "ticker": "|| గోవిందా హరి గోవిందా • వేంకటరమణ గోవిందా • సంకటహరణ గోవిందా • శ్రీనివాస గోవిందా • తిరుమల వాస గోవిందా • భక్తవత్సల గోవిందా ||",
        "effect": "tulasi_gold_sparkles",
        "output": "assets/devotional/anim_02_govinda_namalu.mp4"
    },
    {
        "id": "03_vishnu_sahasranamam",
        "bg_image": "assets/devotional/03_vishnu_sahasranamam.jpg",
        "title": "శ్రీ విష్ణు సహస్రనామ స్తోత్రం",
        "subtitle": "శుక్లాంబరధరం విష్ణుం శశివర్ణం చతుర్భుజమ్ • ప్రసన్నవదనం ధ్యాయేత్ సర్వవిఘ్నోపశాంతయే",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • శ్రీ విష్ణు సహస్రనామ పారాయణం",
        "ticker": "|| ఓం నమో భగవతే వాసుదేవాయ • శాంతాకారం భుజగశయనం పద్మనాభం సురేశమ్ • విశ్వాకారం గగనసదృశం మేఘవర్ణం శుభాంగమ్ ||",
        "effect": "cosmic_stars_lotus",
        "output": "assets/devotional/anim_03_vishnu_sahasranamam.mp4"
    },
    {
        "id": "04_kanakadhara_lakshmi",
        "bg_image": "assets/devotional/04_kanakadhara_lakshmi.jpg",
        "title": "శ్రీ కనకధారా స్తోత్రం & అష్టలక్ష్మి స్తోత్రం",
        "subtitle": "అంగం హరేః పులకభూషణమాశ్రయంతీ • భృంగాంగనేవ ముకులాభరణం తమాలమ్",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • శ్రీ మహాలక్ష్మి అష్టైశ్వర్య పూజ",
        "ticker": "|| ఓం శ్రీం హ్రీం క్లీం మహాలక్ష్మ్యై నమః • నమస్తేస్తు మహామాయే శ్రీపీఠే సురపూజితే • శంఖచక్రగదాహస్తే మహాలక్ష్మి నమోస్తు తే ||",
        "effect": "gold_coin_shower_lotus",
        "output": "assets/devotional/anim_04_kanakadhara_lakshmi.mp4"
    },
    {
        "id": "05_hanuman_chalisa",
        "bg_image": "assets/devotional/05_hanuman_chalisa.jpg",
        "title": "శ్రీ హనుమాన్ చాలీసా & ఆంజనేయ దండకం",
        "subtitle": "జయ హనుమాన జ్ఞాన గున సాగర • జయ కపీస తిహుఁ లోక ఉజాగర • రామదూత అతులిత బలధామా",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • సంకటమోచన హనుమాన్ ఉపాసన",
        "ticker": "|| మనోజవం మారుతతుల్యవేగం జితేంద్రియం బుద్ధిమతాం వరిష్ఠమ్ • వాతాత్మజం వానరయూథముఖ్యం శ్రీరామదూతం శరణం ప్రపద్యే • జై శ్రీరామ్ ||",
        "effect": "saffron_embers_flags",
        "output": "assets/devotional/anim_05_hanuman_chalisa.mp4"
    },
    {
        "id": "06_aditya_hrudayam",
        "bg_image": "assets/devotional/06_aditya_hrudayam.jpg",
        "title": "ఆదిత్య హృదయ స్తోత్రం & గాయత్రీ మంత్రం",
        "subtitle": "ఓం భూర్భువః స్వః తత్సవితుర్వరేణ్యం భర్గో దేవస్య ధీమహి • ధియో యో నః ప్రచోదయాత్",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • ప్రత్యక్ష దైవం సూర్య నమస్కారాలు",
        "ticker": "|| ఆదిత్యాయ విద్మహే సహస్రకిరణాయ ధీమహి తన్నో సూర్యః ప్రచోదయాత్ • నమః సూర్యాయ శాంతాయ సర్వరోగ నివారిణే • ఓం సూర్యాయ నమః ||",
        "effect": "sunbeams_gold_dust",
        "output": "assets/devotional/anim_06_aditya_hrudayam.mp4"
    },
    {
        "id": "07_mangala_harathi",
        "bg_image": "assets/devotional/07_mangala_harathi.jpg",
        "title": "తిరుమల శ్రీవారి దివ్య మంగళ హారతి",
        "subtitle": "శ్రియః కాంతాయ కళ్యాణనిధయే నిధయేఽర్థినామ్ • శ్రీవేంకటనివాసాయ శ్రీనివాసాయ మంగళమ్",
        "badge": "🔴 ప్రత్యక్ష ప్రసారం • దివ్య కర్పూర నీరాజనం & మంగళ హారతి",
        "ticker": "|| బ్రహ్మకడిగిన పాదము • క్షీరాబ్ది కన్యకకు శ్రీ మహాలక్ష్మికిని నీరజాలయకును నీరాజనము • తిరుమల శ్రీ వేంకటేశ్వర స్వామివారి దివ్య మంగళ హారతి ||",
        "effect": "camphor_flames_jasmine",
        "output": "assets/devotional/anim_07_mangala_harathi.mp4"
    }
]

def build_html(seg):
    bg_abs = os.path.abspath(seg["bg_image"]).replace("\\", "/")
    effect = seg["effect"]
    
    js_particle_code = ""
    if effect == "gold_coin_shower_lotus":
        js_particle_code = """
        const coins = [];
        for(let i=0; i<45; i++){
          coins.push({
            x: Math.random()*1920, y: Math.random()*1080,
            r: Math.random()*10 + 6,
            vy: Math.random()*3 + 2,
            vx: (Math.random()-0.5)*1.2,
            rot: Math.random()*Math.PI*2,
            vrot: (Math.random()-0.5)*0.1,
            scaleY: Math.random()*0.8 + 0.2
          });
        }
        function draw(){
          ctx.clearRect(0,0,1920,1080);
          for(let c of coins){
            ctx.save();
            ctx.translate(c.x, c.y);
            ctx.rotate(c.rot);
            ctx.scale(1, c.scaleY);
            let grad = ctx.createRadialGradient(0,0,1, 0,0,c.r);
            grad.addColorStop(0, '#fff4b8');
            grad.addColorStop(0.5, '#ffd700');
            grad.addColorStop(1, '#b8860b');
            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(0, 0, c.r, 0, Math.PI*2);
            ctx.fill();
            ctx.strokeStyle = '#fff8dc';
            ctx.lineWidth = 1.5;
            ctx.stroke();
            ctx.restore();
            c.y += c.vy; c.x += c.vx; c.rot += c.vrot;
            if(c.y > 1080) { c.y = -20; c.x = Math.random()*1920; }
          }
          requestAnimationFrame(draw);
        }
        draw();
        """
    elif effect == "saffron_embers_flags":
        js_particle_code = """
        const embers = [];
        for(let i=0; i<70; i++){
          embers.push({
            x: Math.random()*1920, y: Math.random()*1080,
            r: Math.random()*5 + 1.5,
            vy: -Math.random()*3 - 1,
            vx: (Math.random()-0.5)*2,
            alpha: Math.random()*0.8 + 0.2,
            hue: Math.random()>0.5 ? '#ff4500' : '#ffa500'
          });
        }
        function draw(){
          ctx.clearRect(0,0,1920,1080);
          for(let e of embers){
            ctx.fillStyle = e.hue;
            ctx.shadowColor = '#ff2200';
            ctx.shadowBlur = 14;
            ctx.beginPath();
            ctx.arc(e.x, e.y, e.r, 0, Math.PI*2);
            ctx.fill();
            e.y += e.vy; e.x += e.vx;
            if(e.y < -10) { e.y = 1090; e.x = Math.random()*1920; }
          }
          requestAnimationFrame(draw);
        }
        draw();
        """
    elif effect == "camphor_flames_jasmine":
        js_particle_code = """
        const jasmines = [];
        for(let i=0; i<50; i++){
          jasmines.push({
            x: Math.random()*1920, y: Math.random()*1080,
            r: Math.random()*6 + 3,
            vy: Math.random()*2 + 1,
            vx: Math.sin(i)*1.5,
            rot: Math.random()*Math.PI*2
          });
        }
        function draw(){
          ctx.clearRect(0,0,1920,1080);
          for(let j of jasmines){
            ctx.save();
            ctx.translate(j.x, j.y);
            ctx.rotate(j.rot);
            ctx.fillStyle = 'rgba(255, 255, 240, 0.9)';
            ctx.shadowColor = '#fff';
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.ellipse(0, 0, j.r*1.5, j.r, 0, 0, Math.PI*2);
            ctx.fill();
            ctx.restore();
            j.y += j.vy; j.x += j.vx*0.5; j.rot += 0.03;
            if(j.y > 1080) { j.y = -20; j.x = Math.random()*1920; }
          }
          requestAnimationFrame(draw);
        }
        draw();
        """
    else: # Default golden dust & sacred petals
        js_particle_code = """
        const particles = [];
        for(let i=0; i<65; i++){
          particles.push({
            x: Math.random()*1920, y: Math.random()*1080,
            r: Math.random()*4 + 1.5,
            vx: (Math.random()-0.5)*1.5, vy: -Math.random()*2 - 0.5,
            alpha: Math.random()*0.8 + 0.2
          });
        }
        function draw(){
          ctx.clearRect(0,0,1920,1080);
          for(let p of particles){
            ctx.fillStyle = 'rgba(255, 215, 0, ' + p.alpha + ')';
            ctx.shadowColor = '#ffcc00';
            ctx.shadowBlur = 12;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
            ctx.fill();
            p.x += p.vx; p.y += p.vy;
            if(p.y < 0) { p.y = 1080; p.x = Math.random()*1920; }
          }
          requestAnimationFrame(draw);
        }
        draw();
        """

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Mandali&family=Noto+Sans+Telugu:wght@600;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden; background: #000;
    font-family: 'Noto Sans Telugu', sans-serif; position: relative;
  }}
  .bg {{
    position: absolute; width: 100%; height: 100%;
    background-image: url('{bg_abs}');
    background-size: cover; background-position: center;
    animation: slowZoom 8s infinite alternate ease-in-out;
  }}
  @keyframes slowZoom {{
    0% {{ transform: scale(1.0); }}
    100% {{ transform: scale(1.06); }}
  }}
  canvas {{ position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; pointer-events: none; }}
  .header {{
    position: absolute; top: 30px; left: 50%; transform: translateX(-50%);
    background: rgba(20, 5, 2, 0.88); border: 2px solid #ffd700; border-radius: 50px;
    padding: 12px 40px; display: flex; align-items: center; gap: 20px;
    box-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
  }}
  .live-dot {{ width: 16px; height: 16px; background: #ff0000; border-radius: 50%; box-shadow: 0 0 15px #ff0000; animation: blink 1s infinite alternate; }}
  @keyframes blink {{ 0% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
  .header-text {{ color: #fff; font-size: 24px; font-weight: 800; }}
  .title-box {{
    position: absolute; bottom: 100px; left: 50%; transform: translateX(-50%);
    background: linear-gradient(180deg, rgba(30, 10, 5, 0.94) 0%, rgba(10, 2, 2, 0.97) 100%);
    border: 3px solid #ffcc00; border-radius: 24px; padding: 18px 50px; text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.85), 0 0 25px rgba(255, 204, 0, 0.4);
    min-width: 950px; max-width: 1500px;
  }}
  .main-title {{ font-size: 46px; font-weight: 900; color: #ffd700; text-shadow: 0 0 20px rgba(255, 215, 0, 0.8); }}
  .subtitle {{ font-size: 25px; color: #fff8e7; margin-top: 6px; line-height: 1.4; }}
  .ticker-wrap {{
    position: absolute; bottom: 0; left: 0; width: 100%; height: 60px;
    background: linear-gradient(90deg, #4a0e0e 0%, #1a0505 50%, #4a0e0e 100%);
    border-top: 2px solid #ffd700; overflow: hidden; display: flex; align-items: center;
  }}
  .ticker {{
    display: inline-block; white-space: nowrap; color: #ffd700; font-size: 24px; font-weight: 800;
    animation: marquee 16s linear infinite;
  }}
  @keyframes marquee {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
</style>
</head>
<body>
  <div class='bg'></div>
  <canvas id='c' width='1920' height='1080'></canvas>
  <div class='header'>
    <div class='live-dot'></div>
    <div class='header-text'>{seg['badge']}</div>
  </div>
  <div class='title-box'>
    <div class='main-title'>{seg['title']}</div>
    <div class='subtitle'>{seg['subtitle']}</div>
  </div>
  <div class='ticker-wrap'>
    <div class='ticker'>{seg['ticker']}</div>
  </div>
  <script>
    const canvas = document.getElementById('c');
    const ctx = canvas.getContext('2d');
    {js_particle_code}
  </script>
</body>
</html>"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

async def generate_all():
    rec_base = "temp_anim_build"
    os.makedirs(rec_base, exist_ok=True)
    os.makedirs("assets/devotional", exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for i, seg in enumerate(SEGMENTS):
            print(f"[{i+1}/7] Generating animated video loop for: {seg['id']}...")
            rec_dir = os.path.join(rec_base, seg["id"])
            if os.path.exists(rec_dir):
                shutil.rmtree(rec_dir)
            os.makedirs(rec_dir, exist_ok=True)
            
            html_content = build_html(seg)
            html_path = os.path.join(rec_base, f"{seg['id']}.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            ctx = await browser.new_context(
                record_video_dir=rec_dir,
                record_video_size={"width": 1920, "height": 1080},
                viewport={"width": 1920, "height": 1080}
            )
            page = await ctx.new_page()
            await page.goto(f"file:///{os.path.abspath(html_path)}")
            # Record 8.5 seconds for a perfect seamless GIF-style loop
            await page.wait_for_timeout(8500)
            await ctx.close()
            
            webm_files = [f for f in os.listdir(rec_dir) if f.endswith(".webm")]
            if webm_files:
                src_webm = os.path.join(rec_dir, webm_files[0])
                dst_mp4 = seg["output"]
                cmd = f'ffmpeg -y -i "{src_webm}" -c:v libx264 -preset fast -crf 21 -pix_fmt yuv420p "{dst_mp4}"'
                res = os.system(cmd)
                if res == 0 and os.path.exists(dst_mp4):
                    print(f"  ✅ Finished {dst_mp4} -> Size: {os.path.getsize(dst_mp4):,} bytes")
                else:
                    print(f"  ❌ FFmpeg transcode failed for {seg['id']}")
            else:
                print(f"  ❌ No webm recorded for {seg['id']}")
                
        await browser.close()
    
    # Cleanup temp build html and webm
    if os.path.exists(rec_base):
        shutil.rmtree(rec_base)
    print("\n🎉 ALL 7 DEVOTIONAL ANIMATION LOOPS GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    asyncio.run(generate_all())
