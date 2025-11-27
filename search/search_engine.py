from typing import Dict, List, Tuple

class SearchEngine:
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()

    def score(self, words: List[str]) -> Tuple[int, str]:
        count = sum(1 for w in words if self.keyword in w.lower())
        return count

    def rank(self, dataset: Dict[str, List[str]]) -> Dict[str, Tuple[int, List[str]]]:
        ranked = {
            filename: (self.score(words), words)
            for filename, words in dataset.items()
        }
        # Sort by score descending & remove zero results
        return dict(sorted(((k, v) for k, v in ranked.items() if v[0] > 0), key=lambda x: x[1][0], reverse=True,))
