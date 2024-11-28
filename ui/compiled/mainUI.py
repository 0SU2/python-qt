# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 674)
        MainWindow.setMinimumSize(QSize(150, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frameMain = QFrame(self.centralwidget)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout = QHBoxLayout(self.frameMain)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.framePanel = QFrame(self.frameMain)
        self.framePanel.setObjectName(u"framePanel")
        self.framePanel.setAutoFillBackground(False)
        self.framePanel.setStyleSheet(u"QFrame {\n"
"background-color: rgb(0,0,0  );\n"
"}")
        self.framePanel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.framePanel.setFrameShape(QFrame.NoFrame)
        self.framePanel.setFrameShadow(QFrame.Raised)
        self.framePanel.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.framePanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameIPS = QFrame(self.framePanel)
        self.frameIPS.setObjectName(u"frameIPS")
        self.frameIPS.setStyleSheet(u"QFrame {\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 10px;\n"
"}")
        self.frameIPS.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameIPS.setFrameShape(QFrame.Panel)
        self.frameIPS.setFrameShadow(QFrame.Sunken)
        self.frameIPS.setLineWidth(3)
        self.frameIPS.setMidLineWidth(3)
        self.horizontalLayout_3 = QHBoxLayout(self.frameIPS)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblLogoCompany = QLabel(self.frameIPS)
        self.lblLogoCompany.setObjectName(u"lblLogoCompany")
        self.lblLogoCompany.setMinimumSize(QSize(50, 50))
        self.lblLogoCompany.setMaximumSize(QSize(50, 50))
        self.lblLogoCompany.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lblLogoCompany.setPixmap(QPixmap(u":/icons/assets/logo-xs.png"))
        self.lblLogoCompany.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lblLogoCompany)

        self.VLayoutCompany = QVBoxLayout()
        self.VLayoutCompany.setObjectName(u"VLayoutCompany")
        self.lblUser = QLabel(self.frameIPS)
        self.lblUser.setObjectName(u"lblUser")
        self.lblUser.setMaximumSize(QSize(300, 300))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblUser.setFont(font)
        self.lblUser.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lblUser.setAlignment(Qt.AlignCenter)
        self.lblUser.setWordWrap(True)

        self.VLayoutCompany.addWidget(self.lblUser)

        self.lblCompany = QLabel(self.frameIPS)
        self.lblCompany.setObjectName(u"lblCompany")
        self.lblCompany.setMaximumSize(QSize(300, 300))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.lblCompany.setFont(font1)
        self.lblCompany.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lblCompany.setAlignment(Qt.AlignCenter)
        self.lblCompany.setWordWrap(True)

        self.VLayoutCompany.addWidget(self.lblCompany)


        self.horizontalLayout_3.addLayout(self.VLayoutCompany)


        self.verticalLayout.addWidget(self.frameIPS)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.framePanel)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(6)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	text-align: center;\n"
