---
title: zlma
description: The zlma page provides an in-depth understanding of the zero lag exponential
  moving average (ZLEMA), with insight into its usage, parameters such as 'n_length'
  and 'n_offset', and a usage example. This indicator was created by John Ehlers and
  Ric Way and the page neatly explains the concept with visual aids.
keywords:
- zlma
- zero lag exponential moving average
- John Ehlers
- Ric Way
- exponential moving average
- EMA
- de-lagged data
- moving average
- n_length
- n_offset
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="stocks/ta/zlma - Reference | OpenBB Terminal Docs" />

The zero lag exponential moving average (ZLEMA) indicator was created by John Ehlers and Ric Way. The idea is do a regular exponential moving average (EMA) calculation but on a de-lagged data instead of doing it on the regular data. Data is de-lagged by removing the data from "lag" days ago thus removing (or attempting to) the cumulative effect of the moving average.

### Usage

```python
zlma [-l N_LENGTH] [-o N_OFFSET]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| n_length | Window lengths. Multiple values indicated as comma separated values. | 20 | True | None |
| n_offset | offset | 0 | True | None |

![zlma](https://user-images.githubusercontent.com/46355364/154312786-bc60268b-9da9-4fd9-bed6-fc95f5560075.png)

---
