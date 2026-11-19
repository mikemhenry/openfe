"""Fetch and unpack cached test datasets safely under pytest-xdist."""

import fcntl
from pathlib import Path

import pooch


def fetch_and_extract(store: pooch.Pooch, archive: str) -> Path:
    """Fetch an archive and serialize extraction into the shared Pooch cache."""
    if archive.endswith(".tar.gz"):
        processor = pooch.Untar()
    elif archive.endswith(".zip"):
        processor = pooch.Unzip()
    else:
        raise ValueError(f"Unsupported test data archive: {archive}")

    cache_dir = Path(store.path)
    cache_dir.mkdir(parents=True, exist_ok=True)
    lock_path = cache_dir / f"{archive}.lock"
    with lock_path.open("a+b") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        store.fetch(archive, processor=processor)

    return cache_dir / f"{archive}{processor.suffix}"
