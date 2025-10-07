from sqlalchemy import create_engine
import pandas as pd
import yaml

def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def connect_postgres(cfg):
    user = cfg["database"]["user"]
    password = cfg["database"]["password"]
    host = cfg["database"]["host"]
    port = cfg["database"]["port"]
    dbname = cfg["database"]["dbname"]
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")
    return engine

def import_to_postgres(df: pd.DataFrame, cfg):
    engine = connect_postgres(cfg)
    table = cfg["database"]["table"]
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"✅ Data imported to table '{table}' in database '{cfg['database']['dbname']}'")
