# Python & SQLite3 Integration 🚀

This repository contains a foundational Python script demonstrating how to integrate and manage SQLite databases using Python's built-in `sqlite3` module. 

This project was developed while studying the **"100 Days of Data Science and Machine Learning"** course by Atıl Samancıoğlu.

## 📌 Features
- **Automated Database Setup:** Checks for existing databases and initializes a fresh `students.db` locally.
- **Table Creation:** Executes SQL `CREATE TABLE` commands for `Students` and `Courses` tables with appropriate data types and constraints (e.g., `PRIMARY KEY`, `UNIQUE`, `NOT NULL`).
- **Data Insertion:** Uses `executemany()` to efficiently insert multiple records into the database.
- **Basic SQL Queries:** Demonstrates reading and filtering data using `SELECT`, `WHERE`, `ORDER BY`, and `LIMIT`.
- **CRUD Operations:** Covers Insert, Update, and Delete statements.
- **Aggregate Functions:** Shows how to calculate `COUNT()`, `AVG()`, `MAX()`, and `MIN()` directly through SQL queries.

## 🛠️ Technologies Used
- Python 3.x
- SQLite3 (Python Built-in library)

## 🚀 How to Run
Since this project uses Python's built-in libraries, no external dependencies or installations are required. 

Simply run the script in your IDE or terminal:
```bash
python main.py