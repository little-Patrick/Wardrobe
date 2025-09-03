from typing import Dict, Tuple, Any
from models.churn import customer_churn

class ChurnService:
    """Service layer for running churn model and transforming outputs."""
    def run(self, db_path: str) -> Dict[str, Any]:
        # Directly return dict produced by model for now; could map to dataclass later.
        result = customer_churn.predict_churn(db_path)
        if not isinstance(result, dict):
            raise RuntimeError(result)
        return result
