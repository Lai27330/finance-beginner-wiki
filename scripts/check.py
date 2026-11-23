# -*- coding: utf-8 -*-
"""自動檢查（AGENTS.md 6.3）。用法：python3 scripts/check.py G2|G3|G4|G5 [slug]
只檢查程式能判斷的項目；結果要寫進 runs/ 的執行紀錄。"""
import sys, os, re, glob, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BANNED = ['推薦買', '必買', '穩賺', '保證獲利', '無風險', '一定會漲', '飆股', '明牌', '快上車', '財富自由捷徑']
problems = []

def fm(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', t, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, t)

def report(rule, where, msg):
    problems.append((rule, where, msg))

def banned(path, text):
    for ln, line in enumerate(text.split('\n'), 1):
        for w in BANNED:
            if w in line and '❌' not in line.split(w)[0] and f'「{w}' not in line:
                report('禁用詞', f'{path}:{ln}', f'出現「{w}」')

def links(path, text):
    for h in re.findall(r'\]\(([^)#\s]+)\)', text):
        if h.startswith('http'): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), h))):
            report('斷連結', path, h)

def section(body, name):
    m = re.search(rf'^## {name}\n(.*?)(?=^## |\Z)', body, re.S | re.M)
    return m.group(1) if m else ''

def g2():
    pages = [p for p in glob.glob('wiki/**/*.md', recursive=True)]
    content = [p for p in pages if p.split('/')[1] in ('concepts', 'tools', 'rules', 'paths')]
    levels = {os.path.basename(p)[:-3]: fm(p)[0].get('level') for p in glob.glob('wiki/sources/*.md')}
    for p in pages:
        meta, body = fm(p)
        links(p, body); banned(p, body)
    for p in content:
        meta, body = fm(p)
        kind = p.split('/')[1]
        for k in ('type', 'title', 'summary', 'level', 'sources', 'updated'):
            if k not in meta: report('欄位缺漏', p, k)
        # 事實句要有來源
        sec = section(body, '重點說明') if kind in ('concepts', 'tools') else section(body, '步驟') if kind == 'paths' else ''
        for line in sec.split('\n'):
            if line.startswith(('- ', '1', '2', '3', '4', '5')) and '來源：' not in line and '待補' not in line and '→ [' not in line:
                report('事實無來源', p, line.strip()[:40])
        # 數字要有年度（概念頁重點說明中的 % 或「元」）
        for line in sec.split('\n'):
            if re.search(r'\d+(\.\d+)?%', line) and not re.search(r'20\d\d', line):
                report('數字無年度', p, line.strip()[:40])
        # 概念頁：重點說明中的制度數字若只引用 B 級來源，必須標註「B 級報導」（2026-11-23 新增）
        if kind in ('concepts', 'tools'):
            for line in sec.split('\n'):
                if not re.search(r'\d+(\.\d+)?\s*(%|年|元|個月|天)', line) or '建議' in line or '假設' in line: continue
                cited = re.findall(r'sources/([\w-]+)\.md', line)
                if cited and all(levels.get(x) == 'B' for x in cited) and 'B 級報導' not in line:
                    report('概念頁制度數字只有 B 級來源', p, line.strip()[:40])
        # 制度頁：表格每列要有年度，且來源只能是 A 級
        if kind == 'rules':
            for line in section(body, '規定內容').split('\n'):
                if line.startswith('|') and not line.startswith(('| 項目', '|---')):
                    cells = [c.strip() for c in line.strip('|').split('|')]
                    if len(cells) < 4 or not re.match(r'20\d\d', cells[2]):
                        report('數字無年度', p, cells[0])
            for s in meta.get('sources', []):
                if levels.get(s) != 'A':
                    report('制度頁使用非 A 級來源', p, s)
    # 孤兒頁
    alltext = {p: open(p, encoding='utf-8').read() for p in pages}
    for p in content:
        name = os.path.basename(p)
        if not any(name in t for q, t in alltext.items() if q != p and not q.endswith('index.md')):
            report('孤兒頁（只有目錄連到）', p, '')
    # index 同步
    idx = alltext.get('wiki/index.md', '')
    for p in content + glob.glob('wiki/sources/*.md'):
        if os.path.relpath(p, 'wiki') not in idx: report('目錄未收錄', p, '')

def g3(slug):
    for p in glob.glob(f'notes/*-{slug}.md'):
        meta, body = fm(p)
        sec = section(body, '重點整理')
        for para in [x.strip() for x in sec.split('\n\n') if x.strip() and not x.strip().startswith('###')]:
            if '../wiki/' not in para:
                report('筆記段落沒有引用 Wiki', p, para.strip()[:40])
        links(p, body); banned(p, body)

PREVIEW = {'cover', 'goals'}   # 封面、學習目標只是預告，術語在第一個內容頁解釋

def glossary():
    """讀 wiki/glossary.md → [(術語, 白話解釋)]，長的排前面（先比對「盤後零股」再比對「零股」）。"""
    rows = re.findall(r'^\| ([^|]+?) \| ([^|]+?) \| \[', open('wiki/glossary.md', encoding='utf-8').read(), re.M)
    rows = [(t.strip(), d.strip()) for t, d in rows if t.strip() != '術語']
    return sorted(rows, key=lambda x: -len(x[0].replace(' ', '')))

def terms_in(text, gl):
    text = re.sub(r'\s', '', text); found = []
    for t, _ in gl:
        k = t.replace(' ', '')
        if k in text: found.append(t); text = text.replace(k, '□')
    return found

def first_use(pages, gl):
    """pages: [(版型, 可見文字)] → {術語: 第一次出現的頁碼(1 起算)}"""
    first = {}
    for i, (layout, text) in enumerate(pages, 1):
        if layout in PREVIEW: continue
        for t in terms_in(text, gl): first.setdefault(t, i)
    return first

