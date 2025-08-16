import duckdb
import os
import joblib
import pandas as pd
from pathlib import Path
from utils.database import get_user_db_path, _safe_table_name

# Load the saved model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "customer_churn_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_churn(duckdb_db_path: str):
    print("Model start")
    conn = None
    pred_conn = None
    prob_conn = None
    try:
        # Connect to the DuckDB database
        conn = duckdb.connect(str(duckdb_db_path))
        print("Connected to database:", duckdb_db_path)

        # Determine the source table name; default to the DB file stem
        table_name = _safe_table_name(Path(duckdb_db_path).stem)
        # Fetch data into a DataFrame using DuckDB
        df = conn.execute(f'SELECT * FROM "{table_name}"').fetchdf()

        # Ensure the DataFrame has the required columns
        required_columns = [
            "account_age_months", "avg_orders_per_month", "avg_order_value", "returns_rate",
            "support_tickets_6m", "reviews_submitted", "website_visits_per_month",
            "cart_abandonment_rate", "loyalty_member", "payment_failures_12m", "device_type",
            "discount_usage_rate", "days_since_last_active", "satisfaction_score"
        ]
        
        if not all(col in df.columns for col in required_columns):
            return "Database table is missing required columns."
        
        # Make predictions
        predictions = model.predict(df[required_columns])
        probabilities = model.predict_proba(df[required_columns])[:, 1]
        
        # Add predictions and probabilities to the DataFrame
        df['churn_prediction'] = predictions
        df['churn_probability'] = probabilities

        # Persist results to separate DuckDB databases
        pred_db_path = get_user_db_path("model_churn_pred")
        prob_db_path = get_user_db_path("model_churn_prob")
        pred_conn = duckdb.connect(str(pred_db_path))
        prob_conn = duckdb.connect(str(prob_db_path))

        # Write predictions using DuckDB (register DataFrame and CREATE TABLE AS)
        pred_conn.register("df", df[["churn_prediction"]])
        pred_conn.execute('CREATE OR REPLACE TABLE "ChurnPredictions" AS SELECT * FROM df')
        prob_conn.register("df", df[["churn_probability"]])
        prob_conn.execute('CREATE OR REPLACE TABLE "ChurnProbability" AS SELECT * FROM df')

        print("model end")

        return {"pred_db": str(pred_db_path), "prob_db": str(prob_db_path)}

    except Exception as e:
        return f"Error processing database: {str(e)}"
    finally:
        if conn:
            conn.close()
        if pred_conn:
            pred_conn.close()
        if prob_conn:
            prob_conn.close()


