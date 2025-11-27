from typing import Dict

class TXTReader(BaseReader):
    def read(self, path: str) -> Dict:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            return {"filename": path, "text": text, "words": text.split()}
        except Exception as e:
            return {"filename": path, "error": str(e), "text": "", "words": []}
