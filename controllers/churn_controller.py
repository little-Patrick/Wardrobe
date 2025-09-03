from PySide6.QtWidgets import QFileDialog, QMessageBox, QFormLayout, QLabel

from services.churn_service import ChurnService
from services.database_service import DatabaseService
from views.main_window import MainWindow
from views.churn.analytics_graphs import plot_churn_graphs
from views.churn.analytics_db_table import create_database_tables

class ChurnController:
    """Coordinates running the churn model and updating analytics UI."""
    def __init__(self, window: MainWindow, churn_service: ChurnService, db_service: DatabaseService):
        self.w = window
        self.churn_service = churn_service
        self.db_service = db_service
        self.w.requestRunChurn.connect(self.run_model)
        self.w.requestShowAnalytics.connect(self._show_analytics_for_model)

    # --- Slots --------------------------------------------------------
    def _show_analytics_for_model(self, model_name: str):
        self.w.mainStackedWidget.setCurrentWidget(self.w.analytics_pg)
        self.w.statusbar.showMessage(f"Showing {model_name} analytics")

    def run_model(self):
        start_dir = str(self.db_service.db_dir)
        db_path, _ = QFileDialog.getOpenFileName(
            self.w,
            "Select DuckDB database",
            start_dir,
            "DuckDB Databases (*.duckdb)"
        )
        if not db_path:
            return
        self.w.statusbar.showMessage("Running churn model…")
        try:
            summary = self.churn_service.run(db_path)
            self._update_churn_overview(summary)
            plot_churn_graphs(self.w.graphs_tab)
            create_database_tables(self.w.tableView)
            self.w.statusbar.showMessage("Churn model completed")
        except Exception as e:  # noqa: BLE001 broad for UI barrier
            QMessageBox.warning(self.w, "Churn Model", str(e))
            self.w.statusbar.showMessage("Churn model finished with warnings")

    # --- UI helpers ---------------------------------------------------
    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()
            child = item.layout()
            if child is not None:
                self._clear_layout(child)

    def _update_churn_overview(self, summary: dict):
        layout = QFormLayout(self.w.model_overview_widget)
        self.w.model_overview_widget.setLayout(layout)
        self._clear_layout(layout)
        for key, value in summary.items():
            layout.addRow(QLabel(str(key), self.w.model_overview_widget),
                          QLabel(str(value), self.w.model_overview_widget))
