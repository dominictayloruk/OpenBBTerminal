---
title: "Index Historical"
description: "Historical Index Levels"
---

<!-- markdownlint-disable MD012 MD031 MD033 -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

---

## Implementation details

### Class names

| Model name | Parameters class | Data class |
| ---------- | ---------------- | ---------- |
| `IndexHistorical` | `IndexHistoricalQueryParams` | `IndexHistoricalData` |

### Import Statement

```python
from openbb_core.provider.standard_models.index_historical import (
IndexHistoricalData,
IndexHistoricalQueryParams,
)
```

---

## Parameters

<Tabs>

<TabItem value='standard' label='standard'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| interval | str | Time interval of the data to return. | 1d | True |
| provider | Literal['cboe', 'fmp', 'intrinio', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
</TabItem>

<TabItem value='cboe' label='cboe'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| interval | str | Time interval of the data to return. | 1d | True |
| provider | Literal['cboe', 'fmp', 'intrinio', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
| use_cache | bool | When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass. | True | True |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| interval | str | Time interval of the data to return. | 1d | True |
| provider | Literal['cboe', 'fmp', 'intrinio', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
</TabItem>

<TabItem value='intrinio' label='intrinio'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| interval | str | Time interval of the data to return. | 1d | True |
| provider | Literal['cboe', 'fmp', 'intrinio', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
| limit | int | The number of data entries to return. | 10000 | True |
</TabItem>

<TabItem value='polygon' label='polygon'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| interval | str | Time interval of the data to return. | 1d | True |
| provider | Literal['cboe', 'fmp', 'intrinio', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
| sort | Literal['asc', 'desc'] | Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date. | asc | True |
| limit | int | The number of data entries to return. | 49999 | True |
</TabItem>

<TabItem value='yfinance' label='yfinance'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. Multiple items allowed for provider(s): cboe, fmp, intrinio, polygon, yfinance. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| interval | str | Time interval of the data to return. | 1d | True |
| provider | Literal['cboe', 'fmp', 'intrinio', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
</TabItem>

</Tabs>

---

## Data

<Tabs>

<TabItem value='standard' label='standard'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | Union[date, datetime] | The date of the data. |
| open | float, Strict(strict=True) | The open price. |
| high | float, Strict(strict=True) | The high price. |
| low | float, Strict(strict=True) | The low price. |
| close | float, Strict(strict=True) | The close price. |
| volume | int | The trading volume. |
</TabItem>

<TabItem value='cboe' label='cboe'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | Union[date, datetime] | The date of the data. |
| open | float, Strict(strict=True) | The open price. |
| high | float, Strict(strict=True) | The high price. |
| low | float, Strict(strict=True) | The low price. |
| close | float, Strict(strict=True) | The close price. |
| volume | int | The trading volume. |
| calls_volume | float | Number of calls traded during the most recent trading period. Only valid if interval is 1m. |
| puts_volume | float | Number of puts traded during the most recent trading period. Only valid if interval is 1m. |
| total_options_volume | float | Total number of options traded during the most recent trading period. Only valid if interval is 1m. |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | Union[date, datetime] | The date of the data. |
| open | float, Strict(strict=True) | The open price. |
| high | float, Strict(strict=True) | The high price. |
| low | float, Strict(strict=True) | The low price. |
| close | float, Strict(strict=True) | The close price. |
| volume | int | The trading volume. |
| vwap | float | Volume Weighted Average Price over the period. |
| change | float | Change in the price from the previous close. |
| change_percent | float | Change in the price from the previous close, as a normalized percent. |
</TabItem>

<TabItem value='intrinio' label='intrinio'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | Union[date, datetime] | The date of the data. |
| open | float, Strict(strict=True) | The open price. |
| high | float, Strict(strict=True) | The high price. |
| low | float, Strict(strict=True) | The low price. |
| close | float, Strict(strict=True) | The close price. |
| volume | int | The trading volume. |
</TabItem>

<TabItem value='polygon' label='polygon'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | Union[date, datetime] | The date of the data. |
| open | float, Strict(strict=True) | The open price. |
| high | float, Strict(strict=True) | The high price. |
| low | float, Strict(strict=True) | The low price. |
| close | float, Strict(strict=True) | The close price. |
| volume | int | The trading volume. |
| transactions | int, Gt(gt=0) | Number of transactions for the symbol in the time period. |
</TabItem>

<TabItem value='yfinance' label='yfinance'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | Union[date, datetime] | The date of the data. |
| open | float, Strict(strict=True) | The open price. |
| high | float, Strict(strict=True) | The high price. |
| low | float, Strict(strict=True) | The low price. |
| close | float, Strict(strict=True) | The close price. |
| volume | int | The trading volume. |
</TabItem>

</Tabs>
