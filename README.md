# agentic-artifacts

> Part of the [Agentic Evidence Suite](https://github.com/cmangun/agentic-evidence) — six interoperating components for verifiable agentic AI. See [`REFERENCE-ARCHITECTURE.md`](https://github.com/cmangun/agentic-evidence/blob/main/REFERENCE-ARCHITECTURE.md) for the suite-level architecture.

Artifact manifests and provenance rules for **integrity-preserved agent outputs**.

This repo defines how agent outputs (documents, patches, datasets, images) are:
- Hashed for integrity verification
- Referenced from trace events via provenance links
- Bundled portably for review
- Verified independently

Source receipts/trace semantics: [agentic-receipts](https://github.com/cmangun/agentic-receipts)

## Contents

- `schemas/` — Artifact manifest JSON schema
- `spec/` — Artifact, provenance, and diff-format specifications
- `examples/` — Example bundles with report and code patch artifacts
- `lib/` — Reference implementations (Rust, Python)

## License

MIT