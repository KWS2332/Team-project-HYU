# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test2HJSJFQ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import Truss2_rc
import Truss2_rc

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1157, 785)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setFocusPolicy(Qt.NoFocus)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1120, 1210))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 1200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 20, 321, 41))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(15)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: white;")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 70, 1151, 16))
        self.label_11.setStyleSheet(u"background-color: rgba(54,69,79,0.6);\n"
"")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 1151, 71))
        self.label_6.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 20, 1201, 6000))
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setStyleSheet(u"background-color: white;\n"
"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 120, 191, 201))
        self.label.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label.setPixmap(QPixmap(u":/newPrefix/truss11.jpg"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(710, 120, 191, 201))
        self.label_3.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_3.setPixmap(QPixmap(u":/newPrefix/truss3.jpg"))
        self.label_3.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 120, 191, 201))
        self.label_2.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/truss2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(60, 350, 1143, 74))
        self.label_19.setAutoFillBackground(False)
        self.label_19.setStyleSheet(u"color: rgba(54,69,79);")
        self.label_19.setScaledContents(True)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(960, 610, 91, 31))
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 480, 321, 161))
        self.label_23.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_23.setPixmap(QPixmap(u":/newPrefix/truss1.png"))
        self.label_23.setScaledContents(True)
        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(390, 490, 701, 131))
        self.label_24.setStyleSheet(u"color: rgba(54,69,79);")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(-10, 450, 1171, 711))
        self.label_12.setStyleSheet(u"background-color: rgba(54,69,79,0.6);\n"
"")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(150, 700, 511, 331))
        self.label_17.setStyleSheet(u"")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(690, 710, 321, 161))
        self.label_21.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_21.setPixmap(QPixmap(u":/newPrefix/DT2.jpg"))
        self.label_21.setScaledContents(True)
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(690, 890, 321, 161))
        self.label_20.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_20.setPixmap(QPixmap(u":/newPrefix/DT.png"))
        self.label_20.setScaledContents(True)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 880, 1161, 281))
        self.label_9.setStyleSheet(u"background-color: rgba(54,69,79,0.9);\n"
"")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 670, 1161, 211))
        self.label_13.setStyleSheet(u"background-color: rgba(54,69,79,0.6);")
        self.label_10.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_11.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_19.raise_()
        self.label_12.raise_()
        self.label_24.raise_()
        self.label_23.raise_()
        self.pushButton.raise_()
        self.label_9.raise_()
        self.label_13.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.label_21.raise_()

        self.horizontalLayout.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1157, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; text-decoration: underline;\">The Truss BridgeForge</span></p></body></html>", None))
        self.label_11.setText("")
        self.label_6.setText("")
        self.label_10.setText("")
        self.label.setText("")
        self.label_3.setText("")
        self.label_2.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\ud2b8\ub7ec\uc2a4 \uad50\ub7c9\uc774\ub780?</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\ud2b8\ub7ec\uc2a4 \uad50\ub7c9\uc740 \uc0bc\uac01\ud615 \uad6c\uc870\ub85c \uc774\ub8e8\uc5b4\uc9c4 \uacac\uace0\ud55c"
                        " \ud615\ud0dc\uc758 \uad50\ub7c9\uc73c\ub85c, \ud558\uc911\uc744 \ud6a8\uc728\uc801\uc73c\ub85c \ubd84\uc0b0\uc2dc\ucf1c \ub192\uc740 \uc548\uc815\uc131\uc744 \uc790\ub791\ud569\ub2c8\ub2e4. <br />\uc774\ubc88 \ud504\ub85c\uc81d\ud2b8\uc5d0\uc11c\ub294 \ud2b9\ud788</span><span style=\" font-size:10pt;\"> </span><span style=\" font-size:10pt; color:#aa0000;\">\ub354\ube14 \uc640\ub80c \ud2b8\ub7ec\uc2a4(Double Warren Truss)</span><span style=\" font-size:10pt;\">\ub97c \uc911\uc810\uc801\uc73c\ub85c \ub2e4\ub8e8\uc5b4 \uad50\ub7c9 \uc124\uacc4\ub97c \uc9c4\ud589\ud560 \uac83 \uc785\ub2c8\ub2e4.</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc74c", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">\ub354\ube14 \uc640\ub80c \ud2b8\ub7ec\uc2a4(Double Warren Truss) \uc120\uc815 \uc774\uc720</span><span style=\" font-size:10pt; color:#ffffff;\"><br /><br />\ub354\ube14 \uc640\ub80c \ud2b8\ub7ec\uc2a4\ub294 \ub450 \uac1c\uc758 \uad50\ucc28\ub41c \uc0bc\uac01\ud615\uc774 \ubc18\ubcf5\uc801\uc73c\ub85c \ubc30\uc5f4\ub41c"
                        " \ud615\ud0dc\ub85c, \ud558\uc911 \ubd84\uc0b0\uc5d0 \uc788\uc5b4 \ud0c1\uc6d4\ud55c \ud6a8\uc728\uc131\uc744 \uc81c\uacf5\ud569\ub2c8\ub2e4.<br />\uc774 \uad6c\uc870\ub294 \ud558\uc911\uc744 \uade0\ub4f1\ud558\uac8c \ubd84\ubc30\ud558\uc5ec \uac01 \ubd80\uc7ac\uc5d0 \uac78\ub9ac\ub294 \ud798\uc744 \ucd5c\uc18c\ud654\ud558\uba70,<br />\uc7ac\ub8cc\uc758 \uc0ac\uc6a9\uc744 \ucd5c\uc801\ud654\ud558\uc5ec \uacbd\uc81c\uc131\uacfc \uac15\ub3c4\ub97c \ub3d9\uc2dc\uc5d0 \ud655\ubcf4\ud569\ub2c8\ub2e4.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">\uc774\ub97c \ud1b5\ud574 \uad6c\uc870\uc801 \uc548\uc815\uc131\uc744 \uadf9\ub300\ud654\ud558\uace0, \uae34 \uacbd\uac04\uc5d0\uc11c\ub3c4 \ub6f0\uc5b4"
                        "\ub09c \uc131\ub2a5\uc744 \ubc1c\ud718\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.</span></p></body></html>", None))
        self.label_12.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">- \uac15\ub3c4\uc640 \uc548\uc815\uc131</span><span style=\" font-size:11pt; color:#ffffff;\"><br/></span><span style=\" font-size:10pt; color:#ffffff;\">\uc0bc\uac01\ud615 \ud328\ud134\uc774 \ud558\uc911\uc744 \ud6a8\uc728\uc801\uc73c\ub85c \ubd84\uc0b0\uc2dc\ucf1c \uad6c\uc870\uc801 \uc548\uc815\uc131\uc744 \ubcf4\uc7a5\ud569\ub2c8\ub2e4.</span><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">- \uc7ac\ub8cc \ud6a8\uc728\uc131</span><span style=\" font-size:11pt; color:#ffffff;\"><br/></span><span style=\" font-size:10pt; color:#ffffff;\">\ubd80\uc7ac\uc758 \ucd5c\uc801\ud654\ub41c \ubc30\uce58\ub85c \ucd5c\uc18c\ud55c\uc758 \uc7ac\ub8cc \uc0ac\uc6a9\uc73c\ub85c \ucd5c\ub300 \uac15\ub3c4\ub97c \uad6c\ud604\ud569\ub2c8\ub2e4.</span><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">- \uc720\uc5f0"
                        "\uc131</span><span style=\" font-size:11pt; color:#ffffff;\"><br/></span><span style=\" font-size:10pt; color:#ffffff;\">\ub2e4\uc591\ud55c \uc2a4\ud32c \uae38\uc774\uc640 \ud558\uc911 \uc870\uac74\uc5d0 \uc801\uc751\ud560 \uc218 \uc788\uc5b4 \ub2e4\uc591\ud55c \ud504\ub85c\uc81d\ud2b8\uc5d0 \uc801\uc6a9 \uac00\ub2a5\ud569\ub2c8\ub2e4.</span><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">- \uacbd\uc81c\uc131</span><span style=\" font-size:11pt; color:#ffffff;\"><br/></span><span style=\" font-size:10pt; color:#ffffff;\">\uc7ac\ub8cc \uc808\uac10\uacfc \uac04\ub2e8\ud55c \uc124\uacc4\ub85c \uac74\uc124 \ube44\uc6a9\uc744 \ub0ae\ucd9c \uc218 \uc788\uc2b5\ub2c8\ub2e4.</span><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">- \ub0b4\uad6c\uc131</span><span style=\" font-size:11pt; color:#ffffff;\"><br/></span><span style=\" font-size:10pt; color:#ffffff;\">\uc2dc\uac04\uc774 \uc9c0"
                        "\ub098\ub3c4 \uad6c\uc870\uc801 \ubcc0\ud615\uc774 \uc801\uace0, \uc720\uc9c0\ubcf4\uc218 \ube44\uc6a9\uc774 \ub0ae\uc2b5\ub2c8\ub2e4.</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_20.setText("")
        self.label_9.setText("")
        self.label_13.setText("")
    # retranslateUi

