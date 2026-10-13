"""Build a public web handout using the project-local reference layout."""
from pathlib import Path
import html
import re
import struct

ROOT = Path(__file__).resolve().parent
IMAGE_BASE = 'https://raw.githubusercontent.com/max00189xp/3d-printing-hardware-tutorial/main/output/handout/'
PREVIEW_BASE = 'https://max00189xp.github.io/3d-printing-hardware-tutorial/output/handout/images/web/'
css = (ROOT / 'web-layout.css').read_text(encoding='utf-8-sig')
source = (ROOT / 'output/handout/3D列印機器原理講義.md').read_text(encoding='utf-8-sig')

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\*\*\s*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    return text

def blocks(text):
    lines = text.strip().splitlines()
    output = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line == '[TOC]':
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in row):
                    rows.append(row)
                i += 1
            output.append('<div class="np-table-wrap" tabindex="0" role="region" aria-label="可左右捲動的對照表"><table class="np-table"><thead><tr>' + ''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0]) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in rows[1:]) + '</tbody></table></div>')
            continue
        if line.startswith('> '):
            output.append('<aside class="np-callout warning">'+inline(line[2:])+'</aside>')
        elif re.match(r'\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'\d+\. ', lines[i].strip()):
                items.append(re.sub(r'^\d+\. ', '', lines[i].strip()))
                i += 1
            output.append('<ol class="lesson-list">'+''.join('<li>'+inline(x)+'</li>' for x in items)+'</ol>')
            continue
        elif line.startswith('<') or line == '---':
            pass
        else:
            output.append('<p>'+inline(line)+'</p>')
        i += 1
    return '\n'.join(output)

chunks = re.split(r'^## (.+)\n', source, flags=re.M)
articles = []
labels = []
subtitles = ['從數位模型到實體物件，認識機械、加熱與控制。', '辨認機架、列印頭、平台與三軸方向。', '沿著線材路徑理解送料、加熱與堆疊。', '設計、切片、執行，讓數位模型成為實體。', '把馬達旋轉轉換成直線移動。', '從單一組件到整台機器的協調運作。', '用三個方向描述材料放置位置。', '從材料特性理解用途與列印條件。', '依照成品現象，尋找初步檢查方向。', '機械結構、擠出加熱與精準控制。', '用六個問題檢視你的學習成果。']
for number, (title, body) in enumerate(zip(chunks[1::2], chunks[2::2])):
    title = re.sub(r'^\d+\. ', '', title)
    label = '課程導讀' if title == '學習目標' else title
    labels.append(label)
    sections = []
    image_match = re.search(r'!\[([^\]]+)\]\((images/[^)]+)\)\s*\n\s*\*([^\n]+)\*', body)
    image_html = ''
    if image_match:
        alt, path, caption = image_match.groups()
        body = body.replace(image_match.group(0), '')
        preview_name = Path(path).stem + '.webp'
        if not (ROOT / 'output/handout/images/web' / preview_name).is_file():
            raise FileNotFoundError('Run optimize_images.py before building the page')
        width, height = struct.unpack('>II', (ROOT / 'output/handout' / path).read_bytes()[16:24])
        image_html = '<figure class="np-image-card"><button class="figure-button" type="button" aria-label="放大圖解：'+html.escape(alt, quote=True)+'"><img src="'+PREVIEW_BASE+preview_name+'" data-full-src="'+IMAGE_BASE+path+'" width="'+str(width)+'" height="'+str(height)+'" alt="'+html.escape(alt, quote=True)+'" loading="lazy" decoding="async"></button><figcaption>'+inline(caption)+'</figcaption></figure><p class="figure-hint">點選圖解可放大閱讀；按 Esc 關閉。</p>'
    if title == '課堂複習':
        question_body, answer_body = body.split('<details>', 1)
        answer_body = answer_body.split('</details>', 1)[0]
        answer_body = re.sub(r'<summary>.*?</summary>', '', answer_body, flags=re.S)
        sections = [('複習題', blocks(question_body)), ('參考答案', '<div class="np-callout success">先試著回答，再用下面的答案核對觀念。</div>'+blocks(answer_body))]
    else:
        contents = blocks(body)
        if title == '學習目標':
            contents += '<div class="np-card-grid"><div class="np-card"><h4>01 · 看懂機器</h4><p>從結構與運動系統，認識三軸定位和材料擠出。</p></div><div class="np-card"><h4>02 · 理解流程</h4><p>串起 3D 模型、切片、G-code 與逐層堆疊。</p></div><div class="np-card"><h4>03 · 比較材料</h4><p>依原稿比較 PLA、ABS 與 PETG 的特性和用途。</p></div><div class="np-card"><h4>04 · 判讀問題</h4><p>觀察翹曲、偏移與供料中斷，找出檢查方向。</p></div></div><div class="np-callout">左側選章節，上方切子題；也可用下方箭頭依序閱讀。</div>'
        sections = [('學習目標' if number == 0 else '重點講解', contents)]
        if image_html:
            tip = '<aside class="np-callout warning">原稿座標箭頭的畫法容易誤解；以文字 X＝左右、Y＝前後、Z＝上下及機器結構圖為準。</aside>' if title.startswith('座標系統') else ''
            if title.startswith('常見材料'):
                tip = '<aside class="np-callout warning">原圖的「無毒、生物可分解」為簡化敘述，不能作為所有材料產品與使用條件下的保證。請搭配重點講解中的閱讀提醒。</aside>'
            sections.append(('原稿圖解', tip+image_html))
    content = ''
    for tab_index, (tab_title, section_content) in enumerate(sections):
        content += f'<section class="np-section" id="panel-{number}-{tab_index}" role="tabpanel" tabindex="0" data-tab-title="{html.escape(tab_title)}"><div class="np-page-head"><span class="np-page-number">{number+1:02}</span><div><h2>{html.escape(title)}</h2><p>{subtitles[number]}</p></div></div>{section_content}</section>'
    articles.append('<article class="np-page" data-title="'+html.escape(label, quote=True)+'">'+content+'</article>')

extra_css = '''
body{margin:0;background:#f1f5fc}html{scroll-behavior:smooth}button,a{-webkit-tap-highlight-color:transparent}
.np-root{font-size:16px}.np-root .np-nav-label,.np-root .np-tab{font-size:.9rem}.np-root .np-table td{font-size:.94rem}.np-root .np-table th{font-size:.9rem}.np-root .np-table{min-width:520px}
.np-root .np-section p{margin:0 0 16px}.np-root .np-callout{font-weight:400}.np-root .np-sidebar{position:relative}.sidebar-actions{display:grid;gap:10px;margin:24px 8px 0}.sidebar-actions a,.sidebar-actions button{font-size:.8rem;text-align:center}.np-root .np-nav{gap:7px}
.lesson-list{padding-left:1.6em}.lesson-list li{padding:10px 0 12px;border-bottom:1px solid var(--np-soft-line)}
.figure-button{display:block;padding:0;border:0;background:transparent;width:100%;cursor:zoom-in}.np-root .np-image-card{max-width:900px;margin:0 auto}.np-root .np-image-card img{max-height:65vh;object-fit:contain}.figure-hint{text-align:center;font-size:.8rem;color:var(--np-muted);margin-top:8px!important}
.np-root .np-section[hidden],.np-root .np-page[hidden]{display:none!important}.np-root .np-page.is-active{display:block}.np-root .np-main{scroll-margin-top:16px}.np-root .np-stage{min-height:590px}.np-root .np-titleblock p{letter-spacing:.06em}.np-root .np-footer a{display:inline-block;margin:0 6px}
.image-dialog{width:min(1100px,95vw);max-height:95vh;padding:16px;border:1px solid #c9d7f4;border-radius:18px;background:#fbfcff;color:#18305f}.image-dialog::backdrop{background:#10254ac9}.image-dialog img{display:block;max-width:100%;max-height:78vh;object-fit:contain;margin:auto}.image-dialog button{float:right;background:#2f4f9f;color:white;padding:8px 16px;border:0;border-radius:8px;cursor:pointer}.image-dialog p{clear:both;text-align:center;font:14px 'Microsoft JhengHei',sans-serif}.skip-link{position:absolute;top:-100px;left:20px;z-index:10;background:white;padding:8px}.skip-link:focus{top:10px}
button:focus-visible,a:focus-visible,section:focus-visible,.np-table-wrap:focus-visible{outline:3px solid #ff755f;outline-offset:3px}
@media(max-width:720px){.np-root .np-sidebar{padding:12px}.np-root .np-nav{display:flex;overflow-x:auto;gap:8px}.np-root .np-nav-button{min-width:160px;max-width:210px;flex:0 0 auto}.np-root .np-sidebar-title{margin-bottom:8px}.sidebar-actions{display:flex;flex-wrap:wrap;margin:12px 0 0}.np-root .np-nav-label{white-space:normal}.np-root .np-image-card img{max-height:none}.np-root .np-stage{min-height:400px}.np-root .np-table th,.np-root .np-table td{padding:10px}.np-root .np-page-head h2{font-size:1.35rem}.np-root .np-brand-icon{flex-shrink:0}.np-root .np-titleblock p{letter-spacing:0}.np-root .np-nav-button:hover{transform:none}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.np-root *{animation:none!important;transition:none!important}}
@media print{body{background:white}.np-root{width:100%;margin:0;border:0;border-radius:0;box-shadow:none;color:black}.np-root .np-layout{display:block}.np-root .np-sidebar,.np-root .np-tabs-wrap,.np-root .np-controls,.figure-hint,.image-dialog{display:none!important}.np-root .np-masthead{background:white;color:black;min-height:auto;padding:12px}.np-root .np-masthead::after{display:none}.np-root .np-main,.np-root .np-stage{padding:0;border:0}.np-root .np-page[hidden],.np-root .np-section[hidden],.np-root .np-page{display:block!important}.np-root .np-page{break-before:page}.np-root .np-page:first-child{break-before:auto}.np-root .np-section{margin-bottom:24px}.np-root .np-image-card img{max-height:180mm}.np-root .np-table-wrap{overflow:visible}.np-root .np-table{min-width:0}.np-root .np-table th{background:#eaf2ff;color:black}.np-root .np-page-number{background:#eaf2ff;color:black}.np-root .np-callout,.np-root .np-card{box-shadow:none;break-inside:avoid}.np-root .np-footer{background:white}}
'''

script = '''
(() => {
 'use strict';
 const root=document.querySelector('.np-root'),pages=[...root.querySelectorAll('.np-page')],nav=document.getElementById('np-nav'),tabs=document.getElementById('np-tabs'),prev=document.getElementById('np-prev'),next=document.getElementById('np-next');
 let chapter=0,tab=0;
 const sections=i=>[...pages[i].querySelectorAll('.np-section')];
 const total=pages.reduce((sum,p,i)=>sum+sections(i).length,0);
 const warmed=new Map();
 function warmImage(img){if(!img||warmed.has(img.src))return;const cached=new Image();cached.decoding='async';warmed.set(img.src,cached);cached.src=img.src;}
 function warmNearby(){warmImage(pages[chapter].querySelector('.figure-button img'));for(let i=chapter+1;i<pages.length;i++){const img=pages[i].querySelector('.figure-button img');if(img){warmImage(img);break;}}}
 function hash(){const m=location.hash.match(/^#chapter-(\\d+)-tab-(\\d+)$/);if(m){chapter=Math.max(0,Math.min(pages.length-1,Number(m[1])-1));tab=Math.max(0,Math.min(sections(chapter).length-1,Number(m[2])-1));}}
 function button(text,cls){const b=document.createElement('button');b.type='button';b.className=cls;b.textContent=text;return b;}
 pages.forEach((p,i)=>{const b=button('', 'np-nav-button');b.dataset.chapter=i;const n=document.createElement('span');n.className='np-nav-index';n.textContent=String(i+1).padStart(2,'0');const label=document.createElement('span');label.className='np-nav-label';label.textContent=p.dataset.title;b.append(n,label);b.addEventListener('click',()=>{chapter=i;tab=0;render(true);});nav.append(b);});
 function render(scroll=false){
  [...nav.children].forEach((b,i)=>b.setAttribute('aria-current',String(i===chapter)));
  tabs.replaceChildren();sections(chapter).forEach((s,i)=>{const b=button(s.dataset.tabTitle,'np-tab');b.setAttribute('role','tab');b.id='tab-'+chapter+'-'+i;b.setAttribute('aria-controls',s.id);b.setAttribute('aria-selected',String(i===tab));b.tabIndex=i===tab?0:-1;s.setAttribute('aria-labelledby',b.id);b.addEventListener('click',()=>{tab=i;render();document.getElementById(b.id).focus();});b.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();const count=sections(chapter).length;tab=e.key==='Home'?0:e.key==='End'?count-1:(tab+(e.key==='ArrowRight'?1:-1)+count)%count;render();tabs.children[tab].focus();}});tabs.append(b);});
  pages.forEach((p,i)=>{p.hidden=i!==chapter;p.classList.toggle('is-active',i===chapter);sections(i).forEach((s,j)=>{s.hidden=i!==chapter||j!==tab;});});
  warmNearby();
  const current=pages.slice(0,chapter).reduce((sum,p,i)=>sum+sections(i).length,0)+tab+1;
  prev.disabled=current===1;next.disabled=current===total;document.getElementById('np-progress').style.width=current/total*100+'%';document.getElementById('np-page-count').textContent=String(current).padStart(2,'0')+' / '+total+' · '+pages[chapter].dataset.title;
  history.replaceState(null,'','#chapter-'+String(chapter+1).padStart(2,'0')+'-tab-'+(tab+1));
  if(scroll&&window.innerWidth<=720)document.getElementById('np-main').scrollIntoView({block:'start'});
 }
 function move(delta){if(delta>0){if(tab+1<sections(chapter).length)tab++;else if(chapter+1<pages.length){chapter++;tab=0;}}else{if(tab>0)tab--;else if(chapter>0){chapter--;tab=sections(chapter).length-1;}}render(true);}
 prev.addEventListener('click',()=>move(-1));next.addEventListener('click',()=>move(1));window.addEventListener('hashchange',()=>{hash();render();});
 document.addEventListener('keydown',e=>{if(e.defaultPrevented||e.altKey||e.ctrlKey||e.metaKey||e.target.closest('input,textarea,select,button,a,summary,[contenteditable="true"],[role="tab"]')||document.querySelector('dialog[open]'))return;if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();move(e.key==='ArrowRight'?1:-1);}});
 document.getElementById('print-handout').addEventListener('click',async event=>{const control=event.currentTarget;control.disabled=true;control.textContent='正在準備圖片…';try{const images=[...root.querySelectorAll('.figure-button img')];images.forEach(img=>{img.loading='eager';warmImage(img);});await Promise.all(images.map(img=>img.decode().catch(()=>{})));window.print();}finally{control.disabled=false;control.textContent='列印完整講義';}});
 const dialog=document.getElementById('image-dialog'),large=document.getElementById('large-image'),caption=document.getElementById('large-caption');let origin;
 let imageGeneration=0;
 root.querySelectorAll('.figure-button').forEach(b=>b.addEventListener('click',()=>{origin=b;const img=b.querySelector('img');large.src=img.currentSrc||img.src;large.alt=img.alt;caption.textContent=img.alt+' · 正在載入高清原圖…';dialog.showModal();const generation=++imageGeneration;const full=new Image();full.onload=()=>{if(generation===imageGeneration&&dialog.open){large.src=full.src;caption.textContent=img.alt;}};full.onerror=()=>{if(generation===imageGeneration&&dialog.open)caption.textContent=img.alt+' · 高清原圖暫時無法載入，先顯示閱讀圖。';};full.src=img.dataset.fullSrc;}));document.getElementById('close-image').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});dialog.addEventListener('close',()=>{imageGeneration++;origin?.focus();});
 hash();render();
})();
'''

page = '''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="3D 列印機器原理圖解講義：九個主題、八張圖解、材料比較與課堂複習。"><title>3D 列印機器原理｜互動教學講義</title><style>'''+css+extra_css+'''</style></head><body>
<a class="skip-link" href="#np-main">跳到講義內容</a>
<div class="np-root"><header class="np-masthead"><div class="np-brand-icon" aria-hidden="true">⬡</div><div class="np-titleblock"><h1>3D 列印機器原理</h1><p>機械結構 × 擠出加熱 × 精準控制｜圖解教學講義</p></div></header>
<div class="np-layout"><aside class="np-sidebar"><p class="np-sidebar-title">COURSE CONTENTS · 課程目錄</p><nav class="np-nav" id="np-nav" aria-label="章節導覽"></nav><div class="sidebar-actions"><button type="button" class="np-external-link" id="print-handout">列印完整講義</button><a class="np-external-link" href="3D列印機器原理.pdf" target="_blank" rel="noopener">原始 PDF ↗</a><a class="np-external-link" href="https://hackmd.io/KYyn9hZ1QmibLLlXRzqc1w" target="_blank" rel="noopener">HackMD 講義 ↗</a></div></aside>
<main class="np-main" id="np-main"><div class="np-tabs-wrap"><div class="np-tabs" id="np-tabs" role="tablist" aria-label="章節子題"></div></div><div class="np-stage">'''+''.join(articles)+'''</div><div class="np-controls"><button class="np-control" id="np-prev" type="button" aria-label="上一頁">←</button><div class="np-progress" aria-hidden="true"><div class="np-progress-bar" id="np-progress"></div></div><button class="np-control" id="np-next" type="button" aria-label="下一頁">→</button><div class="np-page-count" id="np-page-count" aria-live="polite"></div></div></main></div>
<footer class="np-footer">內容與八張裁圖依《3D列印機器原理.pdf》第 1 頁整理。另含學習目標、圖說、辨讀提醒與複習題。<br><a href="https://github.com/max00189xp/3d-printing-hardware-tutorial" target="_blank" rel="noopener">GitHub 專案 ↗</a><span>3D 列印硬體教學 · 2026</span></footer></div>
<dialog class="image-dialog" id="image-dialog" aria-label="放大圖解"><button type="button" id="close-image">關閉 ✕</button><p id="large-caption"></p><img id="large-image" alt=""></dialog><noscript><p>請啟用 JavaScript 使用章節分頁；亦可閱讀 <a href="output/handout/3D列印機器原理講義.md">Markdown 講義</a>。</p><style>.np-root .np-page,.np-root .np-section{display:block!important}.np-tabs-wrap,.np-controls{display:none}</style></noscript><script>'''+script+'''</script></body></html>'''
(ROOT / 'index.html').write_text(page, encoding='utf-8')
print('Built index.html:', len(articles), 'chapters,', sum(a.count('role="tabpanel"') for a in articles), 'subpages,', page.count('loading="lazy"'), 'figures')
