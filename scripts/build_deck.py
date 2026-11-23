# -*- coding: utf-8 -*-
"""把逐頁稿（第 2 版）的投影片 HTML 放進模板（AGENTS.md 7.3）。內容只能來自 slides/ 逐頁稿。"""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = '2026-11-22-invest-order-and-quotes'
# Wiki 連結：本機用相對路徑；放上 GitHub Pages 後，頁面上的小程式會自動改成 GitHub 上的網址（不用手動填帳號）
REPO = '../../'

def wave():
    a = []
    for row in range(5):
        for col in range(9):
            cx = col * 60 + (30 if row % 2 else 0); cy = 40 + row * 30
            for r, op in ((28, .55), (20, .4), (12, .3)):
                a.append(f'<path d="M{cx-r} {cy} a{r} {r} 0 0 1 {2*r} 0" fill="none" stroke="#3f7d78" stroke-opacity="{op}" stroke-width="1.2"/>')
    return '<svg class="wave" viewBox="0 0 520 190" preserveAspectRatio="xMaxYMax slice" aria-hidden="true">' + ''.join(a) + '</svg>'

def candle(color, top_label, bot_label):
    return f'''<svg viewBox="0 0 150 220" role="img" aria-label="K 線示意">
  <line x1="50" y1="20" x2="50" y2="200" stroke="{color}" stroke-width="2"/>
  <rect x="30" y="60" width="40" height="90" fill="{color}"/>
  <g font-size="12" fill="#6b7775"><text x="80" y="24">最高</text><text x="80" y="64">{top_label}</text><text x="80" y="154">{bot_label}</text><text x="80" y="204">最低</text></g>
</svg>'''

def sec(layout, chapter, source, body, notes):
    return f'''  <section class="slide" data-layout="{layout}" data-chapter="{chapter}" data-source="{' '.join(source)}">
{body}
    <aside class="notes">{notes}</aside>
  </section>'''

def qbox(q, a):
    return f'<div class="qbox"><p>{q}</p><p class="hint">先自己算，再按「看答案」。</p><button type="button">看答案</button><p class="ans">{a}</p></div>'

S = []
S.append(sec('cover','第一課',['wiki/overview.md'],f'''    <span class="hanko">新手<br>村</span>
    <p class="kicker">理財新手村｜教學簡報｜約 15 分鐘</p>
    <h1>新手投資的<br><span>第一課</span></h1>
    <p class="lead cover-lead">給完全沒有投資經驗的你：<br>錢為什麼要投資、開始前要準備什麼、<br>看盤和下單時畫面上的數字是什麼意思。</p>
    <ol class="chapters">
      <li>為什麼要投資</li><li>投資前的準備</li><li>看懂報價</li><li>大盤</li><li>下單</li><li>交割</li><li>看懂不等於預測</li>
    </ol>
    <p class="note-sm">每一章都有一題可以自己算。</p>
    {wave()}''','今天 15 分鐘，從「為什麼要投資」一路講到「下單後錢什麼時候扣」，每一章都有一題可以自己算。'))
S.append(sec('goals','學習目標',['notes:goals'],'''    <p class="kicker">學習目標</p>
    <h2>看完這份簡報，你能動手……</h2>
    <ol class="goals">
      <li>算出自己的緊急預備金目標</li>
      <li>用複利公式算出 N 年後的金額</li>
      <li>從報價算出漲跌幅，讀懂五檔</li>
      <li>說出「大盤漲 200 點」的意思</li>
      <li>選限價或市價，算出交易成本</li>
      <li>推算 T+2 扣款日</li>
      <li>分辨「看懂」與「預測」</li>
    </ol>''','最後有五題小測驗。'))
S.append(sec('point','情境',['wiki/paths/beginner-invest-order.md'],'''    <p class="kicker">情境</p>
    <h2>領到第一份薪水，<br>可以馬上買股票嗎？</h2>
    <p class="lead">先想三件事。</p>
    <ul class="dots">
      <li>錢放著，會不會變少？</li>
      <li>意外發生時，有沒有錢可以用？</li>
      <li>下單之後，錢什麼時候被扣？</li>
    </ul>''','這三個問題，就是今天的主線。'))
