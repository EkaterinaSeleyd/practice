# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtWidgets
import mediapipe as mp
import os
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import res_rc
from choice import Ui_Dialog1
from subprocess import call

class Ui_MainWindow(object):
    def open_progr(self):
        os.system('python pose.py')
    def openChoice(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 532)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 120, 321, 371))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(142, 236, 245);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/online-training.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(170, 185))

        self.pushButton_2.clicked.connect(self.openChoice)
        #self.pushButton_2.clicked.connect(MainWindow.close)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 120, 321, 371))
        self.pushButton.setStyleSheet(u"background-color: rgb(185,251,192);\n"
"font: 700 16pt \"Century Gothic\";")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/body.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(150, 150))
        self.pushButton.setCheckable(False)

        self.pushButton.clicked.connect(self.open_progr)
        #self.pushButton.clicked.connect(self.openOsanka)
        #self.pushButton.clicked.connect(MainWindow.close)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 651, 71))
        self.label.setStyleSheet(u"background-color: rgb(255, 247, 172);\n"
"font: 700 18pt \"Century Gothic\";\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 430, 261, 31))
        self.label_2.setStyleSheet(u"background-color: rgb(185,251,192);\n"
"font: 700 16pt \"Century Gothic\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 430, 291, 31))
        self.label_3.setStyleSheet(u"background-color: rgb(142, 236, 245);\n"
"font: 700 16pt \"Century Gothic\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SpineApp", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"                 \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435, \u0447\u0435\u043c \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0437\u0430\u043d\u044f\u0442\u044c\u0441\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435 \u043e\u0441\u0430\u043d\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" \u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0439", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(ui_main)
    ui_main.show()
    sys.exit(app.exec())