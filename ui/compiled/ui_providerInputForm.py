# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'providerInputFormFDSSRS.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_providerAdd(object):
    def setupUi(self, providerAdd):
        if not providerAdd.objectName():
            providerAdd.setObjectName(u"providerAdd")
        providerAdd.resize(407, 639)
        self.horizontalLayout_2 = QHBoxLayout(providerAdd)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(providerAdd)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.textName = QPlainTextEdit(self.frame_4)
        self.textName.setObjectName(u"textName")

        self.verticalLayout_2.addWidget(self.textName)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textContact = QPlainTextEdit(self.frame_4)
        self.textContact.setObjectName(u"textContact")

        self.verticalLayout_2.addWidget(self.textContact)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.textPhone = QPlainTextEdit(self.frame_4)
        self.textPhone.setObjectName(u"textPhone")

        self.verticalLayout_2.addWidget(self.textPhone)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEmail = QPlainTextEdit(self.frame_4)
        self.textEmail.setObjectName(u"textEmail")

        self.verticalLayout_2.addWidget(self.textEmail)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.textAddres = QPlainTextEdit(self.frame_4)
        self.textAddres.setObjectName(u"textAddres")

        self.verticalLayout_2.addWidget(self.textAddres)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.widget_2)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnOk = QPushButton(self.widget_2)
        self.btnOk.setObjectName(u"btnOk")

        self.horizontalLayout.addWidget(self.btnOk)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.widget)

        self.frame_3 = QFrame(providerAdd)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.retranslateUi(providerAdd)

        QMetaObject.connectSlotsByName(providerAdd)
    # setupUi

    def retranslateUi(self, providerAdd):
        providerAdd.setWindowTitle(QCoreApplication.translate("providerAdd", u"Form", None))
        self.label.setText(QCoreApplication.translate("providerAdd", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("providerAdd", u"Contacto", None))
        self.label_3.setText(QCoreApplication.translate("providerAdd", u"Telefono", None))
        self.label_4.setText(QCoreApplication.translate("providerAdd", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("providerAdd", u"Direccion", None))
        self.btnCancel.setText(QCoreApplication.translate("providerAdd", u"Cancelar", None))
        self.btnOk.setText(QCoreApplication.translate("providerAdd", u"OK", None))
    # retranslateUi

