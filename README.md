# Deep Search
📌 DeepSearch — Intelligent Local Search Engine

A Python-based intelligent search engine that scans files, cleans their content, processes text, and ranks results using a custom scoring system.

🚀 About the Project

After a long break from programming due to war and difficult circumstances, I decided to rebuild my technical skills through real, practical projects.
DeepSearch was the first step — a complete hands-on project designed to bring me back into Python development and modern software engineering practices.

🔥 Key Features

- Fast file scanning using multithreading (ThreadPoolExecutor)

- Clean architecture with SRP + Factory Pattern

- Flexible file readers (TXT, JSON, and easily extendable)

- Regex-based text cleaning and tokenization

- Advanced search pipeline using token matches, partial matches, and ranking

- Extensible design: add new readers, clean steps, or scoring logic easily

- Robust error handling and logging

🧠 How the system works

1️⃣ File Discovery

All files in the directory are indexed using a fast recursive scanner.

2️⃣ Multithreaded Reading

Each file is processed in parallel via a Reader chosen dynamically (Factory Pattern).

3️⃣ Cleaning & Preprocessing

- Remove unwanted patterns (e.g., URLs)

- Tokenize text

- Normalize words for accurate search

4️⃣ Search Engine

Implements custom ranking logic based on:

- exact matches

- substring matches

- fuzzy-like comparisons

- phrase scoring

5️⃣ Ranking

Results are sorted from highest score → lowest
Zero-score files are removed automatically.

🧩 Technologies & Concepts Used

- Python

- Multithreading

- Design Patterns (Factory, SRP)

- Regex

- Clean Code principles

- File parsing

- Search scoring & ranking

- Dictionaries, Sets, and high-performance text operations

📂 Folder Structure

```
deepsearch/
│── main.py
│── readers/
│   ├── base_reader.py
│   ├── txt_reader.py
│   ├── json_reader.py
│   └── reader_factory.py
│── cleaners/
│   └── data_cleaner.py
│── search/
│   └── search_engine.py
└── utils/
    └── file_utils.py
```