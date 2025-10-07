import pdfplumber
import pandas as pd

def extract_table_from_pdf(pdf_path: str) -> pd.DataFrame:
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        table = first_page.extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    return df
