import sys
'''
import os
import time
import pathlib
import wave
import numpy as np
import math
import cv2
import shutil
from math import ceil
from subprocess import call,STDOUT
from tqdm import tqdm
from stegano import lsb
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, \
    QPushButton, QMainWindow, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 241, 17))
        self.label_2.setStyleSheet("font: 9pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.browse_2 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_2.setGeometry(QtCore.QRect(250, 130, 89, 25))
        self.browse_2.setObjectName("browse_2")
        self.browse_2.findChild(QPushButton, 'browse_2')
#        self.browse_2.clicked.connect(self.clicker)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(0, 250, 371, 23))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_2.setAutoFillBackground(False)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.logo_2 = QtWidgets.QLabel(self.centralwidget)
        self.logo_2.setGeometry(QtCore.QRect(60, 0, 251, 81))
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap("./logo.png"))
        self.logo_2.setObjectName("logo_2")
        self.filename_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.filename_2.setGeometry(QtCore.QRect(10, 130, 221, 25))
        self.filename_2.setObjectName("filename_2")
        self.btnencrypt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnencrypt_2.setGeometry(QtCore.QRect(170, 190, 131, 41))
        self.btnencrypt_2.setObjectName("btnencrypt_2")
        self.btncrypt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btncrypt_2.setGeometry(QtCore.QRect(20, 190, 131, 41))
        self.btncrypt_2.setObjectName("btncrypt_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Укажите путь к файлу:"))
        self.browse_2.setText(_translate("MainWindow", "Обзор..."))
        self.btnencrypt_2.setText(_translate("MainWindow", "Дешифровать"))
        self.btncrypt_2.setText(_translate("MainWindow", "Зашифровать"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # !!! тут ваша логика 
        
        self.browse_2.clicked.connect(self.clicker)           # !!!

    def clicker(self):                                        # !!!
        res, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            'Open File', 
            './', 
            '(*.jpg)'                                         # !!!
        )
        if res:
            self.filename_2.setText(res)
        

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())