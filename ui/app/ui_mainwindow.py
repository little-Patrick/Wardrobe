# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTabWidget,
    QTableView, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(833, 598)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 229, 204);")
        self.actionManage_Database = QAction(MainWindow)
        self.actionManage_Database.setObjectName(u"actionManage_Database")
        icon = QIcon(QIcon.fromTheme(u"folder-visiting"))
        self.actionManage_Database.setIcon(icon)
        self.actionManage_Database.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAdd_File = QAction(MainWindow)
        self.actionAdd_File.setObjectName(u"actionAdd_File")
        icon1 = QIcon(QIcon.fromTheme(u"list-add"))
        self.actionAdd_File.setIcon(icon1)
        self.actionAdd_File.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAnalytics = QAction(MainWindow)
        self.actionAnalytics.setObjectName(u"actionAnalytics")
        icon2 = QIcon(QIcon.fromTheme(u"audio-card"))
        self.actionAnalytics.setIcon(icon2)
        self.actionAnalytics.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.mainStackedWidget.setStyleSheet(u"background=qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.home_pg = QWidget()
        self.home_pg.setObjectName(u"home_pg")
        self.horizontalLayout_3 = QHBoxLayout(self.home_pg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(self.home_pg)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.mainStackedWidget.addWidget(self.home_pg)
        self.manage_db_pg = QWidget()
        self.manage_db_pg.setObjectName(u"manage_db_pg")
        self.horizontalLayout = QHBoxLayout(self.manage_db_pg)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.manage_db_pg)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background=rgba(255, 255, 255, 0)")

        self.horizontalLayout.addWidget(self.listWidget)

        self.mainStackedWidget.addWidget(self.manage_db_pg)
        self.analytics_pg = QWidget()
        self.analytics_pg.setObjectName(u"analytics_pg")
        self.horizontalLayout_2 = QHBoxLayout(self.analytics_pg)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.analytics_pg)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    background-color: rgb(255, 229, 204); /* Match main window background */\n"
"    border: 2px solid rgb(204, 153, 255); /* Retro border color */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(229, 204, 255); /* Light purple for non-selected tabs */\n"
"    border: 1px solid rgb(153, 102, 204); /* Slightly darker border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    color: black; /* Black text for better readability */\n"
"    font: bold 12px \"Courier New\"; /* Retro font */\n"
"    padding: 5px; /* Padding for better spacing */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(153, 102, 204); /* Darker purple for active tab */\n"
"    color: white; /* White text for active tab */\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        self.general_tab.setStyleSheet(u"QTabWidget::pane {\n"
"    background-color: rgb(255, 229, 204); /* Match main window background */\n"
"    border: 2px solid rgb(204, 153, 255); /* Retro border color */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(204, 153, 255); /* Soft purple */\n"
"    border: 1px solid rgb(153, 102, 204); /* Slightly darker border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    color: white; /* Text color */\n"
"    font: bold 12px \"Courier New\"; /* Retro font */\n"
"    padding: 5px; /* Padding for better spacing */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(153, 102, 204); /* Darker purple for active tab */\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.general_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.run_model_btn = QPushButton(self.general_tab)
        self.run_model_btn.setObjectName(u"run_model_btn")
        self.run_model_btn.setMaximumSize(QSize(100, 16777215))
        self.run_model_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 153, 102); /* Soft orange */\n"
"    border: 2px solid rgb(255, 102, 51); /* Slightly darker border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    color: white; /* Text color */\n"
"    font: bold 12px \"Courier New\"; /* Retro font */\n"
"    padding: 5px; /* Padding for better spacing */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 102, 51); /* Darker orange on hover */\n"
"}")

        self.verticalLayout_2.addWidget(self.run_model_btn)

        self.model_overview_widget = QWidget(self.general_tab)
        self.model_overview_widget.setObjectName(u"model_overview_widget")

        self.verticalLayout_2.addWidget(self.model_overview_widget)

        self.tabWidget.addTab(self.general_tab, "")
        self.graphs_tab = QWidget()
        self.graphs_tab.setObjectName(u"graphs_tab")
        self.tabWidget.addTab(self.graphs_tab, "")
        self.table_tab = QWidget()
        self.table_tab.setObjectName(u"table_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.table_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableView = QTableView(self.table_tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"backround=rgba(255, 255, 255, 0)")

        self.horizontalLayout_5.addWidget(self.tableView)

        self.tabWidget.addTab(self.table_tab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.mainStackedWidget.addWidget(self.analytics_pg)

        self.verticalLayout.addWidget(self.mainStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 833, 38))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMaximumSize(QSize(16777215, 16777215))
        self.toolBar.setAcceptDrops(True)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionAdd_File)
        self.toolBar.addAction(self.actionManage_Database)
        self.toolBar.addAction(self.actionAnalytics)

        self.retranslateUi(MainWindow)

        self.mainStackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wardrobe", None))
        self.actionManage_Database.setText(QCoreApplication.translate("MainWindow", u"Manage Database", None))
        self.actionAdd_File.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.actionAnalytics.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:48pt; font-weight:700; font-style:italic; color:#4b1855;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:48pt; font-weight:700; font-style:italic; color:#4b1855;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:700; font-style:italic; color:#4b1855;\">Home Alas</span></p></"
                        "body></html>", None))
        self.run_model_btn.setText(QCoreApplication.translate("MainWindow", u"Run Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphs_tab), QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_tab), QCoreApplication.translate("MainWindow", u"Table", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

