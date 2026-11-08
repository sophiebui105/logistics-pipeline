from pathlib import Path
import duckdb

RAW_DIR = Path("data/raw")
DB_PATH = Path("warehouse/olist.duckdb")


def main():
    DB_PATH.parent.mkdir(exist_ok=True)
    con = duckdb.connect(str(DB_PATH))
    con.execute("CREATE SCHEMA IF NOT EXISTS raw")

    for csv in sorted(RAW_DIR.glob("*.csv")):
        table = csv.stem.replace("olist_", "").replace("_dataset", "")
        con.execute(
            f"CREATE OR REPLACE TABLE raw.{table} AS "
            f"SELECT * FROM read_csv_auto('{csv.as_posix()}')"
        )
        n = con.execute(f"SELECT COUNT(*) FROM raw.{table}").fetchone()[0]
        print(f"{table}: {n:,} rows")

    con.close()


if __name__ == "__main__":
    main()