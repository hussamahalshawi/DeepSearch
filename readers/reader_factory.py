from pathlib import Path

EXTENSION_MAP = {
    "txt": TXTReader(),
    "json": JSONReader(),
}


def get_reader(path: str) -> BaseReader:
    ext = Path(path).suffix.lower().replace(".", "")
    return EXTENSION_MAP.get(ext, TXTReader())  # default fallback
