import sys
import os
from PySide2.QtWidgets import QApplication

from lib.static import UI_FOLDER, UI_COMPILED_FOLDER

from lib.utils.ui_utils import compile_ui, compile_qrc
from lib.views.login_view import LoginView
from lib.views.main_view import MainView
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root"
)

# * APPLICATION - ENTRY POINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # * -------- COMPILE UI FILES --------
    # Compile QT.ui files to Python.py | Update changes on .ui files
    compile_ui(UI_FOLDER, UI_COMPILED_FOLDER)
    compile_qrc(UI_FOLDER, UI_COMPILED_FOLDER)

    # * --------- QT APPLICATION ---------
    # Main application
    app = QApplication(sys.argv)
    # Views
    login_view = LoginView()
    main_view = MainView()
    login_view.main_view = main_view
    main_view.login_view = login_view

    # * --------- START ---------
    login_view.show()

    sys.exit(app.exec_())
