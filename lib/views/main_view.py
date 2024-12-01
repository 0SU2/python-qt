from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QMainWindow, QPushButton, QMessageBox, QTableWidgetItem, QDialog, QDateTimeEdit
from PySide6.QtGui import QIcon

from lib.static import LOGO_FILE, LOGO_XS_FILE
from ui.compiled.ui_testing2 import Ui_MainWindow

from lib.services.server import conectar_base_datos
from ui.compiled.ui_providerInputForm import Ui_providerAdd
from ui.compiled.ui_clientInputForm import Ui_Form
from ui.compiled.ui_productInputForm import Ui_Form as Producto
import mysql.connector

class Product_ADD(QDialog, Producto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Producto")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
        self.textDate.setDateTime(QDateTime.currentDateTime())
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textLevel.toPlainText(), self.textType.toPlainText(), self.textDate.dateTime().toString("yyyy-MM-dd")]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Client_ADD(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Cliente")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textFlavor.toPlainText(), self.textHistory.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Provider_ADD(QDialog, Ui_providerAdd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar proveedor")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textPhone.toPlainText(), self.textPhone.toPlainText(), self.textEmail.toPlainText(), self.textAddres.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

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
        self.btnUpdateRow.clicked.connect(self.updateData)
        self.btnAdd.clicked.connect(self.addNew)

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
 
    # actions
    def deleteSelected(self):
        self.support = []
        if self.tableClient.selectedItems() or self.tableProvider.selectedItems() or self.tableProduct.selectedItems():
            rango = 0
            conexion = conectar_base_datos()
            if conexion:
                try:
                    mysqlcursor = conexion.cursor() 
                    current_view = self.stacked1Contenido.currentIndex()

                    # tabla de proveedores
                    if current_view == 0:
                        self.selected = self.tableProvider.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Avertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM proveedor WHERE ID_Proveedor = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("proveedor", self.tableProvider)

                    # tabla de clientes
                    if current_view == 1:
                        self.selected = self.tableClient.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Avertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM cliente WHERE ID_CLiente = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("cliente", self.tableClient)

                    # tabla de productos
                    if current_view == 2:
                        self.selected = self.tableProduct.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Avertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM polvosabor WHERE ID_Sabor = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("polvosabor", self.tableProduct)

                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
        else:
            QMessageBox.warning(self, "Error", "No seleccionaste ningun dato a borrar")

    def updateData(self):
        # revisar que se haya seleccionado un dato
        if self.tableProvider.selectedItems() or self.tableClient.selectedItems() or self.tableProduct.selectedItems():
            index = self.stacked1Contenido.currentIndex()
            support = []
            rango = 0
            # editar tabla de proveedor
            if index == 0:
                self.selected = self.tableProvider.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM proveedor WHERE ID_Proveedor = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Avertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE proveedor SET Nombre = %s, Contacto = %s, Telefono = %s, Email = %s, Direccion = %s WHERE ID_Proveedor = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("proveedor", self.tableProvider)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla clientes
            if index == 1:
                self.selected = self.tableClient.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM cliente WHERE ID_Cliente = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Avertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE cliente SET Nombre = %s, PreferenciasSabor = %s, HistorialCombinaciones = %s WHERE ID_Cliente = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("cliente", self.tableClient)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla polvosabor
            if index == 2:
                self.selected = self.tableProduct.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM polvosabor WHERE ID_Sabor = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Avertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE polvosabor SET Nombre = %s, Intensidad = %s, Tipo = %s, FechaExpiración = %s WHERE ID_Sabor = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("polvosabor", self.tableProduct)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
        else:
            QMessageBox.warning(self, "Error", "No hay datos a modificar")

    def addNew(self):
        conexion = conectar_base_datos()
        try:
            vista_actual = self.stacked1Contenido.currentIndex()
            mysqlconexion = conexion.cursor()
            # para la tabla de proveedores
            if vista_actual == 0:
                form = Provider_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO proveedor (Nombre,Contacto,Telefono,Email,Direccion) VALUES(%s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("proveedor", self.tableProvider)
            # para la tabla de clientes
            if vista_actual == 1:
                form = Client_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO cliente (Nombre,PreferenciasSabor,HistorialCombinaciones) VALUES(%s, %s, %s)"
                    values = (response[0], response[1], response[2])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("cliente", self.tableClient)
            # para la tabla de productos
            if vista_actual == 2:
                form = Product_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO polvosabor (Nombre,Intensidad,Tipo,FechaExpiración) VALUES(%s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("polvosabor", self.tableProduct)
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error",f"Error: {err}")
        finally:
            conexion.close()

    # valor inicial de la vista
    def initial_state(self):
        """ Set initial state for the window """
        self.lbCompany.setText("Chicles")
        self.lbUser.setText(self.username if self.username is not None else "USER")
        self.stacked1Contenido.setCurrentIndex(0)
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)

        self.llenar_tablas_datos("proveedor", self.tableProvider)

    # cuando escucha que vista fue cambiada
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