S.append(sec('point','一・為什麼',['wiki/concepts/inflation.md'],'''    <p class="kicker">一、為什麼要投資</p>
    <h2>錢放著，會變「薄」</h2>
    <p class="lead">通膨：物價上漲，同樣的錢能買的東西變少。</p>
    <div class="pair">
      <div class="card"><h3>今年</h3><p>一碗麵 100 元<br>手上有 100 元</p></div>
      <div class="card pale"><h3>一年後</h3><p>一碗麵 105 元<br>100 元存一年只變成 101 元</p></div>
    </div>
    <p><span class="formula">101 ÷ 105 ≈ 0.962，購買力約少 3.8%</span></p>
    <p class="note-sm">來源文章的例子，數字為假設。</p>''','這是來源文章的例子，數字是假設的，用來說明算法。'))
S.append(sec('calc-compound','一・為什麼',['wiki/concepts/compound-interest.md'],'''    <p class="kicker">一、為什麼要投資｜動手算</p>
    <h2>複利：報酬再放回去，像滾雪球</h2>
    <p class="lead">未來金額 ＝ 本金 ×（1＋報酬率）<sup>年數</sup></p>
    <div class="calc calc-c">
      <div>
        <label for="cp">本金（元）</label><input id="cp" name="p" type="number" value="100000" min="0" step="1000">
        <label for="cr">每年報酬率（%，假設）</label><input id="cr" name="r" type="number" value="3" min="0" step="0.5">
        <label for="cn">年數</label><input id="cn" name="n" type="number" value="10" min="0" step="1">
      </div>
      <div>
        <table>
          <tr><td>複利（報酬再投入）</td><td data-o="comp"></td></tr>
          <tr><td>每年把報酬領出</td><td data-o="simple"></td></tr>
          <tr class="total"><td>差距</td><td data-o="gap"></td></tr>
        </table>
        <div class="bars"><div><span></span><em>本金</em></div><div><span></span><em>每年領出</em></div><div class="c"><span></span><em>複利</em></div></div>
      </div>
    </div>
    <p class="note-sm">報酬率是假設的；實際投資每年報酬不同，也可能虧損。</p>''','預設 10 萬元、3%、10 年約 134,392 元。可以把年數改成 30 年看看差距。'))
S.append(sec('steps','二・準備',['wiki/paths/beginner-invest-order.md'],'''    <p class="kicker">二、投資前的準備</p>
    <h2>投資前的五個步驟</h2>
    <p class="lead">預備金和還債，排在投資之前。</p>
    <div class="steps">
      <div class="step"><b>01</b><span>存緊急預備金</span></div>
      <div class="step"><b>02</b><span>付固定支出、還高利債務</span></div>
      <div class="step"><b>03</b><span>檢視保險</span></div>
      <div class="step"><b>04</b><span>了解風險屬性（能承受多大的波動）、訂目標</span></div>
      <div class="step"><b>05</b><span>開始學市場基本知識</span></div>
    </div>''','不同來源步驟切法略有不同，但都同意預備金和還債要先做。'))
S.append(sec('calc-fund','二・準備',['wiki/concepts/emergency-fund.md'],'''    <p class="kicker">二、投資前的準備｜動手算</p>
    <h2>緊急預備金是投資的安全帽</h2>
    <p class="lead">急用時，<strong>不必被迫在下跌時賣掉投資</strong>。</p>
    <div class="calc calc-f">
      <div>
        <label for="fs">每月薪資（元）</label><input id="fs" name="salary" type="number" value="30000" min="0" step="1000">
        <label for="fm">想準備幾個月</label><input id="fm" name="months" type="number" value="3" min="0" step="1">
      </div>
      <div>
        <table><tr class="total"><td>預備金目標</td><td data-o="fund"></td></tr></table>
        <ul class="dots" style="margin-top:3vh">
          <li>有作者建議 3～6 個月（建議，不是規定）</li>
          <li>放在方便提款、平常少用的帳戶</li>
        </ul>
      </div>
    </div>''','可以先從 1 個月開始存。'))
