---
title: "symbol_map"
description: "Retrieve the ticker symbol corresponding to a company CIK using the  OBB API endpoint. This function allows you to perform a search query and get the  results along with additional metadata, warnings, and optional chart data."
keywords:
- ticker symbol
- CIK
- company
- ticker mapping
- search query
- provider
- results
- warnings
- chart
- metadata
- data
- symbol
- entity
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="regulators/sec/symbol_map - Reference | OpenBB Platform Docs" />

<!-- markdownlint-disable MD012 MD031 MD033 -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Map a CIK number to a ticker symbol, leading 0s can be omitted or included.


Examples
--------

```python
from openbb import obb
obb.regulators.sec.symbol_map(query='0000789019', provider='sec')
```

---

## Parameters

<Tabs>

<TabItem value='standard' label='standard'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| query | str | Search query. |  | False |
| use_cache | bool | Whether or not to use cache. If True, cache will store for seven days. | True | True |
| provider | Literal['sec'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'sec' if there is no default. | sec | True |
</TabItem>

<TabItem value='sec' label='sec'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| query | str | Search query. |  | False |
| use_cache | bool | Whether or not to use cache. If True, cache will store for seven days. | True | True |
| provider | Literal['sec'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'sec' if there is no default. | sec | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : SymbolMap
        Serializable results.
    provider : Literal['sec']
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

</TabItem>

<TabItem value='sec' label='sec'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| symbol | str | Symbol representing the entity requested in the data. |
</TabItem>

</Tabs>
