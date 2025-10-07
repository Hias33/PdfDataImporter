from modules.pdf_parser import extract_table_from_pdf
from modules.csv_handler import save_to_csv, read_from_csv
from modules.db_handler import import_to_postgres, load_config

def main():
    cfg = load_config()

    # 1. PDF → DataFrame
    df = extract_table_from_pdf("test_data_import.pdf")

    # 2. DataFrame → CSV
    save_to_csv(df, "data.csv")

    # 3. CSV wieder einlesen (optional, zum Testen)
    df_csv = read_from_csv("data.csv")

    # 4. CSV-Daten → PostgreSQL
    import_to_postgres(df_csv, cfg)

if __name__ == "__main__":
    main()
