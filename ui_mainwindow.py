# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 328)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.user_score = QLineEdit(self.centralwidget)
        self.user_score.setObjectName(u"user_score")
        self.user_score.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.user_score, 7, 2, 1, 2)

        self.girl = QLineEdit(self.centralwidget)
        self.girl.setObjectName(u"girl")
        self.girl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.girl, 2, 0, 1, 1)

        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 0, 127);")
        icon = QIcon()
        icon.addFile(u"pic/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QSize(47, 57))

        self.gridLayout.addWidget(self.btn_back, 5, 2, 1, 1)

        self.btn_boy = QPushButton(self.centralwidget)
        self.btn_boy.setObjectName(u"btn_boy")
        icon1 = QIcon()
        icon1.addFile(u"pic/icons8-boy-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_boy.setIcon(icon1)
        self.btn_boy.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_boy, 1, 7, 1, 1)

        self.user = QLineEdit(self.centralwidget)
        self.user.setObjectName(u"user")
        self.user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.user, 4, 2, 1, 2)

        self.boy_score = QLineEdit(self.centralwidget)
        self.boy_score.setObjectName(u"boy_score")
        self.boy_score.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.boy_score, 3, 7, 1, 1)

        self.girl_score = QLineEdit(self.centralwidget)
        self.girl_score.setObjectName(u"girl_score")
        self.girl_score.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.girl_score, 3, 0, 1, 1)

        self.btn_roo = QPushButton(self.centralwidget)
        self.btn_roo.setObjectName(u"btn_roo")
        self.btn_roo.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 0, 127);")
        icon2 = QIcon()
        icon2.addFile(u"pic/on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_roo.setIcon(icon2)
        self.btn_roo.setIconSize(QSize(47, 57))

        self.gridLayout.addWidget(self.btn_roo, 5, 3, 1, 1)

        self.btn_girl = QPushButton(self.centralwidget)
        self.btn_girl.setObjectName(u"btn_girl")
        icon3 = QIcon()
        icon3.addFile(u"pic/icons8-girl-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_girl.setIcon(icon3)
        self.btn_girl.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_girl, 1, 0, 1, 1)

        self.boy = QLineEdit(self.centralwidget)
        self.boy.setObjectName(u"boy")
        self.boy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.boy, 2, 7, 1, 1)

        self.result = QLineEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(14)
        font.setBold(True)
        self.result.setFont(font)
        self.result.setStyleSheet(u"border-bottom-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(170, 0, 127);\n"
"border-radius:10px;")
        self.result.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result, 0, 1, 3, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 390, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.user_score.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your score", None))
        self.btn_back.setText("")
        self.btn_boy.setText("")
        self.boy_score.setText("")
        self.boy_score.setPlaceholderText(QCoreApplication.translate("MainWindow", u"His score", None))
        self.girl_score.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Her score", None))
        self.btn_roo.setText("")
        self.btn_girl.setText("")
    # retranslateUi

