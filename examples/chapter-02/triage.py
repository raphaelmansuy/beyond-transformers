"""Stub triage CLI — Chapter 2 architecture decision framework.

See chapters/02-architectural-taxonomy-2026/SPINE.md and
examples/architecture-decision-framework.md.
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
    print("[stub] architecture triage")
    print("Families:", ", ".join(FAMILIES))
    print("Running examples:", ", ".join(EXAMPLES))


if __name__ == "__main__":
    main()