"	color: white;\n"
"	border: none;\n"
"}")
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frameLineNav = QFrame(self.framePanel)
        self.frameLineNav.setObjectName(u"frameLineNav")
        self.frameLineNav.setMinimumSize(QSize(0, 3))
        self.frameLineNav.setMaximumSize(QSize(16777215, 3))
        self.frameLineNav.setStyleSheet(u"QFrame{\n"
"    border: none;\n"
"    background: white;\n"
"}")
        self.frameLineNav.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameLineNav.setFrameShape(QFrame.StyledPanel)
        self.frameLineNav.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameLineNav)

        self.scrollAreaMenuLateral = QScrollArea(self.framePanel)
        self.scrollAreaMenuLateral.setObjectName(u"scrollAreaMenuLateral")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaMenuLateral.sizePolicy().hasHeightForWidth())
        self.scrollAreaMenuLateral.setSizePolicy(sizePolicy1)
        self.scrollAreaMenuLateral.setMaximumSize(QSize(300, 16777215))
        self.scrollAreaMenuLateral.setStyleSheet(u"QScrollArea {\n"
"background-color: rgb(0,0,0);\n"
"border: 0px solid rgb(53,73,154  );\n"
"}\n"
"")
        self.scrollAreaMenuLateral.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.scrollAreaMenuLateral.setLineWidth(0)
        self.scrollAreaMenuLateral.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaMenuLateral.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollAreaMenuLateral.setWidgetResizable(True)
        self.saNavBar = QWidget()
        self.saNavBar.setObjectName(u"saNavBar")
        self.saNavBar.setGeometry(QRect(0, 0, 300, 440))
        self.saNavBar.setStyleSheet(u"QWidget {\n"
"background-color: rgb(0,0,0);\n"
"border: 0px solid rgb(53,73,154  );\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.saNavBar)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btnNavHome = QPushButton(self.saNavBar)
        self.btnNavHome.setObjectName(u"btnNavHome")
        self.btnNavHome.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btnNavHome.sizePolicy().hasHeightForWidth())
        self.btnNavHome.setSizePolicy(sizePolicy)
        self.btnNavHome.setMinimumSize(QSize(0, 40))
        self.btnNavHome.setFont(font1)
        self.btnNavHome.setLayoutDirection(Qt.LeftToRight)
        self.btnNavHome.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"	border-left: 0px solid rgb(27, 29, 35);\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	text-align: left;\n"
"	color: white;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(119, 156, 171);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(53, 82, 74);\n"
"}\n"
"QPushButton:checked {\n"
"	border-bottom: 1px solid rgb(255,255,255);\n"
"	background-color: rgb(25,36,71);\n"
"}")
        self.btnNavHome.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/cil-view-quilt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNavHome.setIcon(icon)
        self.btnNavHome.setIconSize(QSize(20, 20))
        self.btnNavHome.setCheckable(True)
        self.btnNavHome.setChecked(False)
        self.btnNavHome.setAutoDefault(False)

        self.verticalLayout_10.addWidget(self.btnNavHome)

        self.btnNavManageFiles = QPushButton(self.saNavBar)
        self.btnNavManageFiles.setObjectName(u"btnNavManageFiles")
        self.btnNavManageFiles.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btnNavManageFiles.sizePolicy().hasHeightForWidth())
        self.btnNavManageFiles.setSizePolicy(sizePolicy)
        self.btnNavManageFiles.setMinimumSize(QSize(0, 50))
        self.btnNavManageFiles.setFont(font1)
        self.btnNavManageFiles.setLayoutDirection(Qt.LeftToRight)
        self.btnNavManageFiles.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"	border-left: 0px solid rgb(27, 29, 35);\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	text-align: left;\n"
"	color: white;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(119, 156, 171);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(53, 82, 74);\n"
"}\n"
"QPushButton:checked {\n"
"	border-bottom: 1px solid rgb(255,255,255);\n"
"	background-color: rgb(25,36,71);\n"
"}")
        self.btnNavManageFiles.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNavManageFiles.setIcon(icon1)
        self.btnNavManageFiles.setIconSize(QSize(50, 50))
        self.btnNavManageFiles.setCheckable(True)
        self.btnNavManageFiles.setChecked(False)
        self.btnNavManageFiles.setAutoDefault(False)

        self.verticalLayout_10.addWidget(self.btnNavManageFiles)

        self.btnNavSearch = QPushButton(self.saNavBar)
        self.btnNavSearch.setObjectName(u"btnNavSearch")
        self.btnNavSearch.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btnNavSearch.sizePolicy().hasHeightForWidth())
        self.btnNavSearch.setSizePolicy(sizePolicy)
        self.btnNavSearch.setMinimumSize(QSize(0, 40))
        self.btnNavSearch.setFont(font1)
        self.btnNavSearch.setLayoutDirection(Qt.LeftToRight)
        self.btnNavSearch.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"	border-left: 0px solid rgb(27, 29, 35);\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	text-align: left;\n"
