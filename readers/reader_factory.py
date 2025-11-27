from pathlib import Path

from readers.base_reader import BaseReader
from readers.json_reader import JSONReader
from readers.txt_reader import TXTReader

EXTENSION_MAP = {
    "txt": TXTReader(),
    "json": JSONReader(),
}


def get_reader(path: str) -> BaseReader:
    ext = Path(path).suffix.lower().replace(".", "")
    return EXTENSION_MAP.get(ext, TXTReader())  # default fallback
