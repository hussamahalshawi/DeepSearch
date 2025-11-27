from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
from typing import Dict, List




def process_file(path: str) -> Dict:
    reader = get_reader(path)
    return reader.read(path)




def run(directory: str, keyword: str) -> Dict[str, Tuple[int, List[str]]]:
    files = get_files(directory)
    results = defaultdict(list)


    with ThreadPoolExecutor(max_workers=20) as executor:
        for data in executor.map(process_file, files.values()):
            if "words" in data:
                results[data["filename"]] = data["words"]
            

    cleaner = DataCleaner()
    cleaned = cleaner.clean(results)


    searcher = SearchEngine(keyword)
    return searcher.rank(cleaned)




# ✅ Example usage:
if __name__ == "__main__":
    directory = "/home/hussam/ALL/work/projects"
    keyword = "python"
    print(run(directory, keyword))