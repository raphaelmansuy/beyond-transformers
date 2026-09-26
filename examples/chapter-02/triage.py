"""Stub triage CLI for Chapter 2 architecture decision framework.

See examples/architecture-decision-framework.md and
chapters/02-architectural-taxonomy-2026/README.md.
"""

# stub

FAMILIES = ("generative", "predictive", "energy-based")
EXAMPLES = (
    "efficient-scalar",
    "long-context-agent",
    "structural-reasoner",
    "dynamic-streamer",
)


def main() -> None:
    print("[stub] Beyond Transformers — architecture triage")
    print("Families:", ", ".join(FAMILIES))
    print("Running examples:", ", ".join(EXAMPLES))
    print("Fill in interactive questions later; see architecture-decision-framework.md")


if __name__ == "__main__":
    main()
