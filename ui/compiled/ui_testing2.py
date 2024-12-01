# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2HbECEz.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Logo = QLabel(self.frame_2)
        self.Logo.setObjectName(u"Logo")

        self.horizontalLayout_6.addWidget(self.Logo)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbUser = QLabel(self.widget_4)
        self.lbUser.setObjectName(u"lbUser")

        self.verticalLayout_2.addWidget(self.lbUser)

        self.lbCompany = QLabel(self.widget_4)
        self.lbCompany.setObjectName(u"lbCompany")

        self.verticalLayout_2.addWidget(self.lbCompany)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.btnProvider = QPushButton(self.widget)
        self.btnProvider.setObjectName(u"btnProvider")

        self.verticalLayout.addWidget(self.btnProvider)

        self.btnClient = QPushButton(self.widget)
        self.btnClient.setObjectName(u"btnClient")

        self.verticalLayout.addWidget(self.btnClient)

        self.btnProduct = QPushButton(self.widget)
        self.btnProduct.setObjectName(u"btnProduct")

        self.verticalLayout.addWidget(self.btnProduct)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnLogOut = QPushButton(self.widget_3)
        self.btnLogOut.setObjectName(u"btnLogOut")

        self.horizontalLayout_5.addWidget(self.btnLogOut)

        self.btnClose = QPushButton(self.widget_3)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_5.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_2.addWidget(self.widget)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stacked1Contenido = QStackedWidget(self.frame_3)
        self.stacked1Contenido.setObjectName(u"stacked1Contenido")
        self.tbProvider = QWidget()
        self.tbProvider.setObjectName(u"tbProvider")
        self.verticalLayout_3 = QVBoxLayout(self.tbProvider)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.tbProvider)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.tableProvider = QTableWidget(self.tbProvider)
        if (self.tableProvider.columnCount() < 6):
            self.tableProvider.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableProvider.setObjectName(u"tableProvider")
        self.tableProvider.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tableProvider)

        self.stacked1Contenido.addWidget(self.tbProvider)
        self.tbClient = QWidget()
        self.tbClient.setObjectName(u"tbClient")
        self.verticalLayout_5 = QVBoxLayout(self.tbClient)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_6 = QWidget(self.tbClient)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.tableClient = QTableWidget(self.tbClient)
        if (self.tableClient.columnCount() < 4):
            self.tableClient.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        if (self.tableClient.rowCount() < 1):
            self.tableClient.setRowCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableClient.setVerticalHeaderItem(0, __qtablewidgetitem10)
        self.tableClient.setObjectName(u"tableClient")
        self.tableClient.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient.setGridStyle(Qt.SolidLine)
        self.tableClient.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient.horizontalHeader().setStretchLastSection(True)
        self.tableClient.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tableClient)

        self.stacked1Contenido.addWidget(self.tbClient)
        self.tbProduct = QWidget()
        self.tbProduct.setObjectName(u"tbProduct")
        self.verticalLayout_6 = QVBoxLayout(self.tbProduct)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_8 = QWidget(self.tbProduct)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_3)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.tableProduct = QTableWidget(self.tbProduct)
        if (self.tableProduct.columnCount() < 5):
            self.tableProduct.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tableProduct.setObjectName(u"tableProduct")
        self.tableProduct.setAutoFillBackground(False)
        self.tableProduct.setAlternatingRowColors(False)
        self.tableProduct.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableProduct.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.tableProduct)

        self.stacked1Contenido.addWidget(self.tbProduct)

        self.verticalLayout_4.addWidget(self.stacked1Contenido)

        self.widget_5 = QWidget(self.frame_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnDeleteRow = QPushButton(self.widget_5)
        self.btnDeleteRow.setObjectName(u"btnDeleteRow")

        self.horizontalLayout_3.addWidget(self.btnDeleteRow)

        self.btnUpdateRow = QPushButton(self.widget_5)
        self.btnUpdateRow.setObjectName(u"btnUpdateRow")

        self.horizontalLayout_3.addWidget(self.btnUpdateRow)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked1Contenido.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText("")
        self.lbUser.setText("")
        self.lbCompany.setText("")
        self.btnProvider.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.btnClient.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btnProduct.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.btnLogOut.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem = self.tableProvider.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableProvider.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableProvider.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem3 = self.tableProvider.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem4 = self.tableProvider.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem5 = self.tableProvider.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem6 = self.tableClient.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tableClient.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem8 = self.tableClient.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem9 = self.tableClient.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem10 = self.tableClient.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        ___qtablewidgetitem11 = self.tableProduct.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tableProduct.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem13 = self.tableProduct.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Intensidad", None));
        ___qtablewidgetitem14 = self.tableProduct.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem15 = self.tableProduct.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Fecha de Expiracion", None));
        self.btnDeleteRow.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btnUpdateRow.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

