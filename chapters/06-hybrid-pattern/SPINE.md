# Spine — Chapter 6: The Hybrid Pattern (Attention ⊕ State)

**Source:** Book outline V11 (Notion: Book outline). Packt DOCX not yet attached for this chapter.

**Source class:** outline-only

## Headings (outline V11)

- Samba & Griffin: sliding-window hybrids
- Architectural Placement: early / middle / late Attention
- Memory Management: KV-cache ⊕ recurrent state
- Implementation: Hybrid Long-Context Agent

## Invoice Impact

Hybrid Agent — decode HBM (GiB) + recall @ 128k vs **8B GQA-8** Transformer and pure SSM. Do not invent timings.

## Named example stubs

- `examples/chapter-06/hybrid_long_context_agent.py`
