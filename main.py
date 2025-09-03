import sys
from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow
from services.database_service import DatabaseService
from services.churn_service import ChurnService
from controllers.main_controller import MainController
from controllers.churn_controller import ChurnController


def build_app():
    window = MainWindow()

    # Services
    database_service = DatabaseService()
    churn_service = ChurnService()

    # Controllers
    main_controller = MainController(window, database_service)
    churn_controller = ChurnController(window, churn_service, database_service)
    # Retain references so Python GC doesn't collect controllers
    window._controllers = [main_controller, churn_controller]
    return window


def main():
    app = QApplication(sys.argv)
    window = build_app()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
