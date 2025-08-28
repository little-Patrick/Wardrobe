from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import duckdb
from utils.database import DB_DIR

## QWidget is graph_tab
def plot_churn_graphs(container: QWidget) -> None:
    # churn_bar = _churn_bar_graph()
    # prob_distribution = _prob_distribution_bar()
    # User graph
    # most important features graph
    
    pred_db_path = DB_DIR + "/model_churn_pred.duckdb"
    prob_db_path = DB_DIR + "/model_churn_prob.duckdb"

    pred_conn = duckdb.connect(pred_db_path)
    prob_conn = duckdb.connect(prob_db_path)

    churn_data = pred_conn.execute("SELECT churn_prediction AS churn, COUNT(*) AS count FROM ChurnPredictions GROUP BY churn").fetchall()
    prob_data = prob_conn.execute("SELECT churn_probability AS probability FROM ChurnProbability").fetchall()

    pred_conn.close()
    prob_conn.close()

    layout = QVBoxLayout(container)
    container.setLayout(layout)

      # Prepare data for graphs
    churn_labels = [row[0] for row in churn_data]
    churn_counts = [row[1] for row in churn_data]
    probabilities = [row[0] for row in prob_data]

    # Churn vs. Non-Churn Bar Graph
    churn_fig = Figure()
    churn_ax = churn_fig.add_subplot(111)
    churn_ax.bar(churn_labels, churn_counts, color=['blue', 'orange'])
    churn_ax.set_title("Churn vs Non-Churn")
    churn_ax.set_xlabel("Churn")
    churn_ax.set_ylabel("Count")
    churn_canvas = FigureCanvas(churn_fig)
    layout.addWidget(churn_canvas)

    # Probability Distribution Graph
    prob_fig = Figure()
    prob_ax = prob_fig.add_subplot(111)
    prob_ax.hist(probabilities, bins=20, color='green', alpha=0.7)
    prob_ax.set_title("Probability Distribution")
    prob_ax.set_xlabel("Probability")
    prob_ax.set_ylabel("Frequency")
    prob_canvas = FigureCanvas(prob_fig)
    layout.addWidget(prob_canvas)

def _churn_bar_graph():
    return

def _prob_distribution_bar():
    return
