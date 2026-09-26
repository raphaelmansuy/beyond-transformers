# Chapter 3 — Modern Recurrent Neural Networks

Spine: [`SPINE.md`](SPINE.md) (from Packt DOCX headings).

## What this chapter teaches

- Why gated linear recurrence returned under serving pressure.
- First-principles gated state updates; xLSTM and RWKV-7 Goose at production depth.
- Parallel training vs efficient decode (kernels, CUDA Graphs, state persistence).
- Rebuilding **Efficient Scalar** and recording Invoice Impact vs Chapter 1.

## Example you build

Gated recurrence module + tests + invoice benchmark harness for Efficient Scalar.

## How to run

```bash
python examples/chapter-03/kv_cache_estimate.py       # stub
python examples/chapter-03/gated_recurrence.py        # stub
python examples/chapter-03/test_gated_recurrence.py   # stub
python examples/chapter-03/invoice_benchmark.py       # stub
```

## Key refs

- RWKV — arXiv:2305.13048
- xLSTM — arXiv:2405.04517