S.append(sec('compare','二・準備',['wiki/concepts/debt-first.md'],'''    <p class="kicker">二、投資前的準備</p>
    <h2>為什麼先還債？</h2>
    <p class="lead">債的利息確定要付，投資報酬卻不一定。</p>
    <div class="pair">
      <div class="card pale"><h3>債務利息</h3><p>確定要付，每個月都在累積。卡債循環利息會越滾越大。</p></div>
      <div class="card"><h3>投資報酬</h3><p>不確定，也可能虧損。</p></div>
    </div>''','這裡的債指卡債、小額信貸、親友借款，不含房貸。'))
S.append(sec('quote-screen','三・看懂',['wiki/concepts/quote-screen.md'],f'''    <p class="kicker">三、看懂報價畫面｜動手算</p>
    <h2>打開看盤畫面，先看這幾個數字</h2>
    <div class="qs-wrap">
      <div class="quote" aria-label="虛構的範例報價">
        <div class="qhead"><span class="qname">範例股 0000</span><span class="qtag">虛構範例</span></div>
        <div><span class="qprice">102</span></div>
        <dl>
          <div><dt>昨收</dt><dd>100</dd></div><div><dt>開盤</dt><dd class="up">101</dd></div><div><dt>最高</dt><dd class="up">103</dd></div>
          <div><dt>最低</dt><dd class="down">99</dd></div><div><dt>收盤</dt><dd class="up">102</dd></div><div><dt>成交量</dt><dd>5,000 張</dd></div>
        </dl>
      </div>
      <div>
        <ul class="dots">
          <li>漲跌要跟<strong>昨天收盤</strong>比</li>
          <li>成交量多以「張」計，1 張 ＝ 1,000 股</li>
        </ul>
        <div class="try">
          {qbox('漲跌、漲幅是多少？','102 − 100 ＝ ＋2 元；2 ÷ 100 ＝ 2%')}
          {qbox('5,000 張是幾股？','5,000 × 1,000 ＝ 500 萬股')}
        </div>
      </div>
    </div>''','台股用紅色表示上漲、綠色表示下跌，只是方向。'))
S.append(sec('compare','三・看懂',['wiki/concepts/k-line.md'],f'''    <p class="kicker">三、看懂報價畫面</p>
    <h2>紅 K 不一定代表上漲</h2>
    <p class="lead">K 線只比較「今天的收盤」和「今天的開盤」。</p>
    <div class="kline">
      {candle('#c8453c','收盤','開盤')}
      {candle('#2f7d5a','開盤','收盤')}
      <ul class="dots">
        <li>收盤比開盤高：<span class="up">紅 K</span></li>
        <li>收盤比開盤低：<span class="down">綠 K</span></li>
        <li>例：昨收 30、今開 29、收 29.5 → 紅 K，<strong>但比昨天低</strong></li>
      </ul>
    </div>''','漲跌要和昨天收盤比，K 線的顏色只看今天的開盤和收盤。'))
S.append(sec('orderbook','三・看懂',['wiki/concepts/order-book.md'],f'''    <p class="kicker">三、看懂報價畫面｜動手算</p>
    <h2>五檔報價：還在排隊的買單和賣單</h2>
    <p class="lead">左邊是想買的人，右邊是想賣的人。</p>
    <div class="pair">
      <div>
        <table class="book" aria-label="虛構的五檔報價">
          <tr><th>委買張數</th><th>委買價</th><th class="mid">委賣價</th><th>委賣張數</th></tr>
          <tr><td>30</td><td class="bid">99.9</td><td class="ask mid">100.0</td><td>10</td></tr>
          <tr><td>25</td><td class="bid">99.8</td><td class="ask mid">100.5</td><td>20</td></tr>
        </table>
        <p class="note-sm">虛構範例，只列前兩檔。</p>
      </div>
      <div>
        <ul class="dots">
          <li>委買：出價越高越先成交</li>
          <li>委賣：開價越低越先成交</li>
          <li>同一個價格，先排隊的先成交</li>
          <li>你要買，就跟右邊排隊的委賣成交（他們是你的對手方）</li>
        </ul>
        <div class="try">{qbox('用市價買 15 張，會用什麼價格成交？','先買走最便宜的 100.0 元 10 張，不夠再買 100.5 元 5 張')}</div>
      </div>
    </div>''','五檔是還在排隊、沒有成交的單。'))
