import json
from typing import Dict

from readers.base_reader import BaseReader


class JSONReader(BaseReader):
    def read(self, path: str) -> Dict:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                data = json.load(f)
            text = str(data)
            words = text.split()
            return {"filename": path, "text": text, "words": words}
        except Exception as e:
            return {"filename": path, "error": str(e), "text": "", "words": []}
