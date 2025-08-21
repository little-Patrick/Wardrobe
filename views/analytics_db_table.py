from PySide6.QtGui import QStandardItemModel, QStandardItem
import duckdb
from utils.database import DB_DIR

def create_database_tables(table_view):
    """Populates the QTableView with a joined table of churn predictions and probabilities."""
    pred_db_path = DB_DIR + "/model_churn_pred.duckdb"
    prob_db_path = DB_DIR + "/model_churn_prob.duckdb"

    # Connect to the predictions database
    pred_conn = duckdb.connect(pred_db_path)

    try:
        # Attach the probabilities database
        pred_conn.execute(f"ATTACH DATABASE '{prob_db_path}' AS prob_db")

        # Join the tables across the two databases
        query = """
        SELECT 
            p.churn_prediction AS Prediction,
            pr.churn_probability AS Probability
        FROM ChurnPredictions p
        JOIN prob_db.ChurnProbability pr
        ON p.rowid = pr.rowid
        """
        data = pred_conn.execute(query).fetchall()
        columns = ["Prediction", "Probability"]

    finally:
        pred_conn.close()

    # Populate the QTableView
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(columns)

    for row in data:
        items = [QStandardItem(str(cell)) for cell in row]
        model.appendRow(items)

    table_view.setModel(model)