"	color: white;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(119, 156, 171);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(53, 82, 74);\n"
"}\n"
"QPushButton:checked {\n"
"	border-bottom: 1px solid rgb(255,255,255);\n"
"	background-color: rgb(25,36,71);\n"
"}")
        self.btnNavSearch.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNavSearch.setIcon(icon2)
        self.btnNavSearch.setIconSize(QSize(20, 20))
        self.btnNavSearch.setCheckable(True)
        self.btnNavSearch.setChecked(False)
        self.btnNavSearch.setAutoDefault(False)

        self.verticalLayout_10.addWidget(self.btnNavSearch)

        self.verticalSpacer_2 = QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.scrollAreaMenuLateral.setWidget(self.saNavBar)

        self.verticalLayout.addWidget(self.scrollAreaMenuLateral)

        self.HLayoutBtnInf = QHBoxLayout()
        self.HLayoutBtnInf.setSpacing(0)
        self.HLayoutBtnInf.setObjectName(u"HLayoutBtnInf")
        self.btnLogout = QPushButton(self.framePanel)
        self.btnLogout.setObjectName(u"btnLogout")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnLogout.sizePolicy().hasHeightForWidth())
        self.btnLogout.setSizePolicy(sizePolicy2)
        self.btnLogout.setMinimumSize(QSize(50, 50))
        self.btnLogout.setMaximumSize(QSize(50, 50))
        self.btnLogout.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"	border-left: 0px solid rgb(27, 29, 35);\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"	color: white;\n"
"	padding-left: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(119, 156, 171);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(53, 82, 74);\n"
"}")
        self.btnLogout.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/cil-exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogout.setIcon(icon3)
        self.btnLogout.setIconSize(QSize(35, 35))
        self.btnLogout.setCheckable(False)
        self.btnLogout.setChecked(False)

        self.HLayoutBtnInf.addWidget(self.btnLogout)

        self.btnExit = QPushButton(self.framePanel)
        self.btnExit.setObjectName(u"btnExit")
        sizePolicy2.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy2)
        self.btnExit.setMinimumSize(QSize(50, 50))
        self.btnExit.setMaximumSize(QSize(50, 50))
        self.btnExit.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"	border-left: 0px solid rgb(27, 29, 35);\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"	color: white;\n"
"	padding-left: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(119, 156, 171);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(53, 82, 74);\n"
"}")
        self.btnExit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExit.setIcon(icon4)
        self.btnExit.setIconSize(QSize(35, 35))
        self.btnExit.setCheckable(False)
        self.btnExit.setChecked(False)

        self.HLayoutBtnInf.addWidget(self.btnExit)

        self.btnAbout = QPushButton(self.framePanel)
        self.btnAbout.setObjectName(u"btnAbout")
        sizePolicy2.setHeightForWidth(self.btnAbout.sizePolicy().hasHeightForWidth())
        self.btnAbout.setSizePolicy(sizePolicy2)
        self.btnAbout.setMinimumSize(QSize(50, 50))
        self.btnAbout.setMaximumSize(QSize(50, 50))
        self.btnAbout.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"	border-left: 0px solid rgb(27, 29, 35);\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"	color: white;\n"
