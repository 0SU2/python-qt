import mysql.connector
from PySide6.QtWidgets import QMessageBox

def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",       # Cambiar según tu configuración
            password="root",
            database="chicles"
        )
        return conexion
    except mysql.connector.Error as err:
        QMessageBox.warning("Error", f"Error conectando a la base de datos: {err}")
        return None