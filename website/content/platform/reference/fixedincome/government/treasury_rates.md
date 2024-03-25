---
title: "treasury_rates"
description: "Government Treasury Rates"
keywords:
- fixedincome
- government
- treasury_rates
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="fixedincome/government/treasury_rates - Reference | OpenBB Platform Docs" />

<!-- markdownlint-disable MD012 MD031 MD033 -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Government Treasury Rates.


Examples
--------

```python
from openbb import obb
obb.fixedincome.government.treasury_rates(provider='fmp')
```

---

## Parameters

<Tabs>

<TabItem value='standard' label='standard'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| provider | Literal['federal_reserve', 'fmp'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'federal_reserve' if there is no default. | federal_reserve | True |
</TabItem>

<TabItem value='federal_reserve' label='federal_reserve'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| provider | Literal['federal_reserve', 'fmp'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'federal_reserve' if there is no default. | federal_reserve | True |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| provider | Literal['federal_reserve', 'fmp'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'federal_reserve' if there is no default. | federal_reserve | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : TreasuryRates
        Serializable results.
    provider : Literal['federal_reserve', 'fmp']
        Provider name.
    warnings : Optional[List[Warning_]]
        List of warnings.
    chart : Optional[Chart]
        Chart object.
    extra : Dict[str, Any]
        Extra info.

```

---

## Data

<Tabs>

<TabItem value='standard' label='standard'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | date | The date of the data. |
| week_4 | float | 4 week Treasury bills rate (secondary market). |
| month_1 | float | 1 month Treasury rate. |
| month_2 | float | 2 month Treasury rate. |
| month_3 | float | 3 month Treasury rate. |
| month_6 | float | 6 month Treasury rate. |
| year_1 | float | 1 year Treasury rate. |
| year_2 | float | 2 year Treasury rate. |
| year_3 | float | 3 year Treasury rate. |
| year_5 | float | 5 year Treasury rate. |
| year_7 | float | 7 year Treasury rate. |
| year_10 | float | 10 year Treasury rate. |
| year_20 | float | 20 year Treasury rate. |
| year_30 | float | 30 year Treasury rate. |
</TabItem>

<TabItem value='federal_reserve' label='federal_reserve'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | date | The date of the data. |
| week_4 | float | 4 week Treasury bills rate (secondary market). |
| month_1 | float | 1 month Treasury rate. |
| month_2 | float | 2 month Treasury rate. |
| month_3 | float | 3 month Treasury rate. |
| month_6 | float | 6 month Treasury rate. |
| year_1 | float | 1 year Treasury rate. |
| year_2 | float | 2 year Treasury rate. |
| year_3 | float | 3 year Treasury rate. |
| year_5 | float | 5 year Treasury rate. |
| year_7 | float | 7 year Treasury rate. |
| year_10 | float | 10 year Treasury rate. |
| year_20 | float | 20 year Treasury rate. |
| year_30 | float | 30 year Treasury rate. |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | date | The date of the data. |
| week_4 | float | 4 week Treasury bills rate (secondary market). |
| month_1 | float | 1 month Treasury rate. |
| month_2 | float | 2 month Treasury rate. |
| month_3 | float | 3 month Treasury rate. |
| month_6 | float | 6 month Treasury rate. |
| year_1 | float | 1 year Treasury rate. |
| year_2 | float | 2 year Treasury rate. |
| year_3 | float | 3 year Treasury rate. |
| year_5 | float | 5 year Treasury rate. |
| year_7 | float | 7 year Treasury rate. |
| year_10 | float | 10 year Treasury rate. |
| year_20 | float | 20 year Treasury rate. |
| year_30 | float | 30 year Treasury rate. |
</TabItem>

</Tabs>