"	padding-left: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(119, 156, 171);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 0px solid rgb(255,255,255);\n"
"	background-color: rgb(53, 82, 74);\n"
"}")
        self.btnAbout.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/cil-options.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAbout.setIcon(icon5)
        self.btnAbout.setIconSize(QSize(35, 35))
        self.btnAbout.setCheckable(False)
        self.btnAbout.setChecked(False)

        self.HLayoutBtnInf.addWidget(self.btnAbout)


        self.verticalLayout.addLayout(self.HLayoutBtnInf)


        self.horizontalLayout.addWidget(self.framePanel)

        self.frameSombra = QFrame(self.frameMain)
        self.frameSombra.setObjectName(u"frameSombra")
        self.frameSombra.setMinimumSize(QSize(20, 0))
        self.frameSombra.setMaximumSize(QSize(20, 16777215))
        self.frameSombra.setStyleSheet(u"QFrame#frameSombra{\n"
"    border: none;\n"
"    background: qlineargradient( x1:0 y1:0, x2:0.75 y2:0, stop:0 rgb(170,170,170), stop:1 white);\n"
"}")
        self.frameSombra.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameSombra.setFrameShape(QFrame.StyledPanel)
        self.frameSombra.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frameSombra)

        self.frameContent = QFrame(self.frameMain)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setMinimumSize(QSize(0, 0))
        self.frameContent.setStyleSheet(u"QFrame#frameContent {	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frameContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_2 = QVBoxLayout(self.frameContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.stacked1Contenido = QStackedWidget(self.frameContent)
        self.stacked1Contenido.setObjectName(u"stacked1Contenido")
        self.stacked1Contenido.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.sw1Welcome = QWidget()
        self.sw1Welcome.setObjectName(u"sw1Welcome")
        self.verticalLayout_5 = QVBoxLayout(self.sw1Welcome)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lblWelcome = QLabel(self.sw1Welcome)
        self.lblWelcome.setObjectName(u"lblWelcome")
        self.lblWelcome.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.lblWelcome)

        self.lblWelcomeText = QLabel(self.sw1Welcome)
        self.lblWelcomeText.setObjectName(u"lblWelcomeText")
        self.lblWelcomeText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lblWelcomeText.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.lblWelcomeText)

        self.stacked1Contenido.addWidget(self.sw1Welcome)
        self.sw1Files = QWidget()
        self.sw1Files.setObjectName(u"sw1Files")
        self.verticalLayout_6 = QVBoxLayout(self.sw1Files)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.sw1Files)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(13, 70))
        self.label_2.setMaximumSize(QSize(13, 16777215))
        self.label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_2.setPixmap(QPixmap(u":/icons/assets/vin.png"))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lblListAllFiles = QLabel(self.sw1Files)
        self.lblListAllFiles.setObjectName(u"lblListAllFiles")
        self.lblListAllFiles.setMinimumSize(QSize(0, 70))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.lblListAllFiles.setFont(font3)
        self.lblListAllFiles.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_5.addWidget(self.lblListAllFiles)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.twListAllFiles = QTableWidget(self.sw1Files)
        if (self.twListAllFiles.columnCount() < 3):
            self.twListAllFiles.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.twListAllFiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twListAllFiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twListAllFiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.twListAllFiles.rowCount() < 2):
            self.twListAllFiles.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twListAllFiles.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twListAllFiles.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twListAllFiles.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.twListAllFiles.setItem(0, 1, __qtablewidgetitem6)
        self.twListAllFiles.setObjectName(u"twListAllFiles")
        self.twListAllFiles.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.twListAllFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twListAllFiles.setSelectionMode(QAbstractItemView.SingleSelection)
        self.twListAllFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twListAllFiles.setGridStyle(Qt.SolidLine)
        self.twListAllFiles.horizontalHeader().setMinimumSectionSize(200)
        self.twListAllFiles.horizontalHeader().setDefaultSectionSize(250)
        self.twListAllFiles.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.twListAllFiles)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnFilesDelete = QPushButton(self.sw1Files)
        self.btnFilesDelete.setObjectName(u"btnFilesDelete")
        self.btnFilesDelete.setEnabled(False)
        self.btnFilesDelete.setMinimumSize(QSize(150, 37))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.btnFilesDelete.setFont(font4)
        self.btnFilesDelete.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(173, 8, 76);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(228, 76, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(119, 0, 37);\n"
"}\n"
"")
        self.btnFilesDelete.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_14.addWidget(self.btnFilesDelete)

        self.btnFilesUpload = QPushButton(self.sw1Files)
        self.btnFilesUpload.setObjectName(u"btnFilesUpload")
        self.btnFilesUpload.setMinimumSize(QSize(150, 37))
        self.btnFilesUpload.setFont(font4)
        self.btnFilesUpload.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,167,208);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(21,210,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,128,158);\n"
"}")
        self.btnFilesUpload.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_14.addWidget(self.btnFilesUpload)

        self.horizontalSpacer_6 = QSpacerItem(40, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.btnFilesOpen = QPushButton(self.sw1Files)
        self.btnFilesOpen.setObjectName(u"btnFilesOpen")
        self.btnFilesOpen.setMinimumSize(QSize(250, 37))
        self.btnFilesOpen.setFont(font4)
        self.btnFilesOpen.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,167,208);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(21,210,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,128,158);\n"
