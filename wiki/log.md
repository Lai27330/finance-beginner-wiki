---
type: log
title: Wiki 日誌
---

# Wiki 日誌

> 只能往後新增。查最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

## [2026-11-22] schema | 建立 AGENTS.md 初版
- 架構、來源分級、頁面格式、流程圖 G0～G5、教學簡報結構、理財安全規則

## [2026-11-22] run | 開始執行 invest-order-and-quotes
- N0 討論完成，學習目標 5 條經人類確認（runs/2026-11-22-invest-order-and-quotes.md）

## [2026-11-22] ingest | 第 1 輪 8 份來源
- raw：A 級 4 份（證交所、櫃買中心、證交稅條例、金管會防詐）、B 級 4 份（經理人、工商時報、女人迷、Smart）
- 新增：paths 1、concepts 6、rules 4、sources 8、index、overview
- 讀取失敗：4 份網頁 WebFetch 失敗，改用搜尋摘要，已在 raw 的「擷取限制」註明
- 待補：成交量與五檔、零股交易時間（新制 2026-12-07）、ETF 證交稅 A 級來源、卡債利率上限

## [2026-11-22] lint | G2 檢查
- 第 1 次不通過 3 項：禁用詞誤判 2 處（防詐頁）、制度頁使用 B 級來源 1 處（交易成本）
- 修正後第 2 次通過；手續費與 ETF 稅率改列待補

## [2026-11-22] ingest | Loop 1 第 2 輪：經濟日報 零股新制
- 新增：raw/articles/2026-08-21-odd-lot-new-rule-udn.md、sources 1 頁
- 更新：rules/trading-hours.md（新增「即將變動」）、index
- A3、A7、B8（成交量定義）讀取失敗，等待人類剪存

## [2026-11-22] ingest | Loop 1 第 3 輪：人類剪存 3 份
- 新增 raw：2023-12-01-odd-lot-twse（A）、2026-11-22-broker-fee-twse60（A）、2026-11-22-volume-uptogo（B，只取定義）
- 更新：rules/trading-hours、trading-unit、trading-costs；concepts/quote-screen；sources 3 頁；index；overview
- 發現：手續費 1.425‰ 不是絕對上限（2008 年起超過須通知），已寫入「不同觀點」

## [2026-11-22] note | 研究筆記 Loop 1 後重寫，G3 通過
- 5 條學習目標都有支撐，Loop 1 結束

## [2026-11-23] slides | 逐頁稿 15 頁，G4 第 2 次通過

## [2026-11-23] deck | 簡報草稿（清爽日式・藍綠色），G5 第 2 次通過，待人類確認

## [2026-11-23] schema | 用語：K 線一律稱「紅 K／綠 K」
- 人類要求簡報不出現「黑 K」；Wiki 的 K 線頁保留一次正式名稱說明

## [2026-11-23] ingest | Loop 2 第 3 輪 7 份來源
- raw：A13 證交所逐筆交易、A14 櫃買中心逐筆交易、A15 期交所加權指數、A16 證交所 T+2（人類剪存）、B9 工商時報、B10 經理人、B11 股感
- 新增：rules/settlement-t2、rules/order-types、concepts/order-book、default-settlement、market-index、compound-interest、inflation；sources 7
- 更新：k-line（綠 K）、quote-screen、paths、trading-unit、emergency-fund、index、overview

## [2026-11-23] note | 研究筆記第 2 版（7 條目標），G3 通過

## [2026-11-23] slides | 逐頁稿第 2 版 21 頁，G4 第 4 次通過

## [2026-11-23] deck | 簡報第 2 版（互動元件），G5 第 5 次通過（GitHub 連結待填）

## [2026-11-23] site | 簡報模板新增互動元件與五題版測驗排版

## [2026-11-23] schema | 依執行結果修訂流程（人類同意）
- G1 試讀；G0／G3／G4 學習深度；G2 概念頁 B 級制度數字；G5 瀏覽器實際執行；禁用詞「」豁免；風格與名稱定案

## [2026-11-23] lint | 人類複核證交所與櫃買中心原網頁，內容一致

## [2026-11-23] deck | 封面改版、看答案按鈕可切換；G5 通過（GitHub 連結待填）

## [2026-11-23] ingest | 新增名詞小辭典 glossary.md；五檔、大盤、委託種類、T+2 頁補白話說明

## [2026-11-23] deck | 第 3 次人類審閱後：逐頁稿加術語欄、第 14 頁拆成兩頁（22 頁）、簡報顯示名詞小卡；G2～G5 通過（GitHub 連結待填）

## [2026-11-23] ingest | 第 4 輪來源 C1～C4（大盤對個人的影響、ETF 定義）；委託種類頁新增下單步驟

## [2026-11-23] deck | 第 4 次人類審閱後：大盤拆兩頁、新增模擬下單，共 24 頁；G2～G5 通過（GitHub 連結待填）

## [2026-11-23] deck | 第 5 次人類審閱後：模擬下單支援零股（集合競價、最低手續費）；G5 版面檢查改量元素邊界並檢查互動狀態
