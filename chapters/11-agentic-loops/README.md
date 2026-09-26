# Chapter 11 — Agentic Loops & Hierarchical Planning

## What this chapter teaches

- Decision Mamba and sequence models as policies over trajectories.
- Hierarchical stack: **JEPA planner + EBM verifier + Mamba actor**.
- Closing the loop with the Long-Context Agent and Structural Reasoner.
- Budgeting compute across plan / verify / act.

## Example you build

A **hierarchical agent stub**: planner emits a latent plan, verifier scores candidates (energy stub), actor emits the next action token with a Mamba-style state — all toy interfaces, wired so readers see the control flow.

## How to run

```bash
python examples/chapter-11/jepa_ebm_mamba_agent.py   # stub
```
