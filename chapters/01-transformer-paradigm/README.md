# Chapter 1 — The Transformer Paradigm (2017–2024)

Spine: [`SPINE.md`](SPINE.md) (from Packt DOCX headings).

## What this chapter teaches

- Why Transformers won training (inductive bias, hardware lottery, prefill vs decode).
- How to build an **inference scorecard** and name the four walls: time, memory, bandwidth, recall.
- Physics of inference costs for the Chapter 1 baseline.
- Stress-tests on the four running examples (Scalar, Agent, Reasoner, Streamer).
- The **Invoice Impact** baseline used from Chapter 3 onward.

## Example you build

Scorecard + recall demo against a tiny Transformer (`nano_transformer.py`), then fill Invoice Impact rows (`invoice_summary.py`). See spine for section order.

## How to run

```bash
python examples/chapter-01/nano_transformer.py      # stub
python examples/chapter-01/limit4_recall_demo.py    # stub
python examples/chapter-01/invoice_summary.py       # stub
```

## Key refs

- Attention Is All You Need — arXiv:1706.03762