S.append(sec('point','四・大盤',['wiki/concepts/market-index.md'],f'''    <p class="kicker">四、大盤</p>
    <h2>「大盤漲 200 點」是什麼意思？</h2>
    <p class="lead">大盤是把所有上市股票合起來算的一個數字。</p>
    <ul class="dots">
      <li>大盤＝發行量加權股價指數，民國 55 年設為 100 點</li>
      <li>股本越大的公司影響越大；半導體業占 55.16%（2026-10-30 資料）</li>
      <li>所以大盤漲跌，很大部分是大型半導體股在漲跌</li>
    </ul>
    <div class="pair">
      <p class="remind"><b>像全班的總分</b><br>每個人的分數都算進去，但大個子（股本大的公司）分數占比比較重。</p>
      <div class="try">{qbox('20,000 點漲到 20,200 點，漲幅是多少？','200 ÷ 20,000 ＝ 1%')}</div>
    </div>''','像全班總分，大個子的分數占比比較重。'))
S.append(sec('list','四・大盤',['wiki/concepts/market-index.md'],f'''    <p class="kicker">四、大盤｜動手判斷</p>
    <h2>大盤漲跌，會影響我什麼？</h2>
    <p class="lead">大盤是整個市場的溫度計，會從三個地方碰到你。</p>
    <div class="steps three">
      <div class="step"><b>1</b><h3>大事件，全市場一起動</h3><p>2026 年美伊開戰後到 3/13，大盤跌約 6%<span class="tag-b">B 級報導</span></p></div>
      <div class="step"><b>2</b><h3>市場情緒會帶著你走</h3><p>大盤大漲大跌時，你的股票也可能跟著一起漲跌</p></div>
      <div class="step"><b>3</b><h3>買 ETF 就直接連動</h3><p>報酬跟著它追蹤的指數走；不是每檔都追蹤大盤</p></div>
    </div>
    <div class="try">{qbox('A 天：大盤跌 2%，你的股票跌 2%。B 天：大盤漲 1%，你的股票跌 5%。哪一天比較可能是公司自己的問題？','B 天：大盤在漲，你的股票卻大跌，比較可能是公司本身的原因；A 天比較像整個市場一起跌（數字為假設）')}</div>''','大盤由大型股主導，大盤漲的那天，小公司的股票可能沒漲。判斷題數字為假設。'))
S.append(sec('list','五・下單',['wiki/rules/trading-hours.md','wiki/rules/price-limit.md','wiki/rules/trading-unit.md'],'''    <p class="kicker">五、下單</p>
    <h2>什麼時候可以買？一次買多少？</h2>
    <div class="timeline" aria-hidden="true">
      <div class="bar"></div>
      <div class="seg light" style="left:0%;width:10%"></div>
      <div class="seg" style="left:10%;width:55%"></div>
      <div class="seg light" style="left:67%;width:13%"></div>
      <span class="tick" style="left:0%">8:30</span><span class="tick" style="left:10%">9:00</span><span class="tick" style="left:65%">13:30</span><span class="tick" style="left:80%">14:30</span>
      <span class="tick b" style="left:5%">先下單排隊</span><span class="tick b" style="left:37%">整股、盤中零股成交</span><span class="tick b" style="left:74%">盤後零股 13:40～</span>
    </div>
    <ul class="dots">
      <li>一天最多漲跌 10%（漲停、跌停）</li>
      <li>1 張 ＝ 1,000 股；零股是 1～999 股</li>
      <li>新聞報導 12/7 起零股改 9:00 開盤，以證交所公告為準</li>
    </ul>
    <p class="caution">零股和整股時段重疊，下錯單位可能差 1,000 倍。</p>
    <p class="note-sm">以上為 2026 年規定。</p>''','8:30 可以先下單排隊，9:00 到 13:30 才真正成交。'))
