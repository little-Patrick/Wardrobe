import sys
from pathlib import Path
from ui.app.ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QApplication,
    QMessageBox,
    QListWidgetItem,
    QStyle,
    QListView,
    QMenu,
    QToolButton,
    QLabel,
    QFormLayout,
)
from utils import database
from models.churn import customer_churn
from views.churn import plot_churn_graphs, create_database_tables
 

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
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.show_list_context_menu)
        self._setup_analytics_dropdown()
        self.toolBar.setStyleSheet("""
        QToolBar {
            background-color: rgb(255, 153, 102); /* Soft orange background */
            border: 2px solid rgb(255, 102, 51); /* Slightly darker border */
            border-radius: 10px; /* Rounded corners */
            padding: 5px; /* Padding for better spacing */
        }

        QToolButton {
            background-color: rgb(255, 178, 102); /* Lighter orange for buttons */
            border: 1px solid rgb(255, 102, 51); /* Slightly darker border */
            border-radius: 5px; /* Rounded corners */
            color: white; /* Text color */
            font: bold 12px "Courier New"; /* Retro font */
            padding: 5px; /* Padding for better spacing */
        }

        QToolButton:hover {
            background-color: rgb(255, 102, 51); /* Darker orange on hover */
        }
        """)
        # Wire the Run Model button
        if hasattr(self, "run_model_btn"):
            self.run_model_btn.clicked.connect(self.run_churn_model)

    # Add File Button
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

    # Manage Database Page
    def show_manage_db(self):
        self.populate_db_list()
        self.mainStackedWidget.setCurrentWidget(self.manage_db_pg)

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


    # Analytics Page
    def _setup_analytics_dropdown(self):
        menu = QMenu(self)
        churn_action = menu.addAction("Churn")
        churn_action.triggered.connect(lambda: self.show_analytics_for_model("Churn"))

        tool_btn = self.toolBar.widgetForAction(self.actionAnalytics)
        if isinstance(tool_btn, QToolButton):
            tool_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
            tool_btn.setMenu(menu)
        else:
            self.actionAnalytics.setMenu(menu)
        self._analytics_menu = menu

    def show_analytics_for_model(self, model_name: str):
        self.mainStackedWidget.setCurrentWidget(self.analytics_pg)
        self.statusbar.showMessage(f"Showing {model_name} analytics")


    # Churn Model
    def run_churn_model(self):
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
        results = customer_churn.predict_churn(db_path)
        
        if isinstance(results, dict):
            self.statusbar.showMessage("Churn model completed")
            self._update_churn_overview(results)
            plot_churn_graphs(self.graphs_tab)
            create_database_tables(self.tableView)
        else:
            QMessageBox.warning(self, "Churn Model", str(results))
            self.statusbar.showMessage("Churn model finished with warnings")

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
        layout = QFormLayout(self.model_overview_widget)
        self.model_overview_widget.setLayout(layout)
        self._clear_layout(layout)

        for key, value in summary.items():
            layout.addRow(QLabel(str(key), self.model_overview_widget), 
                          QLabel(str(value), self.model_overview_widget))
        return 

    def show_list_context_menu(self, position):
        item = self.listWidget.itemAt(position)
        if item:
            menu = QMenu(self)
            delete_action = menu.addAction("Delete")
            delete_action.triggered.connect(lambda: self.delete_db_file(item))
            menu.exec(self.listWidget.mapToGlobal(position))

    def delete_db_file(self, item):
        file_path = item.data(Qt.ItemDataRole.UserRole)
        confirm = QMessageBox.question(
            self,
            "Delete Database",
            f"Are you sure you want to delete '{file_path}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                Path(file_path).unlink()
                self.listWidget.takeItem(self.listWidget.row(item))
                self.statusbar.showMessage(f"Deleted database: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete file: {str(e)}")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
