import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Configuración de la conexión a la base de datos
def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="rebeca",       # Cambiar según tu configuración
            password="21712rbk.",
            database="Proyecto_final"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error conectando a la base de datos: {err}")
        return None
def gestionar_productos():
    ventana_productos = tk.Toplevel()
    ventana_productos.title("Gestión de Productos")
    ventana_productos.geometry("400x200")
    ventana_productos.config(bg="lightblue")
    
    tk.Label(ventana_productos, text="Gestión de Productos", font=("Courier New", 14),fg="blue", bg="lightblue").pack(pady=10)
    
    tk.Button(ventana_productos, text="Agregar Producto",font=("Courier New", 10), command=abrir_formulario_producto,fg="blue", bg="lightblue").pack(pady=5)
    tk.Button(ventana_productos, text="Listar Productos", command=listar_productos, fg="blue", bg="lightblue").pack(pady=5)
    tk.Button(ventana_productos, text="Cerrar", command=ventana_productos.destroy, fg="blue", bg="lightblue").pack(pady=10)
def abrir_formulario_producto():
    ventana_form = tk.Toplevel()
    ventana_form.title("Agregar Producto")
    ventana_form.geometry("400x300")
    
    tk.Label(ventana_form, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    combo_nombre = ttk.Combobox(ventana_form, values=["NavyBlue", "RedCherry", "PearlWhite", "OceanBlack"])
    combo_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="Tamaño:").grid(row=1, column=0, padx=10, pady=5)
    combo_tamaño = ttk.Combobox(ventana_form, values=["Chico", "Mediano", "Grande"])
    combo_tamaño.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Precio:").grid(row=2, column=0, padx=10, pady=5)
    entry_precio = tk.Entry(ventana_form)
    entry_precio.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Estado:").grid(row=3, column=0, padx=10, pady=5)
    combo_estado = ttk.Combobox(ventana_form, values=["Activo", "Inactivo"])
    combo_estado.grid(row=3, column=1, padx=10, pady=5)
    
    def guardar_producto():
        nombre = combo_nombre.get()
        tamaño = combo_tamaño.get()
        precio = entry_precio.get()
        estado = combo_estado.get()
        
        if not nombre or not tamaño or not precio or not estado:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO producto (pro_nombre, pro_tamaño, pro_precio, pro_fecha_creacion, pro_estado)
                    VALUES (%s, %s, %s, NOW(), %s)
                """
                cursor.execute(query, (nombre, tamaño, precio, estado))
                conexion.commit()
                messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                ventana_form.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el producto: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_form, text="Guardar", command=guardar_producto).grid(row=4, column=0, columnspan=2, pady=10)
def listar_productos():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Productos")
    ventana_lista.geometry("600x400")

    tk.Label(ventana_lista, text="Lista de Productos", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Nombre", "Tamaño", "Precio", "Estado"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Nombre", text="Nombre", anchor="center")
    tree.heading("Tamaño", text="Tamaño", anchor="center")
    tree.heading("Precio", text="Precio", anchor="center")
    tree.heading("Estado", text="Estado", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.column("ID", width=50, anchor="center")
    tree.column("Nombre", width=150, anchor="center")
    tree.column("Tamaño", width=200, anchor="center")
    tree.column("Precio", width=200, anchor="center")
    tree.column("Estado", width=150, anchor="center")

    # Botón de eliminar producto
    tk.Button(ventana_lista, text="Agregar Producto", command=abrir_formulario_producto).pack(pady=5)
    tk.Button(ventana_lista, text="Eliminar Producto", command=lambda: eliminar_producto(tree)).pack(pady=10)

    # Cargar productos desde la base de datos
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT producto_id, pro_nombre, pro_precio, pro_estado FROM producto"
            cursor.execute(query)
            productos = cursor.fetchall()
            for producto in productos:
                tree.insert("", "end", values=producto)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de productos: {err}")
        finally:
            conexion.close()
def eliminar_producto(tree):
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un producto para eliminar.")
        return

    producto = tree.item(seleccionado)['values']
    producto_id = producto[0]
    producto_nombre = producto[1]

    confirmar = messagebox.askyesno(
        "Confirmar Eliminación",
        f"¿Estás seguro de eliminar el producto '{producto_nombre}' (ID: {producto_id})?"
    )
    if not confirmar:
        return

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM producto WHERE producto_id = %s"
            cursor.execute(query, (producto_id,))
            conexion.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Producto '{producto_nombre}' eliminado correctamente.")
                tree.delete(seleccionado)
            else:
                messagebox.showwarning("Advertencia", "No se encontró el producto para eliminar.")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ROW_IS_REFERENCED_2:
                messagebox.showerror(
                    "Error",
                    f"No se pudo eliminar el producto '{producto_nombre}' porque está asociado a otros registros."
                )
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el producto: {err}")
        finally:
            conexion.close()
def gestionar_clientes():
    ventana_clientes = tk.Toplevel()
    ventana_clientes.title("Gestión de Clientes")
    ventana_clientes.geometry("500x400")
    
    tk.Label(ventana_clientes, text="Gestión de Clientes", font=("Courier New", 14)).pack(pady=10)
    
    tk.Button(ventana_clientes, text="Agregar Cliente", command=abrir_formulario_cliente).pack(pady=5)
    tk.Button(ventana_clientes, text="Listar Clientes", command=listar_clientes).pack(pady=5)
    tk.Button(ventana_clientes, text="Cerrar", command=ventana_clientes.destroy).pack(pady=10)
def listar_clientes():
    # Crear una nueva ventana para listar clientes
    ventana_clientes = tk.Toplevel()
    ventana_clientes.title("Lista de Clientes")
    ventana_clientes.geometry("800x400")

    tk.Label(ventana_clientes, text="Lista de Clientes", font=("Arial", 12)).pack(pady=1)

    # Crear un Treeview para mostrar los clientes y sus direcciones
    tree = ttk.Treeview(ventana_clientes, columns=("ID", "Nombre", "Correo", "Teléfono", "Dirección", "Ciudad", "País", "Codigo Postal"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Nombre", text="Nombre",anchor="center")
    tree.heading("Correo", text="Correo",anchor="center")
    tree.heading("Teléfono", text="Teléfono",anchor="center")
    tree.heading("Dirección", text="Dirección",anchor="center")
    tree.heading("Ciudad", text="Ciudad",anchor="center")
    tree.heading("País", text="País",anchor="center")
    tree.heading("Codigo Postal", text="Codigo Postal",anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)
    tree.column("ID", width=50, anchor="center")
    tree.column("Nombre", width=150, anchor="center")
    tree.column("Correo", width=200, anchor="center")
    tree.column("Teléfono", width=100, anchor="center")
    tree.column("Dirección", width=250, anchor="center")
    tree.column("Ciudad", width=100, anchor="center")
    tree.column("País", width=100, anchor="center")
    tree.column("Codigo Postal", width=100, anchor="center")

    tk.Button(ventana_clientes, text="Eliminar Cliente", command=lambda: eliminar_cliente(tree)).pack(pady=10)

    # Conexión a la base de datos para obtener la información de los clientes
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
                SELECT c.cliente_id, c.cli_nombre, c.cli_correo, c.cli_telefono, 
                       d.dir_direccion, d.dir_ciudad, d.dir_codigo_postal, d.dir_pais
                FROM clientes c
                LEFT JOIN direcciones d ON c.cliente_id = d.cliente_id
            """
            cursor.execute(query)
            clientes = cursor.fetchall()

            # Insertar los datos de los clientes en el Treeview
            for cliente in clientes:
                tree.insert("", "end", values=cliente)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo obtener la lista de clientes: {err}")
        finally:
            conexion.close()
