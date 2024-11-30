from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIcon, QPixmap

from lib.static import LOGO_XS_FILE
from ui.compiled.loginUI import Ui_Login_Menu

import mysql.connector
from lib.services.server import conectar_base_datos

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()

        # * Windows
        self.main_view = None

        # * Config UI
        self.ui = Ui_Login_Menu()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(str(LOGO_XS_FILE)))
        # ! Remove window title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # * Set initial state
        self.initial_state()

        # * Connect Events
        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_login.clicked.connect(self.login)

    # * -------------- INHERIT EVENT HANDLES ---------------
    def closeEvent(self, event):
        self.initial_state()

    # * ------------ APPLICATION EVENT HANDLES ------------
    def initial_state(self):
        """ Set initial state for the window """
        self.ui.text_username.clear()
        self.ui.text_password.clear()
        self.ui.text_username.setFocus()

    def login(self):
        """ Start Log In process """
        username = self.ui.text_username.text()
        password = self.ui.text_password.text()
        print(username, password)

        self.conexion = conectar_base_datos()
        if self.conexion:
            try:
                self.cursor = self.conexion.cursor()
                self.cursor.execute("SELECT * FROM users where username = %s and password = %s", (username, password))
                result = self.cursor.fetchone()
                if result == None:
                    QMessageBox.warning(self, "Login Failed", "Invalid credentials")
                    return 
                else:
                    self.main_view.username = username
                    QMessageBox.warning(self, "Success", "Login success")
                    self.main_view.initial_state()
                    self.main_view.show()
                    self.conexion.close()
                    self.close()
                    return
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Login Failed", f"Error: {err}")
                return
