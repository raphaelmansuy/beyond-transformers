# Chapter 1 — The Transformer Paradigm (2017–2023)

Spine: [`SPINE.md`](SPINE.md) (Packt DOCX headings extract).

## What you learn

- How to build and read an **inference scorecard**: vocabulary, chip speed limits, ceiling vs observed reality.
- The **four walls** of inference — **prefill/time**, **memory**, **bandwidth**, and **recall** — derived as the physics of cost.
- Why the Transformer is the measurement baseline (training-era properties → stage-by-stage forward-pass cost).
- How to stress-test the **same scorecard** on all four running workloads: **Efficient Scalar**, **Long-Context Agent**, **Structural Reasoner**, and **Dynamic Streamer**.

## What you build

- Scorecard / wall accounting stub (`inference_accounting.py`) plus a tiny Transformer baseline (`nano_transformer.py`).
- Master-matrix row stubs covering all four workloads (`invoice_summary.py` — schema only).
- Wall-4 recall smoke check (`limit4_recall_demo.py`).

**Invoice Impact** is not a Chapter 1 deep dive. Use the Ch3+ template at [`examples/templates/invoice-impact.md`](../../examples/templates/invoice-impact.md) when later chapters rebuild a workload against this baseline.

All example scripts are intentionally stubs for now; they remain CPU-smoke runnable.

## How to run

From the repository root:

```bash
python examples/chapter-01/inference_accounting.py
python examples/chapter-01/nano_transformer.py
python examples/chapter-01/limit4_recall_demo.py
python examples/chapter-01/invoice_summary.py
```

See [`SPINE.md`](SPINE.md) for the section order and source headings.

## Key refs

- Attention Is All You Need — arXiv:1706.03762
