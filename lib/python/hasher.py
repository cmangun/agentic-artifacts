"""Reference artifact hasher."""
import hashlib
from pathlib import Path

def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"

def verify_artifact(path: Path, expected_hash: str) -> bool:
    return hash_file(path) == expected_hash
