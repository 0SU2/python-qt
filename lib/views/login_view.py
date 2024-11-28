from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtGui import QIcon, QPixmap

from lib.static import LOGO_XS_FILE
from lib.services.auth import AuthService
from ui.compiled.loginUI import Ui_Login_Menu



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

        if AuthService.authenticate(username, password):
            # cur = connection.cursor()
            # QMessageBox.warning(self, f"Connection succes")
            self.main_view.username = username
            self.main_view.initial_state()
            self.main_view.show()
            self.close()
            return

        QMessageBox.warning(self, "Login Failed", "The username or password is incorrect")
        return
