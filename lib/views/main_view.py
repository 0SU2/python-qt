from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QMessageBox, QTableWidgetItem, QTableWidget
from PySide6.QtGui import QIcon

from lib.static import LOGO_FILE, LOGO_XS_FILE
from ui.compiled.ui_testing2 import Ui_MainWindow

from lib.services.server import conectar_base_datos
import mysql.connector

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # * Windows
        self.login_view = None
       
        # * Config UI
        self.setupUi(self)
        self.setWindowTitle("Chicles") 
        self.setWindowIcon(QIcon(str(LOGO_XS_FILE)))

        # * Set initial state
        self.username = None
        self.initial_state()

        # * Connect Events
        self.btnProvider.clicked.connect(lambda: self.change_main_page(self.btnProvider, 0,))
        self.btnClient.clicked.connect(lambda: self.change_main_page(self.btnClient, 1,))
        self.btnProduct.clicked.connect(lambda: self.change_main_page(self.btnProduct, 2,))

        self.btnClose.clicked.connect(self.close)
        self.btnLogOut.clicked.connect(self.logout)

        self.btnDeleteRow.clicked.connect(self.deleteSelected)

    # getting of client
    def base_datos(self, table):
        conexion = conectar_base_datos()
        if conexion:
            try:
                mysqlcursor = conexion.cursor()
                mysqlcursor.execute(f"SELECT * FROM {table}")
                self.result = mysqlcursor.fetchall()
                conexion.close()
                return self.result
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Error", f"Error: {err}")
                return
            
    # actions
    def deleteSelected(self):
        self.support = []
        rango = 0
        conexion = conectar_base_datos()
        if conexion:
            try:
                mysqlcursor = conexion.cursor() 
                current_view = self.stacked1Contenido.currentIndex()
                if current_view == 0:
                    self.selected = self.tableProvider.selectedItems()
                    mysqlcursor.execute("SELECT * FROM cliente")
                    for item in self.selected:
                        self.support.insert(rango, item.text())
                        rango += 1
                    QMessageBox.warning(self, "Advertencia!", f"Estas apunto de borrar los datos: {str(self.support)}")
                conexion.close()
                return   
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Error", f"Error: {err}")
                return
    
    # query throw data
    def llenar_tablas_datos(self, tabla, QTableWidget):
        allClients = self.base_datos(tabla)
        if allClients:
            lenght = len(allClients)
            QTableWidget.setRowCount(lenght)
            fila = 0
            for item in allClients:
                for index in range(len(item)):
                    QTableWidget.setItem(fila, index, QTableWidgetItem(str(item[index])))
                fila += 1
        else:
            print(f"Error")

    # * -------------- INHERIT EVENT HANDLES ---------------
    def closeEvent(self, event):
        self.initial_state()

    # * ------------ APPLICATION EVENT HANDLES ------------
    def initial_state(self):
        """ Set initial state for the window """
        self.lbCompany.setText("Chicles")
        self.lbUser.setText(self.username if self.username is not None else "USER")
        self.stacked1Contenido.setCurrentIndex(0)
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)

        self.llenar_tablas_datos("proveedor", self.tableProvider)

    def change_main_page(self, pressed_btn_nav, stack1_index):
        # * Alternate state for each btnNav button
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)
        pressed_btn_nav.setChecked(True)
        # * Set active the selected page
        self.stacked1Contenido.setCurrentIndex(stack1_index)
        # load data from the first table
        if stack1_index == 0:
            self.llenar_tablas_datos("proveedor", self.tableProvider)
        if stack1_index == 1:
            self.llenar_tablas_datos("cliente", self.tableClient)
        if stack1_index == 2:
            self.llenar_tablas_datos("polvosabor", self.tableProduct)

    def logout(self):
        self.login_view.initial_state()
        self.login_view.show()
        self.close()