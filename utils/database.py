import os
import re
import sys
from pathlib import Path
import pandas as pd
import duckdb

# Cross-platform config directory for app data
_home = Path.home()
if os.name == "nt":  # Windows
    _config_root = Path(os.getenv("APPDATA", str(_home)))
elif sys.platform == "darwin":  # macOS
    _config_root = _home / "Library" / "Application Support"
else:  # Linux and other POSIX
    _config_root = _home / ".local" / "share"
    
APP_NAME = "Wardrobe"
DB_DIR = str(_config_root / APP_NAME / "db")
os.makedirs(DB_DIR, exist_ok=True)

def import_csv(csv_path: str):
    """Import a CSV into DuckDB as a table named after the file stem.

    - Replaces the table if it already exists.
    - Uses a single persistent DuckDB file for the app.
    """
    df = pd.read_csv(csv_path)
    table_name = _safe_table_name(Path(csv_path).stem)
    db_path = get_user_db_path(csv_path)
    con = duckdb.connect(str(db_path))
    try:
        # Register the DataFrame and create/replace table from it
        con.register("df", df)
        con.execute(f'CREATE OR REPLACE TABLE "{table_name}" AS SELECT * FROM df')
    finally:
        con.close()


def get_user_db_path(file_path: str) -> Path:
    stem = Path(file_path).stem
    db_file_name = _safe_db_filename(stem)
    db_file_path = Path(DB_DIR) / db_file_name
    # Ensure directory exists; don't touch the file to avoid invalid DB errors.
    Path(DB_DIR).mkdir(parents=True, exist_ok=True)
    return db_file_path


def _safe_table_name(name: str):
    return re.sub(r"[^A-Za-z0-9_]", "_", name.strip()) or "table"


def _safe_db_filename(stem: str) -> str:
    safe_stem = re.sub(r"[^A-Za-z0-9_-]", "_", stem.strip()) or "database"
    return f"{safe_stem}.duckdb"
