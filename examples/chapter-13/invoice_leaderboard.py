"""Chapter 13 — Invoice Impact leaderboard schema (CPU-smoke).

Meta-table that conceptually aggregates Chapters 3–12 Invoice Impact
rows versus the Chapter 1 Transformer scorecard (8B GQA-8). Companion
memory units are GiB (2**30). This smoke prints the labelled schema
only — fills stay empty. Do not invent timings or SOTA tables.

Every cell label is one of: modelled | measured | reproduced-from-source | stub
"""

from __future__ import annotations

from collections.abc import Sequence

LABELS = ("modelled", "measured", "reproduced-from-source", "stub")
PRESET = "8B GQA-8"
MEMORY_UNIT = "GiB"  # 2**30 bytes; paper "GB" only in reproduced-from-source cells
GIB_BYTES = 2**30

REQUIRED_WORKLOADS = ("Efficient Scalar", "Long-Context Agent")
OPTIONAL_WORKLOADS = ("Structural Reasoner", "Dynamic Streamer")
WORKLOAD_HEADERS = (
    "Efficient Scalar (required)",
    "Long-Context Agent (required)",
    "Structural Reasoner (optional)",
    "Dynamic Streamer (optional)",
)
WALL_METRICS = (
    "Prefill / time (baseline)",
    "Prefill / time (candidate)",
    "Memory / GiB (baseline)",
    "Memory / GiB (candidate)",
    "Bandwidth (baseline)",
    "Bandwidth (candidate)",
    "Recall (baseline)",
    "Recall (candidate)",
    "MQAR / RULER (honesty)",
)

# Conceptual Ch3–12 Invoice rows. Fills stay empty.
CHAPTER_ROWS: tuple[tuple[int, str, str], ...] = (
    (3, "Modern RNNs", "state"),
    (4, "State Space Models", "state"),
    (5, "Comparative Dynamics", "state"),
    (6, "Hybrid Pattern", "hybrid"),
    (7, "Multimodal Hybrids", "hybrid"),
    (8, "GNNs & Structured Reasoning", "other"),
    (9, "Energy-Based Models", "other"),
    (10, "World Models & JEPA", "other"),
    (11, "Agentic Loops", "hybrid"),
    (12, "Extreme Compression", "state"),
)

# Illustrative / source notes — not companion measurements.
NEEDLE_IDENTITY = "5,401"
BI_MAMBA_PAPER_PCT = "50.6%"
BI_MAMBA_ARXIV = "arXiv:2411.11843"


def labelled(value: str, label: str) -> str:
    """Return `<value> · <label>`, or just the label when the value is empty."""
    if label not in LABELS:
        raise ValueError(f"label must be one of {LABELS}, got {label!r}")
    text = value.strip()
    return f"{text} · {label}" if text else label


def empty_stub() -> str:
    return labelled("", "stub")


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    cols = list(headers)
    body = [list(row) for row in rows]
    if any(len(row) != len(cols) for row in body):
        raise ValueError("each row must match the header width")
    widths = [len(col) for col in cols]
    for row in body:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def fmt(cells: Sequence[str]) -> str:
        return "| " + " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells)) + " |"

    rule = "| " + " | ".join("-" * width for width in widths) + " |"
    return "\n".join((fmt(cols), rule, *(fmt(row) for row in body)))


def run_card_rows() -> list[list[str]]:
    stub = empty_stub()
    return [
        ["Chapter / architecture", "13 meta-table (aggregates Ch3–12)", stub],
        ["Baseline", f"Chapter 1 Transformer scorecard ({PRESET})", stub],
        ["N", "", stub],
        ["GPU class", "", stub],
        ["Precision", "", stub],
        ["Companion script", "examples/chapter-13/invoice_leaderboard.py", stub],
        ["Memory unit", f"{MEMORY_UNIT} ({GIB_BYTES} bytes)", stub],
    ]


def meta_table_rows() -> list[list[str]]:
    stub = empty_stub()
    rows: list[list[str]] = []
    for number, architecture, kind in CHAPTER_ROWS:
        # MQAR + RULER stay on every row so state/hybrid honesty columns exist;
        # cells are empty stubs (pass/fail placeholders later, never invented scores).
        row = [str(number), architecture, kind, stub, stub, stub, stub, stub, stub]
        rows.append(row)
    return rows


def invoice_schema_rows() -> list[list[str]]:
    stub = empty_stub()
    return [[metric, stub, stub, stub, stub] for metric in WALL_METRICS]


def print_section(title: str, body: str) -> None:
    print()
    print(title)
    print("-" * len(title))
    print(body)


def main() -> int:
    print("Invoice Impact leaderboard — schema + labels only")
    print("=" * 48)
    print(f"Baseline: Chapter 1 Transformer scorecard ({PRESET})")
    print(f"Memory unit: {MEMORY_UNIT} (2**30 = {GIB_BYTES} bytes)")
    print("Protocol: same N / GPU class / precision (empty until measured)")
    print(
        "Workloads: "
        + " + ".join(REQUIRED_WORKLOADS)
        + " required; "
        + " + ".join(OPTIONAL_WORKLOADS)
        + " optional (columns kept)"
    )
    print("Labels:", " | ".join(LABELS))
    print("Fills: empty — do not invent numbers, SOTA tables, or timings")
    print("Packt-safe: no customer or company names")

    print_section(
        "Run card",
        markdown_table(("Field", "Value", "Label"), run_card_rows()),
    )
    print_section(
        "Meta-table (Ch3–12 Invoice rows — fills empty)",
        markdown_table(
            (
                "Ch",
                "Architecture",
                "Kind",
                *WORKLOAD_HEADERS,
                "MQAR",
                "RULER",
            ),
            meta_table_rows(),
        ),
    )
    print(
        "Honesty: MQAR on state rows; RULER on hybrid rows. "
        "Empty or pass/fail placeholders only. PPL-only is not success."
    )
    print_section(
        "Invoice schema (shared card shape — fills empty)",
        markdown_table(("Metric", *WORKLOAD_HEADERS), invoice_schema_rows()),
    )
    print_section(
        "Schema notes (not companion measurements)",
        "\n".join(
            (
                f"- Needle identity {labelled(NEEDLE_IDENTITY, 'modelled')} "
                "— illustrative planted token only; not a measured accuracy.",
                f"- Bi-Mamba {labelled(BI_MAMBA_PAPER_PCT, 'reproduced-from-source')} "
                f"({BI_MAMBA_ARXIV}) — paper figure only; never a measured companion result.",
                '- Paper "GB" only in reproduced-from-source cells.',
            )
        ),
    )
    print()
    print("status: schema-only — fills empty; no invented numbers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