S.append(sec('compare','五・下單',['wiki/rules/order-types.md'],'''    <p class="kicker">五、下單｜第一步</p>
    <h2>下單第一步：價格怎麼定？</h2>
    <p class="lead">限價控制價格，市價比較快成交。</p>
    <div class="pair">
      <div class="card"><h3>限價</h3><p>自己指定價格，例如「最多 100 元買」。<br>能控制價格，但可能買不到。</p></div>
      <div class="card pale"><h3>市價</h3><p>不指定價格，直接跟對手方正在排隊的價格成交。<br>比較快，但價格不由自己決定。</p></div>
    </div>
    <p class="caution">同時排隊時，市價單優先於限價單。</p>
    <p class="note-sm">2026 年規定。本簡報只說明差別，不建議要選哪一種。</p>''','本簡報只說明差別，不建議要選哪一種。'))
S.append(sec('order-types','五・下單',['wiki/rules/order-types.md'],'''    <p class="kicker">五、下單｜第二步・動手判斷</p>
    <h2>下單第二步：這張單要等多久？</h2>
    <p class="lead">除了價格，還要選「沒成交時怎麼辦」。</p>
    <ul class="dots">
      <li><b>ROD</b>（當日有效）：今天收盤前都有效，沒成交就繼續排隊</li>
      <li><b>IOC</b>（立即成交否則取消）：能成交多少算多少，剩下立刻取消</li>
      <li><b>FOK</b>（全部成交否則取消）：不能一次全部成交，就整筆取消</li>
    </ul>
    <p class="lead" style="margin:1.6vh 0 0">情境：你要買 50 張，賣方只有 30 張。</p>
    <div class="toggle">
      <button type="button" data-r="ROD：買到 30 張，剩下 20 張繼續排隊到收盤。">ROD</button>
      <button type="button" data-r="IOC：買到 30 張，剩下 20 張取消。">IOC</button>
      <button type="button" data-r="FOK：沒辦法一次買滿 50 張，整筆取消，一張都沒買到。">FOK</button>
    </div>
    <p class="result">點選上面的按鈕，看看結果。</p>
    <p class="note-sm">開盤、收盤時段只能用限價＋ROD（2026 年規定）。</p>''','價格兩種 × 等多久三種，共 6 種組合。'))
S.append(sec('calc','五・下單',['wiki/rules/trading-costs.md'],'''    <p class="kicker">五、下單｜動手算</p>
    <h2>價格沒變，賣掉也會少一點錢</h2>
    <p class="lead">手續費買賣各一次，賣出再加證交稅。</p>
    <div class="calc">
      <div>
        <label for="c-price">股價（元）</label><input id="c-price" name="price" type="number" value="50" min="0" step="0.05">
        <label for="c-shares">股數</label><input id="c-shares" name="shares" type="number" value="1000" min="0" step="1">
        <p class="note-sm">手續費 0.1425%（一般上限）、股票證交稅 0.3%（2026 年規定）。假設不打折、未計最低手續費。</p>
      </div>
      <table>
        <tr><td>成交金額</td><td data-o="amt"></td></tr>
        <tr><td>買進手續費</td><td data-o="buy"></td></tr>
        <tr><td>賣出手續費</td><td data-o="sell"></td></tr>
        <tr><td>證交稅（賣出時）</td><td data-o="tax"></td></tr>
        <tr class="total"><td>來回成本</td><td data-o="total"></td></tr>
      </table>
    </div>''','預設 50 元買賣 1 張，來回約 292.5 元。'))
