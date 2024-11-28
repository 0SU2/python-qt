from PySide2.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PySide2.QtGui import QIcon, QPixmap

from lib.static import LOGO_FILE, LOGO_XS_FILE, MSG_ABOUT
from ui.compiled.mainUI import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        # * Windows
        self.login_view = None

        # * Config UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Python Qt Dashboard Example")
        self.setWindowIcon(QIcon(str(LOGO_XS_FILE)))

        # * Set initial state
        self.username = None
        self.initial_state()

        # * Connect Events
        self.ui.btnNavHome.clicked.connect(lambda: self.change_main_page(self.ui.btnNavHome, 0,))
        self.ui.btnNavManageFiles.clicked.connect(lambda: self.change_main_page(self.ui.btnNavManageFiles, 1,))
        self.ui.btnNavSearch.clicked.connect(lambda: self.change_main_page(self.ui.btnNavSearch, 2,))

        self.ui.btnExit.clicked.connect(self.close)
        self.ui.btnLogout.clicked.connect(self.logout)
        self.ui.btnAbout.clicked.connect(self.about)

    # * -------------- INHERIT EVENT HANDLES ---------------
    def closeEvent(self, event):
        self.initial_state()

    # * ------------ APPLICATION EVENT HANDLES ------------
    def initial_state(self):
        """ Set initial state for the window """
        self.ui.lblUser.setText(self.username if self.username is not None else "USER")
        self.ui.stacked1Contenido.setCurrentIndex(0)
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)

    def change_main_page(self, pressed_btn_nav, stack1_index):
        # * Alternate state for each btnNav button
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)
        pressed_btn_nav.setChecked(True)
        # * Set active the selected page
        self.ui.stacked1Contenido.setCurrentIndex(stack1_index)

    def logout(self):
        self.login_view.initial_state()
        self.login_view.show()
        self.close()

    def about(self):
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap(str(LOGO_FILE)))
        msg.setWindowIcon(QIcon(str(LOGO_XS_FILE)))
        msg.setFixedWidth(250)
        msg.setWindowTitle("About Us")
        msg.setText(f'Version: 0.1.0')
        msg.setInformativeText(MSG_ABOUT)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
