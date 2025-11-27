import re
from typing import List, Dict

class DataCleaner:
    def __init__(self, pattern: str = r"^[a-zA-Z0-9]+$"):
        self.pattern = re.compile(pattern)

    def clean(self, data: Dict[str, List[str]]) -> Dict[str, List[str]]:
        return {
            k: [w for w in words if self.pattern.match(str(w))]
            for k, words in data.items()
        }