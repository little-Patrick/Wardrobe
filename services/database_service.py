from pathlib import Path
from typing import List
from utils import database

class DatabaseService:
    """Facade over lower-level database utilities.

    Adds small convenience helpers for UI layer.
    """
    def __init__(self):
        self.db_dir = Path(database.DB_DIR)
        self.db_dir.mkdir(parents=True, exist_ok=True)

    # Re-export of import functionality
    def import_csv(self, csv_path: str):
        return database.import_csv(csv_path)

    def list_databases(self) -> List[Path]:
        return sorted(self.db_dir.glob("*.duckdb"))

    def delete_database(self, path: Path):
        if path.exists():
            path.unlink()
