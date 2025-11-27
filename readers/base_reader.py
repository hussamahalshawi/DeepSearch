from abc import ABC, abstractmethod
from typing import Dict


class BaseReader(ABC):
    @abstractmethod
    def read(self, path: str) -> Dict:
        """Return structured extracted text data."""
        pass