def eliminar_cliente(tree):
    # Obtener el cliente seleccionado
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un cliente para eliminar.")
        return

    # Obtener los datos del cliente seleccionado
    cliente = tree.item(seleccionado)['values']
    cliente_id = cliente[0]  # ID del cliente (columna 0)
    cliente_nombre = cliente[1]  # Nombre del cliente (columna 1)

    # Confirmar la eliminación
    confirmar = messagebox.askyesno(
        "Confirmar Eliminación", 
        f"¿Estás seguro de eliminar al cliente '{cliente_nombre}' (ID: {cliente_id})?"
    )
    if not confirmar:
        return

    # Conectar a la base de datos para eliminar el cliente
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM clientes WHERE cliente_id = %s"
            cursor.execute(query, (cliente_id,))
            conexion.commit()

            # Verificar si el cliente fue eliminado
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Cliente '{cliente_nombre}' eliminado correctamente.")
                tree.delete(seleccionado)  # Eliminar del Treeview
            else:
                messagebox.showwarning("Advertencia", "No se encontró al cliente para eliminar.")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ROW_IS_REFERENCED_2:
                messagebox.showerror(
                    "Error", 
                    f"No se puede eliminar al cliente '{cliente_nombre}' porque está asociado a otros registros."
                )
            else:
                messagebox.showerror("Error", f"No se pudo eliminar al cliente: {err}")
        finally:
            conexion.close()
def abrir_formulario_cliente():
    ventana_form = tk.Toplevel()
    ventana_form.title("Agregar Cliente")
    ventana_form.geometry("400x400")
    
    tk.Label(ventana_form, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana_form)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="Correo:").grid(row=1, column=0, padx=10, pady=5)
    entry_correo = tk.Entry(ventana_form)
    entry_correo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)
    entry_telefono = tk.Entry(ventana_form)
    entry_telefono.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="Dirección:").grid(row=3, column=0, padx=10, pady=5)
    entry_direccion = tk.Entry(ventana_form)
    entry_direccion.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="Ciudad:").grid(row=4, column=0, padx=10, pady=5)
    entry_ciudad = tk.Entry(ventana_form)
    entry_ciudad.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="País:").grid(row=5, column=0, padx=10, pady=5)
    entry_pais = tk.Entry(ventana_form)
    entry_pais.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(ventana_form, text="Codigo postal:").grid(row=6, column=0, padx=10, pady=5)
    entry_codigo = tk.Entry(ventana_form)
    entry_codigo.grid(row=6, column=1, padx=10, pady=5)

    def guardar_cliente():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        ciudad = entry_ciudad.get()
        pais = entry_pais.get()
        codigo = entry_codigo.get()
        
        if not nombre or not correo or not telefono or not direccion or not ciudad or not pais or not codigo:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()

                # Insertar datos en la tabla `clientes`
                query_cliente = """
                INSERT INTO clientes (cli_nombre, cli_correo, cli_telefono)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query_cliente, (nombre, correo, telefono))
                cliente_id = cursor.lastrowid  # Obtener el ID del cliente insertado

                # Insertar datos en la tabla `direcciones`
                query_direccion = """
                    INSERT INTO direcciones (cliente_id, dir_direccion, dir_ciudad, dir_pais, dir_codigo_postal)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query_direccion, (cliente_id, direccion, ciudad, pais, codigo))
                
                conexion.commit()
                messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
                ventana_form.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el cliente: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_form, text="Guardar", command=guardar_cliente).grid(row=7, column=0, columnspan=2, pady=10)
def gestionar_empleados():
    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Gestión de Empleados")
    ventana_empleados.geometry("500x400")
    
    tk.Label(ventana_empleados, text="Gestión de Empleados", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_empleados, text="Agregar Empleado", command=abrir_formulario_empleado).pack(pady=5)
    tk.Button(ventana_empleados, text="Listar Empleados", command=listar_empleados).pack(pady=5)
    tk.Button(ventana_empleados, text="Cerrar", command=ventana_empleados.destroy).pack(pady=10)
def abrir_formulario_empleado():
    ventana_form = tk.Toplevel()
    ventana_form.title("Agregar Empleado")
    ventana_form.geometry("400x300")
    
    # Campos para agregar empleado
    tk.Label(ventana_form, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana_form)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Fecha Nac. (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    entry_fecha_nac = tk.Entry(ventana_form)
    entry_fecha_nac.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Cargo:").grid(row=2, column=0, padx=10, pady=5)
    entry_cargo = tk.Entry(ventana_form)
    entry_cargo.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Salario:").grid(row=3, column=0, padx=10, pady=5)
    entry_salario = tk.Entry(ventana_form)
    entry_salario.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Fecha Contratación (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
    entry_fecha_contratacion = tk.Entry(ventana_form)
    entry_fecha_contratacion.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Teléfono:").grid(row=5, column=0, padx=10, pady=5)
    entry_telefono = tk.Entry(ventana_form)
    entry_telefono.grid(row=5, column=1, padx=10, pady=5)
    
    def guardar_empleado():
        nombre = entry_nombre.get()
        fecha_nac = entry_fecha_nac.get()
        cargo = entry_cargo.get()
        salario = entry_salario.get()
        fecha_contratacion = entry_fecha_contratacion.get()
        telefono = entry_telefono.get()

        if not nombre or not fecha_nac or not cargo or not salario or not fecha_contratacion or not telefono:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO empleados (emp_nombre, emp_fecha_nac, emp_cargo, emp_salario, emp_fecha_contratacion, emp_telefono)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (nombre, fecha_nac, cargo, salario, fecha_contratacion, telefono))
                conexion.commit()
                messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
                ventana_form.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el empleado: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_form, text="Guardar", command=guardar_empleado).grid(row=6, column=0, columnspan=2, pady=10)
