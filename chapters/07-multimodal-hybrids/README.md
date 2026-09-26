# Chapter 7 — Multimodal Hybrids

## What this chapter teaches

- Extending SSM/hybrid backbones to vision and audio streams.
- Patterns in **MambaVision** and **VAMBA**-style designs.
- Real-time constraints: frame rate, buffering, and state carry-over.
- Mapping multimodal hybrids onto **Dynamic Streamer**.

## Example you build

**Dynamic Streamer (60 fps stub)** — a placeholder loop that “ingests” synthetic frame tokens at a target rate, updates a multimodal state, and logs backlog when the budget is exceeded. No real video model weights required.

## How to run

```bash
python examples/chapter-07/dynamic_streamer_60fps.py   # stub
```
