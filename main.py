import sys
import os
from PySide6 import QtWidgets

# from lib.views.login_view import LoginView
from lib.views.main_view import MainView
from lib.views.login_view import LoginView

if __name__ == "__main__":
    # Main application
    app = QtWidgets.QApplication(sys.argv)
    
    # Views
    # si quieres evitar el logear de usuarios, descomenta esta linea
    # login_view = LoginView()
    main_view = MainView()
    
    # y estas dos:
    # login_view.main_view = main_view
    # main_view.login_view = login_view

    # tambien comenta la main_view.show() y descomenta login_view.show()
    main_view.show()
    # login_view.show()

    app.exec()