S.append(sec('t2','六・交割',['wiki/rules/settlement-t2.md'],'''    <p class="kicker">六、交割｜動手推算</p>
    <h2>買了股票，錢什麼時候扣？</h2>
    <p class="lead">成交後第 2 個營業日（T+2），上午 10 點前。</p>
    <ul class="dots">
      <li>T＝成交日，當天不扣款</li>
      <li>T+2 上午 10 時前，交割帳戶（開戶時綁定的扣款帳戶）要有錢</li>
    </ul>
    <p class="lead" style="margin:2vh 0 0">點選成交日：</p>
    <div class="t2">
      <button type="button" data-d="0">週一</button><button type="button" data-d="1">週二</button><button type="button" data-d="2">週三</button><button type="button" data-d="3">週四</button><button type="button" data-d="4">週五</button>
    </div>
    <div class="week" aria-hidden="true">
      <div>週一</div><div>週二</div><div>週三</div><div>週四</div><div>週五</div><div class="off">週六<small>休市</small></div><div class="off">週日<small>休市</small></div><div>下週一</div><div>下週二</div>
    </div>
    <p class="result">點選成交日，看看 T+2 是哪一天。</p>
    <p class="note-sm">不考慮國定假日；遇到休市要再往後延（2026 年規定）。</p>''','週末不算營業日；遇到國定假日、颱風休市還要再往後延。'))
S.append(sec('sim','綜合練習',['wiki/rules/order-types.md','wiki/concepts/order-book.md','wiki/rules/trading-costs.md','wiki/rules/settlement-t2.md','wiki/rules/trading-unit.md'],'''    <p class="kicker">綜合練習｜動手做</p>
    <h2>自己下一張單試試看</h2>
    <p class="lead" style="margin-bottom:1.2vh">照順序填完委託單，按「送出」看會怎樣成交、要付多少、哪天扣款。</p>
    <div class="sim">
      <div>
        <div class="srow" data-k="side"><span class="sn">①</span><b>買或賣</b><div class="seg"><button type="button" data-v="buy">買進</button><button type="button" data-v="sell">賣出</button></div></div>
        <div class="srow" data-k="unit"><span class="sn">②</span><b>單位</b><div class="seg"><button type="button" data-v="lot">整股（張）</button><button type="button" data-v="odd">零股（股）</button></div></div>
        <div class="srow" data-k="ptype"><span class="sn">③</span><b>價格</b><div class="seg"><button type="button" data-v="limit">限價</button><select name="price" aria-label="限價價格"><option value="99.5">99.5</option><option value="99.6">99.6</option><option value="99.7">99.7</option><option value="99.8">99.8</option><option value="99.9">99.9</option><option value="100.0">100.0</option><option value="100.5" selected>100.5</option><option value="101.0">101.0</option><option value="101.5">101.5</option><option value="102.0">102.0</option><option value="102.5">102.5</option></select><button type="button" data-v="market">市價</button></div></div>
        <div class="srow"><span class="sn">④</span><b>數量</b><div class="seg"><input name="qty" type="number" value="15" min="1" max="99" step="1" aria-label="數量"><span class="ulabel">張</span></div></div>
        <div class="srow" data-k="tif"><span class="sn">⑤</span><b>等多久</b><div class="seg"><button type="button" data-v="ROD">ROD</button><button type="button" data-v="IOC">IOC</button><button type="button" data-v="FOK">FOK</button></div></div>
        <div class="srow"><span class="sn">⑥</span><b>今天是</b><div class="seg"><select name="day" aria-label="成交日"><option value="0">週一</option><option value="1">週二</option><option value="2">週三</option><option value="3" selected>週四</option><option value="4">週五</option></select></div></div>
        <p class="lockmsg"></p>
        <button type="button" class="send">送出委託單</button>
      </div>
      <div>
        <p class="note-sm bookcap" style="margin:0 0 .4vh">整股五檔（張）</p>
        <table class="book mini" aria-label="虛構範例股 0000 五檔">
          <tr><th>委買張數</th><th>委買價</th><th class="mid">委賣價</th><th>委賣張數</th></tr>
          <tr><td>30</td><td class="bid">99.9</td><td class="ask mid">100.0</td><td>10</td></tr><tr><td>25</td><td class="bid">99.8</td><td class="ask mid">100.5</td><td>20</td></tr><tr><td>40</td><td class="bid">99.7</td><td class="ask mid">101.0</td><td>15</td></tr><tr><td>18</td><td class="bid">99.6</td><td class="ask mid">101.5</td><td>30</td></tr><tr><td>50</td><td class="bid">99.5</td><td class="ask mid">102.0</td><td>25</td></tr>
        </table>
        <div class="ticket" aria-live="polite"><p class="t-sum">情境：盤中 10:00，你已持有範例股 0000 50 張又 300 股。</p><p>填好左邊再按「送出委託單」。<br>試試：市價買 15 張；FOK 買 50 張；<br>零股限價 101.0 元買 150 股。</p></div>
      </div>
    </div>
    <p class="note-sm" style="margin-top:1.2vh">虛構五檔。費率 0.1425%、證交稅 0.3%（2026 年），不打折；零股以最低手續費 20 元為例、成交價簡化計算；不考慮國定假日。</p>''','試試看：市價買 15 張、FOK 買 50 張、零股限價 101.0 元買 150 股。'))
