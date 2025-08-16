import sys
from pathlib import Path
from ui.app.ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QApplication,
    QMessageBox,
    QStatusBar,
    QListWidgetItem,
    QStyle,
    QListView,
    QMenu,
    QToolButton,
    QLabel,
    QVBoxLayout,
)
from utils import database
from models import customer_churn

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainStackedWidget.setCurrentWidget(self.home_pg)
        self.actionAdd_File.triggered.connect(self.add_file)
        self.actionManage_Database.triggered.connect(self.show_manage_db)
        self.listWidget.setViewMode(QListView.ViewMode.IconMode)
        self.listWidget.setIconSize(QSize(48, 48))
        self.listWidget.setResizeMode(QListView.ResizeMode.Adjust)
        self._setup_analytics_dropdown()
        # Wire the Run Model button
        if hasattr(self, "run_model_btn"):
            self.run_model_btn.clicked.connect(self.run_churn_model)

    def add_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV",
            "",
            "CSV Files (*.csv)"
        )
        if file_path:
            try:
                database.import_csv(file_path)
                self.statusbar.showMessage("File imported into database successfully")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def show_manage_db(self):
        self.populate_db_list()
        self.mainStackedWidget.setCurrentWidget(self.manage_db_pg)

    def _setup_analytics_dropdown(self):
        menu = QMenu(self)
        churn_action = menu.addAction("Churn")
        churn_action.triggered.connect(lambda: self.show_analytics_for_model("Churn"))

        tool_btn = self.toolBar.widgetForAction(self.actionAnalytics)
        if isinstance(tool_btn, QToolButton):
            tool_btn.setPopupMode(QToolButton.InstantPopup)
            tool_btn.setMenu(menu)
        else:
            self.actionAnalytics.setMenu(menu)
        self._analytics_menu = menu

    def show_analytics_for_model(self, model_name: str):
        self.mainStackedWidget.setCurrentWidget(self.analytics_pg)

        if not hasattr(self, "analyticsHeader"):
            layout = self.general_tab.layout()
            if layout is None:
                layout = QVBoxLayout(self.general_tab)
            self.analyticsHeader = QLabel(self.general_tab)
            layout.addWidget(self.analyticsHeader)

        self.analyticsHeader.setText(f"Analytics: {model_name}")
        self.statusbar.showMessage(f"Showing {model_name} analytics")

    def populate_db_list(self):
        self.listWidget.clear()
        db_dir = Path(database.DB_DIR)
        db_dir.mkdir(parents=True, exist_ok=True)
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        count = 0
        for db_file in sorted(db_dir.glob("*.duckdb")):
            item = QListWidgetItem(icon, db_file.name)
            item.setData(Qt.ItemDataRole.UserRole, str(db_file))
            self.listWidget.addItem(item)
            count += 1
        self.statusbar.showMessage(f"Found {count} database(s)")

    def run_churn_model(self):
        # Ask user to select the DuckDB database to run the model on
        start_dir = database.DB_DIR
        db_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select DuckDB database",
            start_dir,
            "DuckDB Databases (*.duckdb)"
        )
        if not db_path:
            return
        self.statusbar.showMessage("Running churn model…")
        result = customer_churn.predict_churn(db_path)
        if isinstance(result, dict):
            msg = (
                f"Churn model completed.\n"
                f"Predictions DB: {result.get('pred_db')}\n"
                f"Probabilities DB: {result.get('prob_db')}"
            )
            QMessageBox.information(self, "Churn Model", msg)
            self.statusbar.showMessage("Churn model completed")
        else:
            # Treat any non-dict as an error message string
            QMessageBox.warning(self, "Churn Model", str(result))
            self.statusbar.showMessage("Churn model finished with warnings")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