def listar_empleados():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Empleados")
    ventana_lista.geometry("700x400")

    tk.Label(ventana_lista, text="Lista de Empleados", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Nombre", "Fecha Nac.", "Cargo", "Salario", "Fecha Contratacion", "Telefono"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Nombre", text="Nombre", anchor="center")
    tree.heading("Fecha Nac.", text="Fecha Nac.", anchor="center")
    tree.heading("Cargo", text="Cargo", anchor="center")
    tree.heading("Salario", text="Salario", anchor="center")
    tree.heading("Fecha Contratacion", text="Fecha Contratación", anchor="center")
    tree.heading("Telefono", text="Teléfono", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    # Configuración de las columnas
    tree.column("ID", width=50, anchor="center")
    tree.column("Nombre", width=150, anchor="center")
    tree.column("Fecha Nac.", width=100, anchor="center")
    tree.column("Cargo", width=150, anchor="center")
    tree.column("Salario", width=100, anchor="center")
    tree.column("Fecha Contratacion", width=150, anchor="center")
    tree.column("Telefono", width=150, anchor="center")

    tk.Button(ventana_lista, text="Eliminar Empleado", command=lambda: eliminar_empleado(tree)).pack(pady=10)
    # Conexión a la base de datos y carga de datos en el Treeview
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT empleado_id, emp_nombre, emp_fecha_nac, emp_cargo, emp_salario, emp_fecha_contratacion, emp_telefono FROM empleados"
            cursor.execute(query)
            empleados = cursor.fetchall()
            for empleado in empleados:
                tree.insert("", "end", values=empleado)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de empleados: {err}")
        finally:
            conexion.close()
def eliminar_empleado(tree):
    # Obtener el empleado seleccionado
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para eliminar.")
        return

    # Obtener los datos del empleado seleccionado
    empleado = tree.item(seleccionado)['values']
    empleado_id = empleado[0]
    empleado_nombre = empleado[1]

    # Confirmar eliminación
    confirmar = messagebox.askyesno(
        "Confirmar Eliminación",
        f"¿Estás seguro de eliminar al empleado '{empleado_nombre}' (ID: {empleado_id})?"
    )
    if not confirmar:
        return

    # Conectar a la base de datos para eliminar al empleado
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Intentar eliminar el empleado
            query = "DELETE FROM empleados WHERE empleado_id = %s"
            cursor.execute(query, (empleado_id,))
            conexion.commit()

            # Verificar si el registro fue eliminado
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Empleado '{empleado_nombre}' eliminado correctamente.")
                tree.delete(seleccionado)  # Eliminar del Treeview
            else:
                messagebox.showwarning("Advertencia", "No se encontró al empleado para eliminar.")
        except mysql.connector.Error as err:
            # Manejar error si el empleado está asociado a otros registros (asistencia, por ejemplo)
            if err.errno == mysql.connector.errorcode.ER_ROW_IS_REFERENCED_2:
                messagebox.showerror(
                    "Error",
                    f"No se puede eliminar al empleado '{empleado_nombre}' porque tiene registros asociados (por ejemplo, asistencia)."
                )
            else:
                messagebox.showerror("Error", f"No se pudo eliminar al empleado: {err}")
        finally:
            conexion.close()
def gestionar_asistencia():
    ventana_asistencia = tk.Toplevel()
    ventana_asistencia.title("Gestión de Asistencia")
    ventana_asistencia.geometry("500x400")
    
    tk.Label(ventana_asistencia, text="Gestión de Asistencia", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_asistencia, text="Registrar Asistencia", command=abrir_formulario_asistencia).pack(pady=5)
    tk.Button(ventana_asistencia, text="Listar Asistencias", command=listar_asistencias).pack(pady=5)
    tk.Button(ventana_asistencia, text="Cerrar", command=ventana_asistencia.destroy).pack(pady=10)
def abrir_formulario_asistencia():
    ventana_form = tk.Toplevel()
    ventana_form.title("Registrar Asistencia")
    ventana_form.geometry("400x400")
    
    # Campos para agregar asistencia
    tk.Label(ventana_form, text="ID del Empleado:").grid(row=0, column=0, padx=10, pady=5)
    entry_empleado_id = tk.Entry(ventana_form)
    entry_empleado_id.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Hora Entrada (YYYY-MM-DD HH:MM:SS):").grid(row=1, column=0, padx=10, pady=5)
    entry_hora_entrada = tk.Entry(ventana_form)
    entry_hora_entrada.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Hora Salida (YYYY-MM-DD HH:MM:SS):").grid(row=2, column=0, padx=10, pady=5)
    entry_hora_salida = tk.Entry(ventana_form)
    entry_hora_salida.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Estado (A tiempo / Retardo):").grid(row=3, column=0, padx=10, pady=5)
    combo_estado = ttk.Combobox(ventana_form, values=["A tiempo", "Retardo"])
    combo_estado.grid(row=3, column=1, padx=10, pady=5)
    
    def guardar_asistencia():
        empleado_id = entry_empleado_id.get()
        hora_entrada = entry_hora_entrada.get()
        hora_salida = entry_hora_salida.get()
        estado = combo_estado.get()

        if not empleado_id or not hora_entrada or not hora_salida or not estado:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO asistencia (empleado_id, asi_hora_entrada, asi_hora_salida, asi_estado)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (empleado_id, hora_entrada, hora_salida, estado))
                conexion.commit()
                messagebox.showinfo("Éxito", "Asistencia registrada correctamente.")
                ventana_form.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo registrar la asistencia: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_form, text="Guardar", command=guardar_asistencia).grid(row=4, column=0, columnspan=2, pady=10)
def listar_asistencias():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Asistencias")
    ventana_lista.geometry("700x400")

    tk.Label(ventana_lista, text="Lista de Asistencias", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Empleado ID", "Hora Entrada", "Hora Salida", "Estado"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Empleado ID", text="Empleado ID")
    tree.heading("Hora Entrada", text="Hora Entrada")
    tree.heading("Hora Salida", text="Hora Salida")
    tree.heading("Estado", text="Estado")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    # Conexión a la base de datos para obtener asistencias
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT asistencia_id, empleado_id, asi_hora_entrada, asi_hora_salida, asi_estado FROM asistencia")
            asistencias = cursor.fetchall()

            # Insertar los datos en el Treeview
            for asistencia in asistencias:
                tree.insert("", "end", values=asistencia)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo obtener la lista de asistencias: {err}")
        finally:
            conexion.close()
