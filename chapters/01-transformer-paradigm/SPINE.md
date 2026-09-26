# Spine — Chapter 1: The Transformer Paradigm (2017–2023)

**Source:** Packt Final Improved DOCX (`B38257_01_Packt_Final_Improved_v3`). Headings only — not the manuscript.

**Source class:** Packt DOCX (Ch1–3)

## Lead thesis (public companion)

Chapter 1 leads with an **inference scorecard** and the **four walls** — Prefill/Time, Memory, Bandwidth, Recall — applied across all four running examples (Efficient Scalar, Long-Context Agent, Structural Reasoner, Dynamic Streamer). **Invoice Impact** is only a pointer here; the before/after protocol starts in Chapter 3+ via [`examples/templates/invoice-impact.md`](../../examples/templates/invoice-impact.md).

## Headings

1. Technical requirements
2. Tracing How Transformers Won Training
   - Identifying the Three Properties Behind Transformer Dominance
   - Introducing the Reference Production Stack
   - Comparing the Inductive Biases of CNNs, RNNs, and Transformers
   - Deriving Scaled Dot-Product Attention
   - Mapping the Forward Pass Costs Stage by Stage
   - Framing the Transformer as the Measurement Baseline
   - Setting Up the Keep-Versus-Confront Framework
3. Generating Your First Inference Scorecard
   - Defining the Measurement Vocabulary
   - Comparing One Chip’s Two Speed Limits
   - Pinning the Worst Case
   - Running the Scorecard (Lab 1.2)
   - Applying the Same Card to a Small, Fast Model
   - Reading the Card: Ceiling Versus Reality
   - Mapping the Four Walls at a Glance
4. Deriving the Physics of Inference Costs
   - Deriving Equation 1: The Prefill Wall (Time)
   - Deriving Equation 2: The Memory Wall (Memory)
   - Deriving Equation 3: The Bandwidth Wall (Bandwidth)
   - Testing Wall 4: The Recall Test (the Cost No Equation Reports)
   - Consolidating the Four Results on One Page
5. Stress-Testing the Four Workloads
   - The Efficient Scalar: Wall 1 at Small Scale (Time)
   - The Long-Context Agent: Wall 3 When Live, Wall 1 When Cold (Bandwidth and Time)
   - The Structural Reasoner: Wall 4 (Recall)
   - The Dynamic Streamer: Wall 1 in a Real-Time Loop (Time)
   - Assembling the Master Matrix
6. Making the Scorecard Yours
   - Tracing the Chapter in One Thread
   - Applying What You Can Now Do
   - Testing Your Understanding with Seven Questions
   - Carrying It into Chapter 2
7. Summary
8. Further reading

## Technical requirements (distilled)

- Python 3.10+; PyTorch 2.1+ (CPU enough for accounting stubs)
- Examples under `examples/chapter-01/`
- Named scripts: `inference_accounting.py`, `nano_transformer.py`, `limit4_recall_demo.py`
- Install: `python -m pip install "torch>=2.1"`

## Named examples / scripts

- `examples/chapter-01/inference_accounting.py` — scorecard / wall arithmetic baseline
- `examples/chapter-01/nano_transformer.py` — tiny Attention measurement baseline
- `examples/chapter-01/limit4_recall_demo.py` — Wall 4 recall demo
- `examples/chapter-01/invoice_summary.py` — schema-compatible master-matrix rows (not Invoice Impact)

## Invoice Impact (pointer only)

Full before/after Invoice Impact protocol → Chapter 3+ and [`examples/templates/invoice-impact.md`](../../examples/templates/invoice-impact.md).