def slide_pages(body):
    out = []
    for pg in re.split(r'^## 第 \d+ 頁[^\n]*\n', body, flags=re.M)[1:]:
        m = re.search(r'版型：(\w[\w-]*)', pg); layout = m.group(1) if m else ''
        vis = [l for l in pg.split('\n') if not re.match(r'- (版型|講者備註|依據|術語)：', l)]
        out.append((layout, '\n'.join(vis), pg))
    return out

def g4(slug):
    need = {'cover', 'goals', 'quiz', 'recap', 'ending'}
    for p in glob.glob(f'slides/*-{slug}.md'):
        meta, body = fm(p)
        pages = re.split(r'^## 第 \d+ 頁', body, flags=re.M)[1:]
        found = set()
        for i, pg in enumerate(pages, 1):
            m = re.search(r'版型：(\w[\w-]*)', pg); found.add(m.group(1) if m else '')
            if '依據：' not in pg or re.search(r'依據：\s*$', pg, re.M): report('頁面沒有依據', p, f'第 {i} 頁')
        for n in need - found: report('教學結構缺少', p, n)
        banned(p, body)
        # 術語檢查：第一次出現的那一頁，「術語」欄要有 glossary 的白話解釋
        gl = glossary(); gd = dict(gl); sp = slide_pages(body)
        for t, i in first_use([(a, b) for a, b, _ in sp], gl).items():
            m = re.search(r'^- 術語：(.*)$', sp[i-1][2], re.M)
            if not m or f'{t}＝{gd[t]}' not in m.group(1):
                report('術語第一次出現沒有解釋', p, f'第 {i} 頁「{t}」')

def runtime(deck, slug):
    """用瀏覽器實際執行簡報：JS 錯誤、逐頁切換、版面溢出，並存逐頁截圖（2026-11-23 新增）。"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        report('無法執行瀏覽器檢查', deck, '未安裝 playwright，需人工打開檢查'); return
    out = f'runs/screens/{slug}'; os.makedirs(out, exist_ok=True)
    url = 'file://' + os.path.abspath(deck)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, vp in (('desktop', {'width': 1280, 'height': 720}), ('mobile', {'width': 390, 'height': 844})):
            pg = b.new_page(viewport=vp); errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(url); pg.wait_for_timeout(500)
            n = pg.evaluate("document.querySelectorAll('.slide').length")
            for i in range(n):
                idx = pg.evaluate("[...document.querySelectorAll('.slide')].findIndex(s => s.classList.contains('active'))")
                if idx != i: report('翻頁失敗', deck, f'{name} 第 {i+1} 頁無法切換'); break
                pg.wait_for_timeout(500)
                if name == 'desktop':
                    over = pg.evaluate("(() => { const s = document.querySelector('.slide.active'); return s.scrollHeight - s.clientHeight; })()")
                    if over > 4: report('版面溢出', deck, f'第 {i+1} 頁超出畫面 {over}px')
                pg.screenshot(path=f'{out}/{name}-{i+1:02d}.png')
                pg.keyboard.press('ArrowRight')
            for e in errs: report('JS 錯誤', deck, f'{name}：{e[:60]}')
        b.close()

def g5(slug):
    for d in glob.glob(f'decks/*-{slug}/index.html'):
        t = open(d, encoding='utf-8').read()
        if '{{' in t or '}}' in t: report('殘留佔位符', d, '')
        n_html = t.count('class="slide')
        sl = glob.glob(f'slides/*-{slug}.md')
        if sl:
            n_md = len(re.findall(r'^## 第 \d+ 頁', open(sl[0], encoding='utf-8').read(), re.M))
            if n_html != n_md: report('頁數不一致', d, f'簡報 {n_html} 頁、逐頁稿 {n_md} 頁')
        for i, sec in enumerate(re.findall(r'<section class="slide[^>]*>', t), 1):
            if 'data-source=' not in sec: report('投影片沒有 data-source', d, f'第 {i} 張')
        if '不構成任何投資建議' not in t: report('缺少免責聲明', d, '')
        # 術語檢查（畫面版）：簡報畫面上第一次出現的術語，那一張要有名詞小卡
        gl = glossary(); secs = re.findall(r'<section class="slide" data-layout="([\w-]+)".*?</section>', t, re.S)
        bodies = re.findall(r'<section class="slide".*?</section>', t, re.S)
        vis = [re.sub(r'<[^>]+>', ' ', re.sub(r'<aside class="notes">.*?</aside>|<dl class="terms">.*?</dl>', '', b, flags=re.S)) for b in bodies]
        for term, i in first_use(list(zip(secs, vis)), gl).items():
            card = re.search(r'<dl class="terms">(.*?)</dl>', bodies[i-1], re.S)
            if not card or f'<dt>{term}</dt>' not in card.group(1):
                report('畫面上術語第一次出現沒有名詞小卡', d, f'第 {i} 張「{term}」')
        banned(d, re.sub(r'<[^>]+>', ' ', t))
        runtime(d, slug)

if __name__ == '__main__':
    gate = sys.argv[1] if len(sys.argv) > 1 else 'G2'
    slug = sys.argv[2] if len(sys.argv) > 2 else ''
    {'G2': g2, 'G3': lambda: g3(slug), 'G4': lambda: g4(slug), 'G5': lambda: g5(slug)}[gate]()
    if problems:
        print(f'{gate}：不通過，共 {len(problems)} 項')
        for r, w, m in problems: print(f'  [{r}] {w}  {m}')
        sys.exit(1)
    print(f'{gate}：自動檢查通過')
