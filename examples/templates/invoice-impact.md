# Invoice Impact template (Chapter 3+)

This is the **Chapter 3+** before/after protocol. Chapter 1 leads with the **inference scorecard** and the **four walls** (prefill/time, memory, bandwidth, recall). Do not use “Invoice Impact” as the Chapter 1 lead phrase.

From Chapter 3 onward, copy this schema when a candidate is compared to the Chapter 1 Transformer scorecard baseline (**8B GQA-8**) on the running examples.

## Protocol

1. Same **N**, same **GPU class**, and **precision disclosed** for baseline and candidate. The Chapter 1 Transformer scorecard preset is **8B GQA-8** (do not silently swap in 7B).
2. Four workload columns. **Efficient Scalar** and **Long-Context Agent** are required. **Structural Reasoner** and **Dynamic Streamer** are optional — keep the columns; empty cells are OK.
3. Every numeric or result cell must be labelled `modelled` | `measured` | `reproduced` | `reproduced-from-source`. Stubs stay empty. Do not invent numbers. Companion memory units are **GiB** (2³⁰). Paper “GB” only in cells labelled `reproduced-from-source`.
4. State models must include the **MQAR** honesty row (use **RULER** for hybrids). Perplexity-only success is not allowed.
5. Packt-safe: no customer or company names.

Filled-cell format: `<value> · <label>`.

## Run card

| Field | Value |
|-------|-------|
| Chapter / architecture | |
| Baseline | Chapter 1 Transformer scorecard (**8B GQA-8**) |
| N | |
| GPU class | |
| Precision | |
| Companion script | `examples/chapter-NN/…` |

## Invoice schema

| Metric | Efficient Scalar (required) | Long-Context Agent (required) | Structural Reasoner (optional) | Dynamic Streamer (optional) |
|--------|----------------------------|-------------------------------|--------------------------------|-----------------------------|
| Prefill / time (baseline) | | | | |
| Prefill / time (candidate) | | | | |
| Memory / GiB (baseline) | | | | |
| Memory / GiB (candidate) | | | | |
| Bandwidth (baseline) | | | | |
| Bandwidth (candidate) | | | | |
| Recall (baseline) | | | | |
| Recall (candidate) | | | | |
| MQAR / RULER (honesty) | | | | |

**Honesty:** MQAR for state models; RULER when the candidate is a hybrid. A PPL-only row is not a success criterion.

Link the chapter README and the script under `examples/chapter-NN/` when you fill a card.
