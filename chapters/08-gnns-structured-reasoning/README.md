# Chapter 8 — GNNs & Structured Reasoning

## What this chapter teaches

- The **Structure Gap**: flat sequences vs relational constraints.
- ConstraintLLM-style ideas: decoding under graph / schema constraints.
- Combining message passing with language backbones.
- The **Structural Reasoner** + knowledge graph (KG) running example.

## Example you build

**Structural Reasoner + KG** — a stub that loads a tiny toy graph, runs one GNN-style message-pass layer, and filters LLM-like candidate answers that violate edges (rule-based filter only).

## How to run

```bash
python examples/chapter-08/structural_reasoner_kg.py   # stub
```
