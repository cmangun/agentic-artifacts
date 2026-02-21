# agentic-artifacts

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

## Suite

This repo is part of the **Agentic Evidence Suite**:
- [agentic-receipts](https://github.com/cmangun/agentic-receipts) (standard)
- [agentic-trace-cli](https://github.com/cmangun/agentic-trace-cli) (tooling)
- [agentic-artifacts](https://github.com/cmangun/agentic-artifacts) (outputs)
- [agentic-policy-engine](https://github.com/cmangun/agentic-policy-engine) (governance)
- [agentic-eval-harness](https://github.com/cmangun/agentic-eval-harness) (scenarios)
- [agentic-evidence-viewer](https://github.com/cmangun/agentic-evidence-viewer) (review UI)

## License

MIT