S.append(sec('list','六・交割',['wiki/concepts/default-settlement.md'],'''    <p class="kicker">六、交割</p>
    <h2>錢不夠，會發生什麼事？</h2>
    <p class="lead">違約交割的後果，比想像中嚴重。<span class="tag-b">B 級報導・法規原文待確認</span></p>
    <ul class="dots">
      <li>券商凍結帳戶、強制賣出股票</li>
      <li>違約金最高可達成交金額 7%（例：30 萬 × 7% ＝ 21,000 元）</li>
      <li>紀錄進聯徵（銀行查詢的信用紀錄）、帳戶可能被註銷，5 年內不能開戶</li>
      <li>情節重大有刑責</li>
    </ul>''','以上後果來自新聞報導，法規原文待確認。'))
S.append(sec('list','七・提醒',['wiki/concepts/k-line.md','wiki/concepts/order-book.md','wiki/concepts/market-index.md','wiki/concepts/investment-fraud.md'],'''    <p class="kicker">七、看懂不等於預測</p>
    <h2>新手常見的四個誤解</h2>
    <div class="pair">
      <div class="card"><p>❌ 紅 K 就是上漲</p><p>✅ 漲跌要和昨收比</p></div>
      <div class="card"><p>❌ 成交價就是我能買到的價</p><p>✅ 要看委賣那一側</p></div>
      <div class="card"><p>❌ 大盤漲，我的股票也漲</p><p>✅ 個股不一定</p></div>
      <div class="card"><p>❌ 名人推薦比較可靠</p><p>✅ 詐騙常冒用名人</p></div>
    </div>
    <p class="note-sm">有疑慮可撥 165 或 02-2737-3434 查證。</p>''','看懂數字，也要看懂它沒說的事。'))
QZ = [
 ('Q1　昨收 30、今開 29、收 29.5，今天是？', ['紅 K，而且上漲', '紅 K，但比昨天低', '綠 K，而且下跌'], 1, '收盤 29.5 高於開盤 29 是紅 K，但比昨收 30 低。'),
 ('Q2　委賣 100.0 元 10 張、100.5 元 20 張，市價買 5 張用什麼價格？', ['99.9 元', '100.0 元', '100.5 元'], 1, '先用最低的委賣價 100.0 元成交，10 張足夠。'),
 ('Q3　週四成交，最晚什麼時候要付款？', ['週五上午 10 點前', '下週一上午 10 點前', '下週二上午 10 點前'], 1, '週末不算營業日：週五 T+1、下週一 T+2。'),
 ('Q4　想控制買進價格，要選？', ['限價', '市價', 'FOK 市價'], 0, '限價可以指定價格；市價跟對手方正在排隊的價格成交。'),
 ('Q5　10 萬元、每年 3%、複利 10 年，約多少？', ['約 11.0 萬元', '約 13.0 萬元', '約 13.4 萬元'], 2, '100,000 ×（1.03）^10 ≈ 134,392 元（假設報酬率）。'),
]
qhtml = ''.join('<div class="q" data-exp="' + e + '"><p class="qt">' + q + '</p>' + ''.join(f'<button type="button"{" data-ok=\"1\"" if k == ok else ""}>{o}</button>' for k, o in enumerate(opts)) + '<p class="exp"></p></div>' for q, opts, ok, e in QZ)
S.append(sec('quiz','小測驗',['slides:p5','slides:p10','slides:p11','slides:p15','slides:p18'],f'''    <p class="kicker">小測驗</p>
    <h2>五題，點選答案看解說</h2>
    <div class="quiz quiz5">{qhtml}</div>''','答案都在第 5、10、11、15、18 頁。'))
