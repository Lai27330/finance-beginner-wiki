---
type: rule
title: 委託種類：限價、市價與 ROD／IOC／FOK
summary: 下單時要選「什麼價格」和「掛多久」，共 6 種組合。
level: A
sources: [2018-10-31-continuous-trading-twse, 2026-11-23-continuous-trading-tpex]
updated: 2026-11-23
---

# 委託種類：限價、市價與 ROD／IOC／FOK

## 規定內容

| 項目 | 內容 | 適用年度 | 來源 |
|---|---|---|---|
| 價格類別 | 限價（自己指定價格）、市價（不指定價格，依對手方價格成交） | 2020 起（現行） | [證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md) |
| 有效期別 | ROD 當日有效；IOC 立即成交，沒成交的部分取消；FOK 全部成交，否則整筆取消 | 2020 起（現行） | [證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md) |
| 組合 | 2 種價格 × 3 種期別 ＝ 6 種 | 2020 起（現行） | [證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md) |
| 適用時段 | 開盤、收盤（集合競價）只能用限價 ROD；市價、IOC、FOK 只在盤中逐筆交易時段（開盤後至 13:25）可用 | 2026 | [證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)、[櫃買中心 逐筆交易](../sources/2026-11-23-continuous-trading-tpex.md) |
| 市價的撮合順序 | 市價委託優先於限價委託（含漲跌停價） | 2020 起（現行） | [證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md) |

## 白話解釋

- **限價**：「我最多出 100 元買」。不會用比 100 元貴的價格買到，但可能買不到。
- **市價**：「現在賣方開多少，我就買」。比較快成交，但成交價由當時委託簿上的賣方決定，不是你決定。（來源：[證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)、[櫃買中心 逐筆交易](../sources/2026-11-23-continuous-trading-tpex.md)）

- 除了「價格怎麼定」，下單時還要選「這張單要等多久」：
  - **ROD（當日有效）**：今天收盤前都有效，沒成交就繼續排隊。
  - **IOC（立即成交否則取消）**：能馬上成交多少就成交多少，剩下的立刻取消。
  - **FOK（全部成交否則取消）**：要嘛一次全部成交，要嘛整筆取消。
（來源：[證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)）

IOC 與 FOK 的例子（證交所說明）：你要買 50 張，賣方 100 元有 10 張、101 元有 20 張。
- 用 **IOC**：先買到 30 張，剩下 20 張取消。
- 用 **FOK**：沒辦法一次買滿 50 張，整筆取消。
（來源：[證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)）

## 一張委託單要決定什麼（下單步驟）

1. **買或賣**。
2. **整股或零股**：整股以「張」為單位（1 張＝1,000 股），零股以「股」為單位；零股只能用限價、ROD。（來源：[證交所 盤中零股](../sources/2023-12-01-odd-lot-twse.md)）
3. **價格怎麼定**：限價（填價格）或市價。（來源：[證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)）
4. **數量**：幾張或幾股。
5. **這張單要等多久**：ROD、IOC 或 FOK。（來源：[證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)）

送出後，依「價格優先、時間優先」跟對手方排隊的單成交（見[五檔報價](../concepts/order-book.md)）；成交後要付交易成本，並在 T+2 交割（見[交易成本](trading-costs.md)、[T+2 交割](settlement-t2.md)）。

## 新手常見問題

- 新手該選哪一種？→ 本 Wiki 不做建議。可以先理解：限價能控制價格、可能買不到；市價成交快、價格不由自己決定。

## 相關頁面

- [五檔報價](../concepts/order-book.md)、[漲跌幅限制](price-limit.md)、[T+2 交割](settlement-t2.md)

## 來源

- [證交所 逐筆交易說明](../sources/2018-10-31-continuous-trading-twse.md)
- [櫃買中心 逐筆交易](../sources/2026-11-23-continuous-trading-tpex.md)
