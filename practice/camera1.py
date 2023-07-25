# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import sys
import os

class Ui_Dialog2(object):
    def open_mahi(self):
        os.system('python mahi.py')
    def open_mahiN(self):
        os.system('python mahiN.py')
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(431, 276)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 451, 281))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 140, 131, 61))
        self.pushButton.setStyleSheet(u"background-color: rgb(185,251,192);\n"
"font: 700 18pt \"Century Gothic\";")
        icon = QIcon()
        icon.addFile(u"../../Users/user/Downloads/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.clicked.connect(self.open_mahi)
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 140, 131, 61))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(145,236,245);\n"
"font: 700 18pt \"Century Gothic\";")
        icon1 = QIcon()
        icon1.addFile(u"../../Users/user/Downloads/no-video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.clicked.connect(self.open_mahiN)
        self.pushButton_2.clicked.connect(Dialog.close)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 371, 51))
        self.label.setStyleSheet(u"font: 700 12pt \"Century Gothic\";\n"
"background-color: rgb(255, 247,172);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.label.setText(QCoreApplication.translate("Dialog", u" \u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f?", None))
    # retranslateUi

