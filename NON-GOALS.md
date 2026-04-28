# Non-goals

What `agentic-artifacts` deliberately does not try to be. This repo records data provenance (object lineage); action provenance is the receipts repo's lane. The split is precise per `GLOSSARY.md` in the meta-repo.

## Not runtime artifact storage

Manifests record lineage and integrity hashes; the underlying object storage is downstream. Adopters keep their existing artifact storage (object stores, content-addressable stores, blob services); manifests reference those objects by hash and location.

## Not build-time provenance

Build-time provenance — what source produced what binary, with what builders — is owned by SLSA. Artifacts records *runtime* lineage of agent outputs, distinct from but composable with SLSA's build-time chain. See the SLSA section of `INTEROP.md` for the cross-reference predicate.

## Not action provenance

Action provenance — *what an agent did, signed* — lives in `agentic-receipts`. Data lineage — *what data flowed where, hashed* — lives here. The two compose in the bundle but answer different audit questions; conflating them is one of the most common mistakes in this design space.

## Not a content-addressable store

Manifests reference content by hash, but this repo does not implement deduplication, caching, or hash-keyed retrieval. Adopters wanting a CAS for their artifact store choose one independently and reference it from manifests.

## Not a backup system

Manifests prove integrity at the moment of recording. They do not provide redundancy, replication, or recovery from data loss. A bundle without its referenced artifacts is incomplete; ensuring artifact persistence and availability is the adopter's responsibility through their normal storage and backup tooling.
