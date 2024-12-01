# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logintestCFBqHl.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
from . import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(424, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setGeometry(QRect(10, 10, 402, 530))
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522727, y1:1, x2:0.528, y2:0, stop:0 rgba(24, 190, 183, 255), stop:0.323864 rgba(227, 238, 244, 255), stop:1 rgba(249, 249, 249, 255));\n"
"\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 20px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.button_login = QPushButton(self.dropShadowFrame)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setEnabled(True)
        self.button_login.setGeometry(QRect(70, 370, 261, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.button_login.setFont(font)
        self.button_login.setCursor(QCursor(Qt.ArrowCursor))
        self.button_login.setMouseTracking(True)
        self.button_login.setLayoutDirection(Qt.LeftToRight)
        self.button_login.setAutoFillBackground(False)
        self.button_login.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(27, 117, 183);\n"
"	text-align: center;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(24, 190, 183);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(15, 68, 106);\n"
"}")
        self.button_login.setCheckable(False)
        self.button_login.setAutoRepeat(False)
        self.button_login.setAutoExclusive(False)
        self.button_login.setAutoDefault(True)
        self.button_login.setFlat(False)
        self.text_password = QLineEdit(self.dropShadowFrame)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setEnabled(True)
        self.text_password.setGeometry(QRect(120, 310, 191, 21))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.text_password.setFont(font1)
        self.text_password.setAcceptDrops(True)
        self.text_password.setAutoFillBackground(False)
        self.text_password.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: black;")
        self.text_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.text_password.setFrame(False)
        self.text_password.setEchoMode(QLineEdit.Password)
        self.text_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_password.setDragEnabled(False)
        self.text_password.setReadOnly(False)
        self.text_password.setClearButtonEnabled(True)
        self.line_password = QFrame(self.dropShadowFrame)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(62, 340, 280, 1))
        self.line_password.setLayoutDirection(Qt.LeftToRight)
        self.line_password.setStyleSheet(u"background-color: rgb(130, 127, 148);")
        self.line_password.setFrameShadow(QFrame.Raised)
        self.line_password.setFrameShape(QFrame.HLine)
        self.line_username = QFrame(self.dropShadowFrame)
        self.line_username.setObjectName(u"line_username")
        self.line_username.setGeometry(QRect(62, 290, 280, 1))
        self.line_username.setLayoutDirection(Qt.LeftToRight)
        self.line_username.setStyleSheet(u"background-color: rgb(130, 127, 148);")
        self.line_username.setFrameShadow(QFrame.Raised)
        self.line_username.setFrameShape(QFrame.HLine)
        self.text_username = QLineEdit(self.dropShadowFrame)
        self.text_username.setObjectName(u"text_username")
        self.text_username.setEnabled(True)
        self.text_username.setGeometry(QRect(120, 260, 191, 21))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.text_username.setFont(font2)
        self.text_username.setAcceptDrops(True)
        self.text_username.setAutoFillBackground(False)
        self.text_username.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: black;")
        self.text_username.setInputMethodHints(Qt.ImhNone)
        self.text_username.setFrame(False)
        self.text_username.setEchoMode(QLineEdit.Normal)
        self.text_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_username.setDragEnabled(False)
        self.text_username.setReadOnly(False)
        self.text_username.setClearButtonEnabled(False)
        self.horizontalLayoutWidget = QWidget(self.dropShadowFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 50, 341, 141))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.img_Logo = QLabel(self.horizontalLayoutWidget)
        self.img_Logo.setObjectName(u"img_Logo")
        self.img_Logo.setLayoutDirection(Qt.LeftToRight)
        self.img_Logo.setStyleSheet(u"image: url(:/icons/assets/Logo.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.img_Logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_Logo)

        self.icon_user = QLabel(self.dropShadowFrame)
        self.icon_user.setObjectName(u"icon_user")
        self.icon_user.setGeometry(QRect(70, 260, 31, 21))
        self.icon_user.setStyleSheet(u"image: url(:/icons/assets/user-black.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.icon_lock = QLabel(self.dropShadowFrame)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setGeometry(QRect(70, 310, 31, 21))
        self.icon_lock.setStyleSheet(u"image: url(:/icons/assets/lock-black.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_close = QPushButton(self.dropShadowFrame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(360, 10, 31, 21))
        font3 = QFont()
        font3.setBold(True)
        self.button_close.setFont(font3)
        self.button_close.setStyleSheet(u"QPushButton {\n"
"   border:none;\n"
"   border-radius:8px;\n"
"   background-color: rgb(25,36,71);\n"
"   color: rgb(208, 208, 208);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(24, 190, 183);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(15, 68, 106);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_login.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.button_login.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.text_password.setInputMask("")
        self.text_password.setText("")
        self.text_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.text_username.setInputMask("")
        self.text_username.setText("")
        self.text_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.img_Logo.setText("")
        self.icon_user.setText("")
        self.icon_lock.setText("")
        self.button_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

