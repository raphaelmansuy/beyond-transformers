# Chapter 3 — Modern Recurrent Neural Networks (The Gated Linear Pattern)

Spine: [`SPINE.md`](SPINE.md) (Packt DOCX headings extract).

## What you learn

- Why gated linear recurrence returned under serving pressure (vs attention KV growth).
- First-principles gated state updates; **xLSTM** (sLSTM / mLSTM) and **RWKV-7 Goose** at production depth.
- Parallel training vs efficient decode (kernels, CUDA Graphs, state persistence / reset).
- Rebuilding **Efficient Scalar** and recording **Invoice Impact** against the Chapter 1 scorecard baseline.

## What you build

- Gated recurrence reference + tests (`gated_recurrence.py`, `test_gated_recurrence.py`).
- KV-vs-state estimate (`kv_cache_estimate.py`) and an invoice benchmark harness (`invoice_benchmark.py`).

Invoice Impact template: [`examples/templates/invoice-impact.md`](../../examples/templates/invoice-impact.md).

## How to run

```bash
python examples/chapter-03/kv_cache_estimate.py
python examples/chapter-03/gated_recurrence.py
python examples/chapter-03/test_gated_recurrence.py
python examples/chapter-03/invoice_benchmark.py
```

## Key refs

- RWKV — arXiv:2305.13048
- xLSTM — arXiv:2405.04517
