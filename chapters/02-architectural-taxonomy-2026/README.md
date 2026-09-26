# Chapter 2 — The Architectural Taxonomy of 2026

Spine: [`SPINE.md`](SPINE.md) (Packt DOCX headings extract).

## What you learn

- Three inference paradigms (buckets): **Generative**, **Predictive**, and **Energy-Based**.
- How to read throughput / quality / recall claims and spot the four anti-patterns.
- **Compression vs retrieval** as the central design axis (state vs attention / KV consequence).
- How to **route** all four running examples (Efficient Scalar, Long-Context Agent, Structural Reasoner, Dynamic Streamer) and diagnose a mis-route.

## What you build

- KV-consequence arithmetic stub (`kv_cache.py`) and a routing / triage CLI stub (`triage.py`).
- Decision notes in [`examples/architecture-decision-framework.md`](../../examples/architecture-decision-framework.md).

## How to run

```bash
python examples/chapter-02/kv_cache.py   # stub
python examples/chapter-02/triage.py     # stub
```

See [`SPINE.md`](SPINE.md) for the full heading spine.