"}")
        self.btnFilesOpen.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_14.addWidget(self.btnFilesOpen)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.stacked1Contenido.addWidget(self.sw1Files)
        self.sw1ManGui = QWidget()
        self.sw1ManGui.setObjectName(u"sw1ManGui")
        self.verticalLayout_7 = QVBoxLayout(self.sw1ManGui)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox = QGroupBox(self.sw1ManGui)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(800, 150))
        font5 = QFont()
        font5.setPointSize(11)
        self.groupBox.setFont(font5)
        self.groupBox.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setPointSize(10)
        self.label_8.setFont(font6)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.cbFilterType = QComboBox(self.groupBox)
        self.cbFilterType.addItem("")
        self.cbFilterType.setObjectName(u"cbFilterType")
        self.cbFilterType.setMinimumSize(QSize(0, 20))
        self.cbFilterType.setFont(font6)

        self.gridLayout_2.addWidget(self.cbFilterType, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.cbFilterExtension = QComboBox(self.groupBox)
        self.cbFilterExtension.addItem("")
        self.cbFilterExtension.setObjectName(u"cbFilterExtension")
        self.cbFilterExtension.setMinimumSize(QSize(0, 20))
        self.cbFilterExtension.setFont(font6)

        self.gridLayout_2.addWidget(self.cbFilterExtension, 1, 1, 1, 1)

        self.btnFilterReset = QPushButton(self.groupBox)
        self.btnFilterReset.setObjectName(u"btnFilterReset")
        self.btnFilterReset.setMinimumSize(QSize(250, 33))
        self.btnFilterReset.setMaximumSize(QSize(250, 16777215))
        self.btnFilterReset.setFont(font4)
        self.btnFilterReset.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,167,208);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	padding-left: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(21,210,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,128,158);\n"
"}")

        self.gridLayout_2.addWidget(self.btnFilterReset, 4, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.lblFilterFileSize = QLabel(self.groupBox)
        self.lblFilterFileSize.setObjectName(u"lblFilterFileSize")
        self.lblFilterFileSize.setFont(font6)
        self.lblFilterFileSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lblFilterFileSize)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.hsFilterFileSize = QSlider(self.groupBox)
        self.hsFilterFileSize.setObjectName(u"hsFilterFileSize")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.hsFilterFileSize.sizePolicy().hasHeightForWidth())
        self.hsFilterFileSize.setSizePolicy(sizePolicy3)
        self.hsFilterFileSize.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hsFilterFileSize, 3, 1, 1, 1)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.sw1ManGui)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(13, 40))
        self.label_4.setMaximumSize(QSize(13, 40))
        self.label_4.setPixmap(QPixmap(u":/icons/assets/vin.png"))

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lblList = QLabel(self.sw1ManGui)
        self.lblList.setObjectName(u"lblList")
        self.lblList.setMinimumSize(QSize(0, 40))
        self.lblList.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setPointSize(12)
        self.lblList.setFont(font7)

        self.horizontalLayout_6.addWidget(self.lblList)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.twListFiles = QTableWidget(self.sw1ManGui)
        if (self.twListFiles.columnCount() < 3):
            self.twListFiles.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twListFiles.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.twListFiles.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.twListFiles.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        if (self.twListFiles.rowCount() < 2):
            self.twListFiles.setRowCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.twListFiles.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.twListFiles.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.twListFiles.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.twListFiles.setItem(0, 1, __qtablewidgetitem13)
        self.twListFiles.setObjectName(u"twListFiles")
        self.twListFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twListFiles.setSelectionMode(QAbstractItemView.SingleSelection)
        self.twListFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twListFiles.setGridStyle(Qt.SolidLine)
        self.twListFiles.horizontalHeader().setMinimumSectionSize(200)
        self.twListFiles.horizontalHeader().setDefaultSectionSize(250)
        self.twListFiles.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.twListFiles)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btnSearchDelete = QPushButton(self.sw1ManGui)
        self.btnSearchDelete.setObjectName(u"btnSearchDelete")
        self.btnSearchDelete.setEnabled(True)
        self.btnSearchDelete.setMinimumSize(QSize(150, 37))
        self.btnSearchDelete.setFont(font4)
        self.btnSearchDelete.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(173, 8, 76);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(228, 76, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(119, 0, 37);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.btnSearchDelete)

        self.btnSearchUpload = QPushButton(self.sw1ManGui)
        self.btnSearchUpload.setObjectName(u"btnSearchUpload")
        self.btnSearchUpload.setMinimumSize(QSize(150, 37))
        self.btnSearchUpload.setFont(font4)
        self.btnSearchUpload.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,167,208);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(21,210,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,128,158);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btnSearchUpload)

        self.horizontalSpacer_5 = QSpacerItem(40, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.btnSearchOpen = QPushButton(self.sw1ManGui)
        self.btnSearchOpen.setObjectName(u"btnSearchOpen")
        self.btnSearchOpen.setMinimumSize(QSize(250, 37))
        self.btnSearchOpen.setFont(font4)
        self.btnSearchOpen.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,167,208);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(21,210,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,128,158);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btnSearchOpen)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.stacked1Contenido.addWidget(self.sw1ManGui)

        self.verticalLayout_2.addWidget(self.stacked1Contenido)


        self.horizontalLayout.addWidget(self.frameContent)


        self.verticalLayout_4.addWidget(self.frameMain)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked1Contenido.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblLogoCompany.setText("")
        self.lblUser.setText(QCoreApplication.translate("MainWindow", u"USER", None))
        self.lblCompany.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>COMPANY</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NAVIGATION BAR", None))
        self.btnNavHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(shortcut)
        self.btnNavHome.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.btnNavManageFiles.setText(QCoreApplication.translate("MainWindow", u"Manage Files", None))
