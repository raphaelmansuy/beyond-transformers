# Chapter 1 — The Transformer Paradigm (2017–2023)

## What this chapter teaches

- Why Attention became the default for sequence modeling (2017–2023).
- The physics of Attention: QKV, softmax, and quadratic cost in sequence length.
- The **KV-cache wall**: memory and latency limits at long context.
- The four running examples you will reuse: Efficient Scalar, Long-Context Agent, Structural Reasoner, Dynamic Streamer.
- How **Invoice Impact** records before/after cost–latency–quality vs this baseline.

## Example you build

**Baseline Transformer stubs** for Efficient Scalar and Long-Context Agent, plus an Invoice Impact note using [`examples/templates/invoice-impact.md`](../../examples/templates/invoice-impact.md). Scripts demonstrate a tiny Attention block and a placeholder KV-cache size estimate — not production training.

## How to run

```bash
python examples/chapter-01/baseline_attention.py   # stub
python examples/chapter-01/kv_cache_estimate.py     # stub
```

## Key refs

- Attention Is All You Need — arXiv:1706.03762
