from PySide6.QtWidgets import QMainWindow, QListView, QToolButton, QMenu
from PySide6.QtCore import QSize, Qt, Signal
from ui.app.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """Top-level application window (presentation-only).

    Emits signals which controllers subscribe to; contains no business logic.
    """
    requestImportCsv = Signal()
    requestManageDb = Signal()
    requestRunChurn = Signal()
    requestShowAnalytics = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setup_toolbar_styling()
        self._wire_actions()
        self._setup_list_widget()
        self._setup_analytics_dropdown()
        self.mainStackedWidget.setCurrentWidget(self.home_pg)
        self._controllers = []

    # --- Setup helpers -------------------------------------------------
    def _wire_actions(self):
        self.actionAdd_File.triggered.connect(self.requestImportCsv.emit)
        self.actionManage_Database.triggered.connect(self.requestManageDb.emit)
        # If user clicks analytics action directly (not via dropdown), default to Churn
        self.actionAnalytics.triggered.connect(lambda: self.requestShowAnalytics.emit("Churn"))
        if hasattr(self, "run_model_btn"):
            self.run_model_btn.clicked.connect(self.requestRunChurn.emit)

    def _setup_list_widget(self):
        self.listWidget.setViewMode(QListView.ViewMode.IconMode)
        self.listWidget.setIconSize(QSize(48, 48))
        self.listWidget.setResizeMode(QListView.ResizeMode.Adjust)
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

    def _setup_analytics_dropdown(self):
        menu = QMenu(self)
        churn_action = menu.addAction("Churn")
        churn_action.triggered.connect(lambda: self.requestShowAnalytics.emit("Churn"))
        tool_btn = self.toolBar.widgetForAction(self.actionAnalytics)
        if isinstance(tool_btn, QToolButton):
            tool_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
            tool_btn.setMenu(menu)
        else:
            self.actionAnalytics.setMenu(menu)
        self._analytics_menu = menu

    def _setup_toolbar_styling(self):
        # Keep styling consolidated here
        self.toolBar.setStyleSheet(
        """
        QToolBar { background-color: rgb(255, 153, 102); border: 2px solid rgb(255, 102, 51); border-radius: 10px; padding: 5px; }
        QToolButton { background-color: rgb(255, 178, 102); border: 1px solid rgb(255, 102, 51); border-radius: 5px; color: white; font: bold 12px 'Courier New'; padding: 5px; }
        QToolButton:hover { background-color: rgb(255, 102, 51); }
        """
        )
