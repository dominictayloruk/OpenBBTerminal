---
title: load
description: This page provides detailed instructions on how to load a stock ticker
  to perform analysis, complete with usage examples and parameters. It also provides
  information on loading Indian tickers and references to data sources.
keywords:
- load stock ticker
- perform stock analysis
- Indian stock ticker
- stock analysis parameters
- stock data usage
- data source
- intraday stock minutes
- pre/after market hours
- load custom file
- monthly data
- weekly data
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="stocks/ta/load - Reference | OpenBB Terminal Docs" />

Load stock ticker to perform analysis on. When the data source is syf', an Indian ticker can be loaded by using '.NS' at the end, e.g. 'SBIN.NS'. See available market in https://help.yahoo.com/kb/exchanges-data-providers-yahoo-finance-sln2310.html.

### Usage

```python
load -t TICKER [-s START] [-e END] [-i {1,5,15,30,60}] [-p] [-f FILEPATH] [-m] [-w] [-r {ytd,1y,2y,5y,6m}]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| ticker | Stock ticker | None | False | None |
| start | The starting date (format YYYY-MM-DD) of the stock | 2019-11-21 | True | None |
| end | The ending date (format YYYY-MM-DD) of the stock | 2022-11-25 | True | None |
| interval | Intraday stock minutes | 1440 | True | 1, 5, 15, 30, 60 |
| prepost | Pre/After market hours. Only works for 'yf' source, and intraday data | False | True | None |
| filepath | Path to load custom file. | None | True | None |
| monthly | Load monthly data | False | True | None |
| weekly | Load weekly data | False | True | None |

---
