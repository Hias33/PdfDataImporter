import pandas as pd
from pathlib import Path

def save_to_csv(df: pd.DataFrame, csv_path: str = "data.csv"):
    """
    Speichert den übergebenen DataFrame als CSV-Datei.
    """
    path = Path(csv_path)
    df.to_csv(path, index=False)
    print(f"💾 CSV exportiert nach: {path.resolve()}")

def read_from_csv(csv_path: str = "data.csv") -> pd.DataFrame:
    """
    Liest eine CSV-Datei wieder in einen Pandas DataFrame ein.
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"❌ Datei '{csv_path}' wurde nicht gefunden.")
    df = pd.read_csv(path)
    print(f"📂 CSV geladen aus: {path.resolve()}")
    return df