def registrar_pedido():
    ventana_pedido = tk.Toplevel()
    ventana_pedido.title("Registrar Pedido")
    ventana_pedido.geometry("700x600")

    tk.Label(ventana_pedido, text="Registrar Pedido", font=("Arial", 14)).pack(pady=10)

    # Inputs para el pedido
    tk.Label(ventana_pedido, text="Cliente ID:").pack(pady=5)
    entry_cliente_id = tk.Entry(ventana_pedido)
    entry_cliente_id.pack()

    tk.Label(ventana_pedido, text="Dirección ID:").pack(pady=5)
    entry_direccion_id = tk.Entry(ventana_pedido)
    entry_direccion_id.pack()

    tk.Label(ventana_pedido, text="Fecha (YYYY-MM-DD):").pack(pady=5)
    entry_fecha = tk.Entry(ventana_pedido)
    entry_fecha.pack()

    tk.Label(ventana_pedido, text="Notas:").pack(pady=5)
    entry_notas = tk.Entry(ventana_pedido, width=50)
    entry_notas.pack()

    # Inputs para productos
    productos = []
    frame_productos = tk.Frame(ventana_pedido)
    frame_productos.pack(pady=10)

    def agregar_producto():
        producto_id = entry_producto_id.get()
        cantidad = entry_cantidad.get()
        if not producto_id or not cantidad:
            messagebox.showerror("Error", "Debes llenar todos los campos del producto.")
            return
        productos.append((producto_id, cantidad))
        entry_producto_id.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        actualizar_lista_productos()

    def actualizar_lista_productos():
        listbox_productos.delete(0, tk.END)
        for i, producto in enumerate(productos):
            listbox_productos.insert(i, f"Producto ID: {producto[0]}, Cantidad: {producto[1]}")

    tk.Label(frame_productos, text="Producto ID:").grid(row=0, column=0, padx=5)
    entry_producto_id = tk.Entry(frame_productos)
    entry_producto_id.grid(row=0, column=1, padx=5)

    tk.Label(frame_productos, text="Cantidad:").grid(row=1, column=0, padx=5)
    entry_cantidad = tk.Entry(frame_productos)
    entry_cantidad.grid(row=1, column=1, padx=5)
    
    tk.Label(frame_productos, text="Precio:").grid(row=2, column=0, padx=5)
    entry_precio = tk.Entry(frame_productos, state='readonly')  # Solo lectura
    entry_precio.grid(row=2, column=1, padx=5)

    def obtener_precio_producto():
            producto_id = entry_producto_id.get()
            if producto_id:
                conexion = conectar_base_datos()
                if conexion:
                    try:
                        cursor = conexion.cursor()
                        query_precio = "SELECT pro_precio FROM producto WHERE producto_id = %s"
                        cursor.execute(query_precio, (producto_id,))
                        precio = cursor.fetchone()
                        if precio:
                            entry_precio.config(state='normal')  # Habilitar el campo para mostrar el precio
                            entry_precio.delete(0, tk.END)
                            entry_precio.insert(0, f"{precio[0]:.2f}")  # Mostrar el precio con dos decimales
                            entry_precio.config(state='readonly')  # Volver a ponerlo en solo lectura
                        else:
                            entry_precio.config(state='normal')
                            entry_precio.delete(0, tk.END)
                            entry_precio.insert(0, "No encontrado")
                            entry_precio.config(state='readonly')
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"No se pudo obtener el precio: {err}")
                    finally:
                        conexion.close()

        # Llamar a la función de obtener precio cuando cambie el ID del producto
    entry_producto_id.bind("<FocusOut>", lambda event: obtener_precio_producto())
    
    tk.Button(frame_productos, text="Agregar Producto", command=agregar_producto).grid(row=3, column=0, columnspan=2, pady=5)

    tk.Label(ventana_pedido, text="Lista de Productos:").pack(pady=5)
    listbox_productos = tk.Listbox(ventana_pedido, width=80, height=2)
    listbox_productos.pack()
    # Métodos de pago
    tk.Label(ventana_pedido, text="Método de Pago:").pack(pady=5)
    metodo_pago_opciones = ["Tarjeta Credito/Debito", "Paypal", "Efectivo en puntos de pago"]
    entry_metodo_pago = tk.StringVar(ventana_pedido)
    entry_metodo_pago.set(metodo_pago_opciones[2])  # Valor predeterminado
    dropdown_metodo_pago = tk.OptionMenu(ventana_pedido, entry_metodo_pago, *metodo_pago_opciones)
    dropdown_metodo_pago.pack(pady=5)

    # Guardar pedido
    def guardar_pedido():
        cliente_id = entry_cliente_id.get()
        direccion_id = entry_direccion_id.get()
        fecha = entry_fecha.get()
        notas = entry_notas.get()
        metodo_pago = entry_metodo_pago.get()  # Asegúrate de que esta entrada esté capturando el valor correctamente

        # Validación para asegurar que todos los campos están completos
        if not cliente_id or not direccion_id or not fecha or not productos or not metodo_pago:
            messagebox.showerror("Error", "Todos los campos y al menos un producto son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()

                # Insertar en la tabla `pedidos`
                query_pedido = "INSERT INTO pedidos (cliente_id, direcciones_id, ped_fecha, ped_notas, ped_metodo_pago) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query_pedido, (cliente_id, direccion_id, fecha, notas, metodo_pago))
                pedido_id = cursor.lastrowid  # Obtener el ID del pedido insertado

                # Insertar productos en `detalle_pedido`, usando el mismo método de pago
                for producto_id, cantidad in productos:
                    # Obtener el precio unitario del producto desde la tabla `producto`
                    query_precio = "SELECT pro_precio FROM producto WHERE producto_id = %s"
                    cursor.execute(query_precio, (producto_id,))
                    precio_unitario = cursor.fetchone()[0]  # Recuperar el precio del producto

                    # Calcular el precio total
                    precio_total = int(cantidad) * precio_unitario

                    # Insertar en la tabla `detalle_pedido`
                    query_producto = """
                        INSERT INTO detalle_pedido (pedido_id, producto_id, det_cantidad, det_precio_total) 
                        VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(query_producto, (pedido_id, producto_id, cantidad, precio_total))

                conexion.commit()
                messagebox.showinfo("Éxito", "Pedido registrado correctamente.")
                ventana_pedido.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo registrar el pedido: {err}")
            finally:
                conexion.close()

    # Botón para guardar el pedido
    tk.Button(ventana_pedido, text="Guardar Pedido", command=guardar_pedido).pack(pady=20)
def listar_pedidos():
    # Crear una nueva ventana para listar los pedidos
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Pedidos")
    ventana_lista.geometry("700x400")

    tk.Label(ventana_lista, text="Lista de Pedidos", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Cliente ID", "Dirección ID", "Fecha", "Método Pago", "Notas"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Cliente ID", text="Cliente ID", anchor="center")
    tree.heading("Dirección ID", text="Dirección ID", anchor="center")
    tree.heading("Fecha", text="Fecha", anchor="center")
    tree.heading("Método Pago", text="Método Pago", anchor="center")
    tree.heading("Notas", text="Notas", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    # Configuración del ancho de las columnas
    tree.column("ID", width=50, anchor="center")
    tree.column("Cliente ID", width=100, anchor="center")
    tree.column("Dirección ID", width=100, anchor="center")
    tree.column("Fecha", width=100, anchor="center")
    tree.column("Método Pago", width=150, anchor="center")
    tree.column("Notas", width=200, anchor="center")

    # Conectar a la base de datos y obtener los datos
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Consulta SQL para obtener los pedidos con detalles del método de pago
            query = """
                SELECT p.pedido_id, p.cliente_id, p.direcciones_id, p.ped_fecha, dp.ped_metodo_pago, p.ped_notas
                FROM pedidos p
                JOIN detalle_pedido dp ON p.pedido_id = dp.pedido_id
            """
            cursor.execute(query)
            pedidos = cursor.fetchall()

            # Insertar los pedidos obtenidos en el Treeview
            for pedido in pedidos:
                tree.insert("", "end", values=pedido)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de pedidos: {err}")
        finally:
            conexion.close()
def gestionar_pedidos():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Gestión de Pedidos")
    ventana_pedidos.geometry("500x400")
    
    tk.Label(ventana_pedidos, text="Gestión de Pedidos", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_pedidos, text="Listar Pedidos", command=listar_pedidos).pack(pady=5)
    tk.Button(ventana_pedidos, text="Cerrar", command=ventana_pedidos.destroy).pack(pady=10)
def abrir_formulario_pedido():
    ventana_form = tk.Toplevel()
    ventana_form.title("Agregar Pedido")
    ventana_form.geometry("400x300")
    
    tk.Label(ventana_form, text="Dirección ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_direccion_id = tk.Entry(ventana_form)
    entry_direccion_id.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    entry_fecha = tk.Entry(ventana_form)
    entry_fecha.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Método de Pago:").grid(row=2, column=0, padx=10, pady=5)
    metodo_pago_var = tk.StringVar()
    metodo_pago_menu = ttk.Combobox(ventana_form, textvariable=metodo_pago_var, values=["Tarjeta Credito/Debito", "Paypal", "Efectivo en puntos de pago"])
    metodo_pago_menu.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(ventana_form, text="Notas:").grid(row=3, column=0, padx=10, pady=5)
    entry_notas = tk.Entry(ventana_form)
    entry_notas.grid(row=3, column=1, padx=10, pady=5)
    
    def guardar_pedido():
        direccion_id = entry_direccion_id.get()
        fecha = entry_fecha.get()
        metodo_pago = metodo_pago_var.get()
        notas = entry_notas.get()

        if not direccion_id or not fecha or not metodo_pago:
            messagebox.showwarning("Advertencia", "Dirección, Fecha y Método de Pago son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO pedidos (direcciones_id, ped_fecha, ped_metodo_pago, ped_notas)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (direccion_id, fecha, metodo_pago, notas))
                conexion.commit()
                messagebox.showinfo("Éxito", "Pedido agregado correctamente.")
                ventana_form.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el pedido: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_form, text="Guardar", command=guardar_pedido).grid(row=4, column=0, columnspan=2, pady=10)
def listar_pedidos():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Pedidos")
    ventana_lista.geometry("700x400")

    tk.Label(ventana_lista, text="Lista de Pedidos", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Dirección ID", "Fecha", "Método Pago", "Notas"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Dirección ID", text="Dirección ID", anchor="center")
    tree.heading("Fecha", text="Fecha", anchor="center")
    tree.heading("Método Pago", text="Método Pago", anchor="center")
    tree.heading("Notas", text="Notas", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.column("ID", width=50, anchor="center")
    tree.column("Dirección ID", width=150, anchor="center")
    tree.column("Fecha", width=100, anchor="center")
    tree.column("Método Pago", width=150, anchor="center")
    tree.column("Notas", width=200, anchor="center")

    # Cargar datos desde la base de datos
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT pedido_id, direcciones_id, ped_fecha, ped_metodo_pago, ped_notas FROM pedidos"
            cursor.execute(query)
            pedidos = cursor.fetchall()
            for pedido in pedidos:
                tree.insert("", "end", values=pedido)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de pedidos: {err}")
        finally:
            conexion.close()
def listar_almacenes():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Almacenes")
    ventana_lista.geometry("600x400")

    tk.Label(ventana_lista, text="Lista de Almacenes", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Nombre", "Ubicación"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Nombre", text="Nombre", anchor="center")
    tree.heading("Ubicación", text="Ubicación", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.column("ID", width=50, anchor="center")
    tree.column("Nombre", width=150, anchor="center")
    tree.column("Ubicación", width=200, anchor="center")

    # Conexión a la base de datos y carga de datos
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT almacen_id, alm_nombre, alm_ubicacion FROM almacenes"
            cursor.execute(query)
            almacenes = cursor.fetchall()
            for almacen in almacenes:
                tree.insert("", "end", values=almacen)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de almacenes: {err}")
        finally:
            conexion.close()

    tk.Button(ventana_lista, text="Agregar Almacén", command=abrir_formulario_almacen).pack(pady=5)
    tk.Button(ventana_lista, text="Eliminar Almacén", command=lambda: eliminar_almacen(tree)).pack(pady=5)
def gestionar_almacenes():
    ventana_almacenes = tk.Toplevel()
    ventana_almacenes.title("Gestión de Almacenes")
    ventana_almacenes.geometry("500x400")
    
    tk.Label(ventana_almacenes, text="Gestión de Almacenes", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_almacenes, text="Agregar Almacen", command=abrir_formulario_almacen).pack(pady=5)
    tk.Button(ventana_almacenes, text="Listar Almacenes", command=listar_almacenes).pack(pady=5)
    tk.Button(ventana_almacenes, text="Cerrar", command=ventana_almacenes.destroy).pack(pady=10)
def abrir_formulario_almacen():
    ventana_formulario = tk.Toplevel()
    ventana_formulario.title("Agregar Almacén")
    ventana_formulario.geometry("400x300")

    tk.Label(ventana_formulario, text="Nombre del Almacén:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_formulario)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_formulario, text="Ubicación del Almacén:").pack(pady=5)
    entrada_ubicacion = tk.Entry(ventana_formulario)
    entrada_ubicacion.pack(pady=5)

    def guardar_almacen():
        nombre = entrada_nombre.get()
        ubicacion = entrada_ubicacion.get()

        if not nombre or not ubicacion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO almacenes (alm_nombre, alm_ubicacion) VALUES (%s, %s)"
                cursor.execute(query, (nombre, ubicacion))
                conexion.commit()
                messagebox.showinfo("Éxito", "Almacén agregado correctamente.")
                ventana_formulario.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el almacén: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_formulario, text="Guardar", command=guardar_almacen).pack(pady=20)
def eliminar_almacen(tree):
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un almacén para eliminar.")
        return

    almacen = tree.item(seleccionado)['values']
    almacen_id = almacen[0]
    almacen_nombre = almacen[1]

    confirmar = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de eliminar el almacén '{almacen_nombre}' (ID: {almacen_id})?")
    if not confirmar:
        return

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM almacenes WHERE almacen_id = %s"
            cursor.execute(query, (almacen_id,))
            conexion.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Almacén '{almacen_nombre}' eliminado correctamente.")
                tree.delete(seleccionado)
            else:
                messagebox.showwarning("Advertencia", "No se encontró el almacén para eliminar.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el almacén: {err}")
        finally:
            conexion.close()
def gestionar_materiales():
    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Gestión de Materiales")
    ventana_empleados.geometry("500x400")
    
    tk.Label(ventana_empleados, text="Gestión de Materiales", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_empleados, text="Agregar Material", command=abrir_formulario_material).pack(pady=5)
    tk.Button(ventana_empleados, text="Listar Materiales", command=listar_materiales).pack(pady=5)
    tk.Button(ventana_empleados, text="Cerrar", command=ventana_empleados.destroy).pack(pady=10)  
def listar_materiales():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Materiales")
    ventana_lista.geometry("600x400")

    tk.Label(ventana_lista, text="Lista de Materiales", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Nombre", "Descripción"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Nombre", text="Nombre", anchor="center")
    tree.heading("Descripción", text="Descripción", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.column("ID", width=50, anchor="center")
    tree.column("Nombre", width=150, anchor="center")
    tree.column("Descripción", width=300, anchor="center")
    
    tk.Button(ventana_lista, text="Eliminar Material", command=lambda: eliminar_material(tree)).pack(pady=5)
    # Conexión a la base de datos y carga de datos
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT material_id, mat_nombre, mat_descripcion FROM material"
            cursor.execute(query)
            materiales = cursor.fetchall()
            for material in materiales:
                tree.insert("", "end", values=material)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de materiales: {err}")
        finally:
            conexion.close()
def abrir_formulario_material():
    ventana_formulario = tk.Toplevel()
    ventana_formulario.title("Agregar Material")
    ventana_formulario.geometry("400x300")

    tk.Label(ventana_formulario, text="Nombre del Material:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_formulario)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_formulario, text="Descripción del Material:").pack(pady=5)
    entrada_descripcion = tk.Text(ventana_formulario, height=5, width=40)
    entrada_descripcion.pack(pady=5)

    def guardar_material():
        nombre = entrada_nombre.get()
        descripcion = entrada_descripcion.get("1.0", tk.END).strip()

        if not nombre or not descripcion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO material (mat_nombre, mat_descripcion) VALUES (%s, %s)"
                cursor.execute(query, (nombre, descripcion))
                conexion.commit()
                messagebox.showinfo("Éxito", "Material agregado correctamente.")
                ventana_formulario.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el material: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_formulario, text="Guardar", command=guardar_material).pack(pady=20)
def eliminar_material(tree):
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un material para eliminar.")
        return

    material = tree.item(seleccionado)['values']
    material_id = material[0]
    material_nombre = material[1]

    confirmar = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de eliminar el material '{material_nombre}' (ID: {material_id})?")
    if not confirmar:
        return

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM material WHERE material_id = %s"
            cursor.execute(query, (material_id,))
            conexion.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Material '{material_nombre}' eliminado correctamente.")
                tree.delete(seleccionado)
            else:
                messagebox.showwarning("Advertencia", "No se encontró el material para eliminar.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el material: {err}")
        finally:
            conexion.close()            
def abrir_formulario_producto_almacen():
    ventana_formulario = tk.Toplevel()
    ventana_formulario.title("Agregar Producto a Almacén")
    ventana_formulario.geometry("500x400")

    # Entradas
    tk.Label(ventana_formulario, text="ID Producto:").pack(pady=5)
    entrada_producto = tk.Entry(ventana_formulario)
    entrada_producto.pack(pady=5)

    tk.Label(ventana_formulario, text="ID Almacén:").pack(pady=5)
    entrada_almacen = tk.Entry(ventana_formulario)
    entrada_almacen.pack(pady=5)

    tk.Label(ventana_formulario, text="ID Material:").pack(pady=5)
    entrada_material = tk.Entry(ventana_formulario)
    entrada_material.pack(pady=5)

    tk.Label(ventana_formulario, text="Cantidad en Stock:").pack(pady=5)
    entrada_stock = tk.Entry(ventana_formulario)
    entrada_stock.pack(pady=5)

    def guardar_producto_almacen():
        producto_id = entrada_producto.get()
        almacen_id = entrada_almacen.get()
        material_id = entrada_material.get()
        cantidad_stock = entrada_stock.get()

        if not (producto_id and almacen_id and material_id and cantidad_stock):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO productos_almacen (producto_id, almacen_id, material_id, pro_alm_cantidad_stock)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (producto_id, almacen_id, material_id, cantidad_stock))
                conexion.commit()
                messagebox.showinfo("Éxito", "Producto agregado al almacén correctamente.")
                ventana_formulario.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo agregar el producto al almacén: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_formulario, text="Guardar", command=guardar_producto_almacen).pack(pady=20)
def gestionar_productos_almacen():
    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Gestión de Productos Alamcen")
    ventana_empleados.geometry("500x400")
    
    tk.Label(ventana_empleados, text="Productos Alamcen", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(ventana_empleados, text="Agregar Productos Alamcen", command=abrir_formulario_producto_almacen).pack(pady=5)
    tk.Button(ventana_empleados, text="Listar Productos Alamcen", command=listar_productos_almacen).pack(pady=5)
    tk.Button(ventana_empleados, text="Cerrar", command=ventana_empleados.destroy).pack(pady=10)
def listar_productos_almacen():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Productos en Almacenes")
    ventana_lista.geometry("800x400")

    tk.Label(ventana_lista, text="Productos en Almacenes", font=("Arial", 14)).pack(pady=20)

    # Configuración del Treeview
    tree = ttk.Treeview(ventana_lista, columns=("ID", "Producto", "Almacén", "Material", "Stock"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Producto", text="Producto", anchor="center")
    tree.heading("Almacén", text="Almacén", anchor="center")
    tree.heading("Material", text="Material", anchor="center")
    tree.heading("Stock", text="Cantidad en Stock", anchor="center")
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.column("ID", width=50, anchor="center")
    tree.column("Producto", width=150, anchor="center")
    tree.column("Almacén", width=150, anchor="center")
    tree.column("Material", width=150, anchor="center")
    tree.column("Stock", width=100, anchor="center")

    tk.Button(ventana_lista, text="Agregar Producto Almacen", command=abrir_formulario_producto_almacen).pack(pady=5)
    tk.Button(ventana_lista, text="Eliminar Producto Almacen", command=lambda: eliminar_producto_almacen(tree)).pack(pady=10)

    # Conexión a la base de datos y carga de datos
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
                SELECT pa.producto_almacen_id, p.pro_nombre, a.alm_nombre, m.mat_nombre, pa.pro_alm_cantidad_stock
                FROM productos_almacen pa
                JOIN producto p ON pa.producto_id = p.producto_id
                JOIN almacenes a ON pa.almacen_id = a.almacen_id
                JOIN material m ON pa.material_id = m.material_id
            """
            cursor.execute(query)
            productos = cursor.fetchall()
            for producto in productos:
                tree.insert("", "end", values=producto)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo cargar la lista de productos en almacenes: {err}")
        finally:
            conexion.close()
def eliminar_producto_almacen(tree):
    # Obtener el elemento seleccionado en el Treeview
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un producto para eliminar.")
        return

    # Obtener los datos del producto seleccionado
    producto_almacen = tree.item(seleccionado)['values']
    producto_almacen_id = producto_almacen[0]  # El ID del producto_almacen está en la primera columna
    producto_nombre = producto_almacen[1]  # Nombre del producto para confirmación
    almacen_nombre = producto_almacen[2]  # Nombre del almacén para confirmación

    # Confirmación de eliminación
    confirmar = messagebox.askyesno(
        "Confirmar Eliminación",
        f"¿Estás seguro de eliminar el producto '{producto_nombre}' del almacén '{almacen_nombre}'?"
    )
    if not confirmar:
        return

    # Conexión a la base de datos para eliminar el producto
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM productos_almacen WHERE producto_almacen_id = %s"
            cursor.execute(query, (producto_almacen_id,))
            conexion.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"El producto '{producto_nombre}' fue eliminado correctamente del almacén '{almacen_nombre}'.")
                # Eliminar del Treeview
                tree.delete(seleccionado)
            else:
                messagebox.showwarning("Advertencia", "No se encontró el producto para eliminar.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el producto del almacén: {err}")
        finally:
            conexion.close()
