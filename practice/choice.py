# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choice.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QMainWindow, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import sys
import os
from camera import Ui_Dialog
from camera1 import Ui_Dialog2
from camera2 import Ui_Dialog3
class Ui_Dialog1(object):
    def openChoiceP(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openChoiceM(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.window)
        self.window.show()
    def openChoiceN(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 306)
        Dialog.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 381, 281))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 81, 24))
        self.pushButton.setStyleSheet(u"font:14pt \"Century Gothic\";\n"
"background-color: rgb(142, 236, 245);")
        icon = QIcon()
        icon.addFile(u"icons/arrow_back_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.pushButton.clicked.connect(Dialog.close)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 120, 211, 41))
        self.pushButton_2.setStyleSheet(u"font: 700 16pt \"Century Gothic\";\n"
"background-color: rgb(142, 236, 245);")
        self.pushButton_2.clicked.connect(self.openChoiceP)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 170, 211, 41))
        self.pushButton_3.setStyleSheet(u"font: 700 16pt \"Century Gothic\";\n"
"background-color: rgb(142, 236, 245);")
        self.pushButton_3.clicked.connect(self.openChoiceM)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 220, 211, 41))
        self.pushButton_4.setStyleSheet(u"font: 700 16pt \"Century Gothic\";\n"
"background-color: rgb(142, 236, 245);")
        self.pushButton_4.clicked.connect(self.openChoiceN)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 321, 41))
        self.label.setStyleSheet(u"font: 700 18pt \"Century Gothic\";\n"
"background-color: rgb(255, 247, 172);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u0441\u0435\u0434\u0430\u043d\u0438\u044f", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0445\u0438 \u0440\u0443\u043a\u0430\u043c\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043a\u043b\u043e\u043d\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"    \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0435:", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osanka = QtWidgets.QMainWindow()
    ui = Ui_Dialog1()
    ui.setupUi(osanka)
    osanka.show()
    sys.exit(app.exec())