#if QT_CONFIG(shortcut)
        self.btnNavManageFiles.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.btnNavSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(shortcut)
        self.btnNavSearch.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btnLogout.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Logout</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnLogout.setText("")
#if QT_CONFIG(tooltip)
        self.btnExit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Exit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnExit.setText("")
#if QT_CONFIG(tooltip)
        self.btnAbout.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>About...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnAbout.setText("")
        self.lblWelcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p><p><img src=\":/icons/assets/Logo.png\"/></p></body></html>", None))
        self.lblWelcomeText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><span style=\" font-size:16pt; font-weight:600;\">\u00a1Welcome!</span></p><p><span style=\" font-size:12pt;\">Select an entry from the navigation bar to start.</span></p></body></html>", None))
        self.lblListAllFiles.setText(QCoreApplication.translate("MainWindow", u"List of stored files", None))
        ___qtablewidgetitem = self.twListAllFiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem1 = self.twListAllFiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"FECHA", None));
        ___qtablewidgetitem2 = self.twListAllFiles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"SIZE", None));
        ___qtablewidgetitem3 = self.twListAllFiles.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.twListAllFiles.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.twListAllFiles.isSortingEnabled()
        self.twListAllFiles.setSortingEnabled(False)
        self.twListAllFiles.setSortingEnabled(__sortingEnabled)

        self.btnFilesDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btnFilesUpload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.btnFilesOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Extension", None))
        self.cbFilterType.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.cbFilterExtension.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.btnFilterReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.lblFilterFileSize.setText(QCoreApplication.translate("MainWindow", u"<1MB", None))
        self.lblList.setText(QCoreApplication.translate("MainWindow", u"List of stored files", None))
        ___qtablewidgetitem5 = self.twListFiles.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem6 = self.twListFiles.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem7 = self.twListFiles.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"SIZE", None));
        ___qtablewidgetitem8 = self.twListFiles.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.twListFiles.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled1 = self.twListFiles.isSortingEnabled()
        self.twListFiles.setSortingEnabled(False)
        self.twListFiles.setSortingEnabled(__sortingEnabled1)

        self.btnSearchDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btnSearchUpload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.btnSearchOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
    # retranslateUi

