---
title: bigmac
description: This page provides documentation for the Big Mac Index functionality
  in OpenBB. It includes details on how to use the 'bigmac' function and its parameters,
  along with source code links and return information. This information is useful
  for individuals looking to utilize the OpenBB economic dataset for data analysis.
keywords:
- bigmac
- docusaurus
- Big Mac Index
- economy
- country_codes
- dataframe
- matplotlib
- USD equivalent
- parameters
- returns
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="economy.bigmac - Reference | OpenBB SDK Docs" />

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="model" label="Model" default>

Display Big Mac Index for given countries

Source Code: [[link](https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/economy/nasdaq_model.py#L183)]

```python
openbb.economy.bigmac(country_codes: List[str] = None)
```

---

## Parameters

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| country_codes | List[str] | List of country codes (ISO-3 letter country code). Codes available through economy.country_codes(). | None | True |


---

## Returns

| Type | Description |
| ---- | ----------- |
| pd.DataFrame | Dataframe with Big Mac indices converted to USD equivalent. |
---

</TabItem>
<TabItem value="view" label="Chart">

Display Big Mac Index for given countries

Source Code: [[link](https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/economy/nasdaq_view.py#L59)]

```python
openbb.economy.bigmac_chart(country_codes: List[str] = None, raw: bool = False, export: str = "", external_axes: Optional[List[matplotlib.axes._axes.Axes]] = None)
```

---

## Parameters

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| country_codes | List[str] | List of country codes (ISO-3 letter country code). Codes available through economy.country_codes(). | None | True |
| raw | bool | Flag to display raw data, by default False | False | True |
| export | str | Format data, by default "" |  | True |
| external_axes | Optional[List[plt.Axes]] | External axes (1 axis is expected in the list), by default None | None | True |


---

## Returns

This function does not return anything

---

</TabItem>
</Tabs>