def registrar_inventario():
    ventana_inventario = tk.Toplevel()
    ventana_inventario.title("Registrar Inventario")
    ventana_inventario.geometry("600x500")

    tk.Label(ventana_inventario, text="Registrar Inventario", font=("Arial", 14)).pack(pady=10)

    # Inputs para el inventario
    tk.Label(ventana_inventario, text="Almacén ID:").pack(pady=5)
    entry_almacen_id = tk.Entry(ventana_inventario)
    entry_almacen_id.pack()

    tk.Label(ventana_inventario, text="Producto ID:").pack(pady=5)
    entry_producto_id = tk.Entry(ventana_inventario)
    entry_producto_id.pack()

    tk.Label(ventana_inventario, text="Material ID:").pack(pady=5)
    entry_material_id = tk.Entry(ventana_inventario)
    entry_material_id.pack()

    tk.Label(ventana_inventario, text="Cantidad:").pack(pady=5)
    entry_cantidad = tk.Entry(ventana_inventario)
    entry_cantidad.pack()

    def guardar_inventario():
        almacen_id = entry_almacen_id.get()
        producto_id = entry_producto_id.get()
        material_id = entry_material_id.get()
        cantidad = entry_cantidad.get()

        # Validación para asegurar que todos los campos estén completos
        if not almacen_id or not producto_id or not material_id or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query_inventario = """
                    INSERT INTO inventario (almacen_id, producto_id, material_id, inv_cantidad)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query_inventario, (almacen_id, producto_id, material_id, cantidad))
                conexion.commit()
                messagebox.showinfo("Éxito", "Inventario registrado correctamente.")
                ventana_inventario.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo registrar el inventario: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_inventario, text="Guardar Inventario", command=guardar_inventario).pack(pady=20)
def registrar_movimiento():
    ventana_movimiento = tk.Toplevel()
    ventana_movimiento.title("Registrar Movimiento de Inventario")
    ventana_movimiento.geometry("600x500")

    tk.Label(ventana_movimiento, text="Registrar Movimiento de Inventario", font=("Arial", 14)).pack(pady=10)

    # Inputs para el movimiento
    tk.Label(ventana_movimiento, text="Inventario ID:").pack(pady=5)
    entry_inventario_id = tk.Entry(ventana_movimiento)
    entry_inventario_id.pack()

    tk.Label(ventana_movimiento, text="Tipo de Movimiento (Entrada/Salida/Transferencia):").pack(pady=5)
    entry_tipo_movimiento = tk.Entry(ventana_movimiento)
    entry_tipo_movimiento.pack()

    tk.Label(ventana_movimiento, text="Cantidad:").pack(pady=5)
    entry_cantidad = tk.Entry(ventana_movimiento)
    entry_cantidad.pack()

    tk.Label(ventana_movimiento, text="Descripción:").pack(pady=5)
    entry_descripcion = tk.Entry(ventana_movimiento, width=50)
    entry_descripcion.pack()

    def guardar_movimiento():
        inventario_id = entry_inventario_id.get()
        tipo_movimiento = entry_tipo_movimiento.get()
        cantidad = entry_cantidad.get()
        descripcion = entry_descripcion.get()

        # Validación de campos
        if not inventario_id or not tipo_movimiento or not cantidad or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Validación tipo de movimiento
        if tipo_movimiento not in ['Entrada', 'Salida', 'Transferencia']:
            messagebox.showerror("Error", "Tipo de movimiento inválido. Debe ser 'Entrada', 'Salida' o 'Transferencia'.")
            return

        conexion = conectar_base_datos()
        if conexion:
            try:
                cursor = conexion.cursor()
                query_movimiento = """
                    INSERT INTO movimientos_inventario (inventario_id, mov_tipo_movimiento, mov_cantidad, mov_fecha_movimiento, mov_descripcion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                fecha_movimiento = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(query_movimiento, (inventario_id, tipo_movimiento, cantidad, fecha_movimiento, descripcion))
                conexion.commit()
                messagebox.showinfo("Éxito", "Movimiento de inventario registrado correctamente.")
                ventana_movimiento.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo registrar el movimiento: {err}")
            finally:
                conexion.close()

    tk.Button(ventana_movimiento, text="Guardar Movimiento", command=guardar_movimiento).pack(pady=20)
def listar_inventarios():
    ventana_listar_inventarios = tk.Toplevel()
    ventana_listar_inventarios.title("Inventarios")
    ventana_listar_inventarios.geometry("600x400")

    tk.Label(ventana_listar_inventarios, text="Inventarios Registrados", font=("Arial", 14)).pack(pady=10)

    # Listbox para mostrar inventarios
    listbox_inventarios = tk.Listbox(ventana_listar_inventarios, width=80, height=10)
    listbox_inventarios.pack(pady=10)

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query_inventario = """
                SELECT i.inventario_id, a.almacen_id, p.pro_nombre, m.mat_nombre, i.inv_cantidad
                FROM inventario i
                JOIN almacenes a ON i.almacen_id = a.almacen_id
                JOIN producto p ON i.producto_id = p.producto_id
                JOIN material m ON i.material_id = m.material_id
            """
            cursor.execute(query_inventario)
            inventarios = cursor.fetchall()

            for inventario in inventarios:
                listbox_inventarios.insert(tk.END, f"ID: {inventario[0]} | Almacén: {inventario[1]} | Producto: {inventario[2]} | Material: {inventario[3]} | Cantidad: {inventario[4]}")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo obtener los inventarios: {err}")
        finally:
            conexion.close()
def gestionar_inventarios():
    ventana_inventarios = tk.Toplevel()
    ventana_inventarios.title("Gestión de Inventarios")
    ventana_inventarios.geometry("500x400")

    tk.Label(ventana_inventarios, text="Gestión de Inventarios", font=("Arial", 14)).pack(pady=10)

    tk.Button(ventana_inventarios, text="Registrar Inventario", command=registrar_inventario).pack(pady=5)
    tk.Button(ventana_inventarios, text="Registrar Movimiento", command=registrar_movimiento).pack(pady=5)
    tk.Button(ventana_inventarios, text="Listar Inventarios", command=listar_inventarios).pack(pady=5)
    tk.Button(ventana_inventarios, text="Cerrar", command=ventana_inventarios.destroy).pack(pady=10)
def verificar_contraseña():
    def validar():
        contraseña_ingresada = entry_contraseña.get()
        if contraseña_ingresada == "123":  # Cambia "admin123" por la contraseña deseada
            ventana_contraseña.destroy()
            abrir_menu_administrador()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta. Inténtalo de nuevo.")

    # Crear ventana emergente para ingresar contraseña
    ventana_contraseña = tk.Toplevel()
    ventana_contraseña.title("Verificación de Contraseña")
    ventana_contraseña.geometry("300x150")
    ventana_contraseña.resizable(False, False)
    
    tk.Label(ventana_contraseña, text="Introduce la contraseña:", font=("Arial", 12)).pack(pady=10)
    entry_contraseña = tk.Entry(ventana_contraseña, show="*", width=25)
    entry_contraseña.pack(pady=5)

    tk.Button(ventana_contraseña, text="Ingresar", command=validar).pack(pady=10)
def abrir_menu_administrador():
    ventana_admin = tk.Tk()
    ventana_admin.title("Menú Principal")
    ventana_admin.geometry("400x500")

    tk.Label(ventana_admin, text="Menú Principal", font=("Arial", 16)).pack(pady=10)
    
    tk.Button(ventana_admin, text="Gestión de Productos", command=gestionar_productos).pack(pady=5)
    tk.Button(ventana_admin, text="Gestión de Clientes", command=gestionar_clientes).pack(pady=5)
    tk.Button(ventana_admin, text="Gestión de Empleados", command=gestionar_empleados).pack(pady=5)
    tk.Button(ventana_admin, text="Gestión de Asistencia", command=gestionar_asistencia).pack(pady=5)
    tk.Button(ventana_admin, text="Gestion Pedidos", command=gestionar_pedidos).pack(pady=5)
    tk.Button(ventana_admin, text="Gestion Almacenes", command=gestionar_almacenes).pack(pady=5)
    tk.Button(ventana_admin, text="Gestion Materiales", command=gestionar_materiales).pack(pady=5)
    tk.Button(ventana_admin, text="Gestion Productos Almacen", command=gestionar_materiales).pack(pady=5)
    tk.Button(ventana_admin, text="Gestion Inventario", command=gestionar_inventarios).pack(pady=5)
    tk.Button(ventana_admin, text="Salir", command=ventana_admin.destroy).pack(pady=10)

    ventana_admin.mainloop()
def abrir_menu_usuario():
    ventana_usuario = tk.Toplevel()
    ventana_usuario.title("Menú de Usuario")
    ventana_usuario.geometry("300x200")
    ventana_usuario.config(bg="lightblue")
    
    tk.Label(ventana_usuario,font=("Courier New", 14),fg="blue", bg="lightblue").pack(pady=10)
    
    tk.Button(ventana_usuario, text="Registrar Pedido ",font=("Courier New", 10), command=registrar_pedido,fg="blue", bg="white").pack(pady=5)
    tk.Button(ventana_usuario, text="Salir",font=("Courier New", 10), command=ventana_usuario.destroy,fg="blue", bg="white").pack(pady=10)
def menu_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema Empresarial",)
    ventana_principal.geometry("300x200")
    ventana_principal.config(bg="lightblue")
    
    tk.Label(ventana_principal, text="Bienvenido", font=("Courier New", 14),fg="blue", bg="lightblue").pack(pady=10)
    tk.Button(ventana_principal, text="Administrador", font=("Courier New", 10),command=verificar_contraseña, fg="blue", bg="lightblue").pack(pady=5)
    tk.Button(ventana_principal, text="Usuario",font=("Courier New", 10), command=abrir_menu_usuario, fg="blue", bg="lightblue").pack(pady=5)
    tk.Button(ventana_principal, text="Salir",font=("Courier New", 10), command=ventana_principal.destroy, fg="blue", bg="lightblue").pack(pady=10)
    
    ventana_principal.mainloop()

menu_principal()