S.append(sec('recap','回顧',['notes:conclusion'],'''    <p class="kicker">重點回顧</p>
    <h2>今天記住三件事</h2>
    <div class="recap">
      <div><b>一</b><span>通膨讓錢變薄；先存預備金、還高利債，再談投資</span></div>
      <div><b>二</b><span>漲跌和昨收比；五檔看排隊；大盤不等於個股</span></div>
      <div><b>三</b><span>下單有成本，T+2 前要準備好錢</span></div>
    </div>''','看懂盤面是為了理解市場，不是為了猜明天。'))
pages = [('paths/beginner-invest-order.md','準備順序'),('concepts/inflation.md','通膨'),('concepts/compound-interest.md','複利'),('concepts/emergency-fund.md','緊急預備金'),('concepts/debt-first.md','先理債'),('concepts/quote-screen.md','報價畫面'),('concepts/k-line.md','K 線'),('concepts/order-book.md','五檔'),('concepts/market-index.md','大盤'),('rules/trading-hours.md','交易時間'),('rules/order-types.md','委託種類'),('rules/trading-costs.md','交易成本'),('rules/settlement-t2.md','T+2'),('concepts/default-settlement.md','違約交割')]
links = '、'.join(f'<a class="repo" data-path="wiki/{p}" href="{REPO}wiki/{p}">{n}</a>' for p, n in pages)
S.append(sec('ending','資料來源',['wiki/index.md'],f'''    <p class="kicker">資料來源</p>
    <p class="disclaimer">本內容僅供學習，不構成任何投資建議。</p>
    <ul class="dots">
      <li class="src">內容來自理財新手村 Wiki（19 個頁面、23 份來源）：{links}；<a class="repo" data-path="wiki/index.md" href="{REPO}wiki/index.md">全部目錄</a></li>
      <li class="src">制度數字為 2026 年規定，可能變動；標註 B 級者待法規確認</li>
      <li class="src">圖片為原創，報價與五檔為虛構範例</li>
    </ul>''','每一條資訊的出處都可以在 GitHub 上的 Wiki 查到。'))

# 名詞小卡：讀逐頁稿每頁的「術語」欄
md = open(f'{ROOT}/slides/{SLUG}.md', encoding='utf-8').read()
mdpages = re.split(r'^## 第 \d+ 頁[^\n]*\n', md, flags=re.M)[1:]
assert len(mdpages) == len(S), f'逐頁稿 {len(mdpages)} 頁、簡報 {len(S)} 頁'
for i, pg in enumerate(mdpages):
    m = re.search(r'^- 術語：(.*)$', pg, re.M)
    if m:
        items = ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in (x.split('＝', 1) for x in re.split(r'；(?=[^；＝]{1,8}＝)', m.group(1))))
        S[i] = S[i].replace('    <aside class="notes">', f'    <dl class="terms">{items}</dl>\n    <aside class="notes">', 1)

t = open(f'{ROOT}/decks/_template.html', encoding='utf-8').read()
start = t.index('<main>\n'); end = t.index('</main>', start) + len('</main>')
out = t[:start] + '<main>\n  <!-- 依據：slides/' + SLUG + '.md 第 2 版（每個 section 對應逐頁稿一頁） -->\n' + '\n'.join(S) + '\n</main>' + t[end:]
out = out.replace('{{簡報標題}}', '新手投資的第一課')
out = re.sub(r'<!--\n  理財新手村 HTML 簡報模板.*?-->\n', f'<!-- 理財新手村簡報｜由 decks/_template.html 複製；依據 slides/{SLUG}.md -->\n', out, count=1, flags=re.S)
out = out.replace('.quiz { display: grid; grid-template-columns: repeat(3, 1fr);', '.quiz { display: grid; grid-template-columns: repeat(3, 1fr);')
os.makedirs(f'{ROOT}/decks/{SLUG}', exist_ok=True)
open(f'{ROOT}/decks/{SLUG}/index.html', 'w', encoding='utf-8').write(out)
print('slides', len(S))
