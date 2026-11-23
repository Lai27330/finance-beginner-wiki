# -*- coding: utf-8 -*-
"""依 wiki/glossary.md，在逐頁稿每個術語「第一次出現」的頁面寫入「術語」欄（AGENTS.md 7.2）。
用法：python3 scripts/add_terms.py <slug>。可重複執行：舊的術語欄會先刪掉再重寫。之後由 check.py G4 驗證。"""
import sys, re, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, 'scripts'); import check
p = glob.glob(f'slides/*-{sys.argv[1]}.md')[0]; s = open(p, encoding='utf-8').read()
head, body = s.split('\n# 逐頁稿', 1); body = '\n# 逐頁稿' + body
gl = check.glossary(); gd = dict(gl); sp = check.slide_pages(body)
bypage = {}
for t, i in check.first_use([(a, b) for a, b, _ in sp], gl).items(): bypage.setdefault(i, []).append(t)
chunks = re.split(r'(^## 第 \d+ 頁[^\n]*\n)', body, flags=re.M); out = [chunks[0]]
for n, k in enumerate(range(1, len(chunks), 2), 1):
    hdr, pg = chunks[k], re.sub(r'^- 術語：.*\n', '', chunks[k+1], flags=re.M)
    if n in bypage:
        vis = re.sub(r'\s', '', sp[n-1][1])
        ts = sorted(bypage[n], key=lambda t: vis.find(t.replace(' ', '')))
        pg = pg.replace('- 講者備註：', '- 術語：' + '；'.join(f'{t}＝{gd[t]}' for t in ts) + '\n- 講者備註：', 1)
    out += [hdr, pg]
open(p, 'w', encoding='utf-8').write(head + ''.join(out))
for i in sorted(bypage): print(f'第 {i} 頁：', '、'.join(bypage[i]))
