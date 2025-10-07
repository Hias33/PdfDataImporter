# PdfDataImporter

**A Python tool to extract tables from PDF files, convert them to CSV, and import the data into a PostgreSQL database.**  
Designed for automation, ETL workflows, and data migration.

---

## 🚀 Features

- Extracts tabular data from PDF files using `pdfplumber`.
- Converts extracted tables to CSV with `pandas`.
- Imports CSV data into PostgreSQL via `SQLAlchemy`.
- Configuration via `config.yaml` (no hardcoded credentials).
- Modular design for easy extension and maintenance.
- Works on local machines or Raspberry Pi.

---

## 🧱 Project Structure

PdfDataImporter/
│
├─ main.py
├─ config.yaml
├─ requirements.txt
├─ test_data_import.pdf
├─ .gitignore
└─ modules/
  ├─ pdf_parser.py
  ├─ csv_handler.py
  └─ db_handler.py
