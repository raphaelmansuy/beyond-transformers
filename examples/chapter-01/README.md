# Examples — Chapter 1

CPU-smoke stubs for the Chapter 1 **inference scorecard** and its **four walls** (prefill/time, memory, bandwidth, recall). The scorecard / master-matrix surface covers all four running workloads: Efficient Scalar, Long-Context Agent, Structural Reasoner, and Dynamic Streamer.

- `inference_accounting.py` — scorecard / wall arithmetic baseline stub.
- `nano_transformer.py` — tiny Transformer measurement baseline.
- `limit4_recall_demo.py` — Wall 4 recall check.
- `invoice_summary.py` — schema-compatible master-matrix rows for later concatenation (not Invoice Impact).

**Invoice Impact** (before/after vs this baseline) lives in Chapter 3+ — see [`../templates/invoice-impact.md`](../templates/invoice-impact.md).

Run from the repository root:

```bash
python examples/chapter-01/inference_accounting.py
python examples/chapter-01/nano_transformer.py
python examples/chapter-01/limit4_recall_demo.py
python examples/chapter-01/invoice_summary.py
```

Chapter guide and spine: [`chapters/01-transformer-paradigm/`](../../chapters/01-transformer-paradigm/).
