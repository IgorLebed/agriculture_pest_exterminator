# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_gui_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.map_tab = QtWidgets.QWidget()
        self.map_tab.setObjectName("map_tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.map_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 761, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.map_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.map_layout.setContentsMargins(0, 0, 0, 0)
        self.map_layout.setObjectName("map_layout")
        self.webView = QWebEngineView(self.verticalLayoutWidget_2)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.map_layout.addWidget(self.webView)
        self.tabWidget.addTab(self.map_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.settings_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 344))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tabWidget.addTab(self.settings_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.menu_layout = QtWidgets.QVBoxLayout()
        self.menu_layout.setObjectName("menu_layout")
        self.btn_upload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_upload.setObjectName("btn_upload")
        self.menu_layout.addWidget(self.btn_upload)
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setObjectName("btn_download")
        self.menu_layout.addWidget(self.btn_download)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.menu_layout.addWidget(self.btn_clear)
        self.trajectory_generation = QtWidgets.QPushButton(self.centralwidget)
        self.trajectory_generation.setObjectName("trajectory_generation")
        self.menu_layout.addWidget(self.trajectory_generation)
        self.gridLayout.addLayout(self.menu_layout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1202, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuiew = QtWidgets.QMenu(self.menuBar)
        self.menuiew.setObjectName("menuiew")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_programm = QtWidgets.QAction(MainWindow)
        self.actionClose_programm.setObjectName("actionClose_programm")
        self.actionSimple = QtWidgets.QAction(MainWindow)
        self.actionSimple.setObjectName("actionSimple")
        self.actionDiferent = QtWidgets.QAction(MainWindow)
        self.actionDiferent.setObjectName("actionDiferent")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_programm)
        self.menuiew.addAction(self.actionSimple)
        self.menuiew.addAction(self.actionDiferent)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuiew.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.map_tab), _translate("MainWindow", "Map"))
        self.pushButton.setText(_translate("MainWindow", "Clicked on me"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings"))
        self.btn_upload.setText(_translate("MainWindow", "Upload mission"))
        self.btn_download.setText(_translate("MainWindow", "Download mission"))
        self.btn_clear.setText(_translate("MainWindow", "Clear misson"))
        self.trajectory_generation.setText(_translate("MainWindow", "Trajacroty generation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuiew.setTitle(_translate("MainWindow", "View"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose_programm.setText(_translate("MainWindow", "Close programm"))
        self.actionSimple.setText(_translate("MainWindow", "Simple"))
        self.actionDiferent.setText(_translate("MainWindow", "Diferent"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())