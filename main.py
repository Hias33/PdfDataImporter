from modules.pdf_parser import extract_table_from_pdf
from modules.csv_handler import save_to_csv, read_from_csv
from modules.db_handler import import_to_postgres, load_config

def main():
    cfg = load_config()

    df = extract_table_from_pdf("test_data_import.pdf")

    save_to_csv(df, "data.csv")

    df_csv = read_from_csv("data.csv")

    import_to_postgres(df_csv, cfg)

if __name__ == "__main__":
    main()
