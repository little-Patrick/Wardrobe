from pathlib import Path
from PySide6.QtWidgets import QFileDialog, QMessageBox, QApplication, QListWidgetItem, QStyle
from PySide6.QtCore import Qt

from services.database_service import DatabaseService
from views.main_window import MainWindow

class MainController:
    """Handles generic window events (import, manage DB list)."""
    def __init__(self, window: MainWindow, db_service: DatabaseService):
        self.w = window
        self.db_service = db_service

        # Connect signals
        self.w.requestImportCsv.connect(self.import_csv_dialog)
        self.w.requestManageDb.connect(self.show_manage_db)
        self.w.listWidget.customContextMenuRequested.connect(self._show_list_context_menu)

    # --- File import --------------------------------------------------
    def import_csv_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.w,
            "Select CSV",
            "",
            "CSV Files (*.csv)"
        )
        if not file_path:
            return
        try:
            self.db_service.import_csv(file_path)
            self.w.statusbar.showMessage("File imported into database successfully")
            self.populate_db_list()
        except Exception as e:  # noqa: BLE001 broad OK for UI barrier
            QMessageBox.critical(self.w, "Error", str(e))

    # --- Manage DB page -----------------------------------------------
    def show_manage_db(self):
        self.populate_db_list()
        self.w.mainStackedWidget.setCurrentWidget(self.w.manage_db_pg)

    def populate_db_list(self):
        self.w.listWidget.clear()
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        count = 0
        for db_file in self.db_service.list_databases():
            item = QListWidgetItem(icon, db_file.name)
            item.setData(Qt.ItemDataRole.UserRole, str(db_file))
            self.w.listWidget.addItem(item)
            count += 1
        self.w.statusbar.showMessage(f"Found {count} database(s)")

    def _delete_db_file(self, item):
        file_path = Path(item.data(Qt.ItemDataRole.UserRole))
        confirm = QMessageBox.question(
            self.w,
            "Delete Database",
            f"Are you sure you want to delete '{file_path}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                self.db_service.delete_database(file_path)
                self.w.listWidget.takeItem(self.w.listWidget.row(item))
                self.w.statusbar.showMessage(f"Deleted database: {file_path}")
            except Exception as e:  # noqa: BLE001
                QMessageBox.critical(self.w, "Error", f"Failed to delete file: {str(e)}")

    def _show_list_context_menu(self, position):
        item = self.w.listWidget.itemAt(position)
        if not item:
            return
        from PySide6.QtWidgets import QMenu  # local import to avoid polluting namespace
        menu = QMenu(self.w)
        delete_action = menu.addAction("Delete")
        delete_action.triggered.connect(lambda: self._delete_db_file(item))
        menu.exec(self.w.listWidget.mapToGlobal(position))
