from pathlib import Path
from typing import Dict




def get_files(directory: str) -> Dict[str, str]:
    """Return a dict { filename: filepath }
     for all files inside directory."""
    
    directory = Path(directory)
    return {file.name: str(file) for file in directory.rglob("*") if file.is_file()}