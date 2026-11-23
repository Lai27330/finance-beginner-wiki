---
type: rule
title: T+2 交割
summary: 買股票的錢，在成交後第 2 個營業日上午 10 點前扣款。
level: A
sources: [2009-01-01-dvp-settlement-twse, 2026-11-22-trading-system-tpex]
updated: 2026-11-23
---

# T+2 交割

## 規定內容

| 項目 | 內容 | 適用年度 | 來源 |
|---|---|---|---|
| T、T+1、T+2 | T＝成交日；T+1＝成交日次一營業日；T+2＝成交日次二營業日 | 2009 起（現行） | [證交所 T+2 交割](../sources/2009-01-01-dvp-settlement-twse.md) |
| 投資人付款／交券期限 | T+2 日上午 10 時前 | 2009 起（現行） | [證交所 T+2 交割](../sources/2009-01-01-dvp-settlement-twse.md) |
| 取得股票或賣出的價款 | T+2 日上午 11 時後 | 2009 起（現行） | [證交所 T+2 交割](../sources/2009-01-01-dvp-settlement-twse.md) |

## 白話解釋

下單成交那天（T）不會扣錢。要在成交後第 2 個**營業日**上午 10 點前，把錢放進交割帳戶。週末和休市日不算營業日。

交割帳戶是開戶時一起開立、綁定的銀行帳戶（官方稱款項劃撥帳戶），買股票從這裡扣款，賣股票的錢也會匯到這裡。（來源：[櫃買中心 交易系統](../sources/2026-11-22-trading-system-tpex.md)、[證交所 T+2 交割](../sources/2009-01-01-dvp-settlement-twse.md)）

例子（假設日期）：週四成交 → 週五是 T+1 → 下週一是 T+2，上午 10 點前要有錢。

## 新手常見問題

- 下單當下帳戶沒錢，會不會被擋下來？→ 成交當天不扣款，所以一定要自己確認 T+2 前錢夠。錢不夠的後果見[違約交割](../concepts/default-settlement.md)。

## 相關頁面

- [違約交割](../concepts/default-settlement.md)、[交易成本](trading-costs.md)、[委託種類](order-types.md)

## 來源

- [證交所 T+2 交割](../sources/2009-01-01-dvp-settlement-twse.md)
- [櫃買中心 交易系統](../sources/2026-11-22-trading-system-tpex.md)
