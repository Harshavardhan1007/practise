import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()                                   # reads .env.
SOURCE = os.getenv("SOURCE_PATH", "data/sales.csv")
TARGET = os.getenv("TARGET_PATH", "output/sales_data.parquet") #data 

def extract() -> pd.DataFrame:
    return pd.read_csv(SOURCE)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["order_id"])
    df["amount"] = df["amount"].astype(float)
    return df

def load(df: pd.DataFrame) -> None:
    df.to_parquet(TARGET, index=False)

if __name__ == "__main__":
    load(transform(extract()))
    print("ETL complete ✅")
