import psycopg2
import getpass
import bcrypt 
def conectar_bd():
    # Establecer conexión con la base de datos
    try:
        conexion = psycopg2.connect(
            user="postgres",  
            password="riv22500/",  
            host="localhost",
            port="5432",
            database="proyecto2Consola"  
        )
        return conexion
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None
    
def abrirCuenta(conexion):
    try:
        cursor = conexion.cursor()
        mesa_id = input("Ingrese el ID de la mesa para abrir la cuenta: ")
        cursor.execute("INSERT INTO Cuentas (mesa_id) VALUES (%s)", (mesa_id,))
        conexion.commit()
        print("Cuenta abierta correctamente para la mesa", mesa_id)
    except (Exception, psycopg2.Error) as error:
        print("Error al abrir la cuenta:", error)

def cerrarCuenta(conexion):
    try:
        cursor = conexion.cursor()
        cuenta_id = input("Ingrese el ID de la cuenta para cerrarla: ")
        cursor.execute("UPDATE Cuentas SET estado = 'cerrada', fecha_cierre = CURRENT_TIMESTAMP WHERE cuenta_id = %s", (cuenta_id,))
        conexion.commit()
        print("Cuenta cerrada correctamente")
    except (Exception, psycopg2.Error) as error:
        print("Error al cerrar la cuenta:", error)
def agregarProducto(conexion):
    try:
        cursor = conexion.cursor()

        # Seleccionar todos los platos y bebidas
        cursor.execute("SELECT 'Plato', nombre, descripcion, precio,plato_id FROM Platos UNION ALL SELECT 'Bebida', nombre, descripcion, precio, bebida_id FROM Bebidas ORDER BY 1, 2")
        productos = cursor.fetchall()

        # Mostrar los productos
        print("Productos:")
        print("N° | Tipo  | Nombre              | Descripción                          | Precio")
        print("---|-------|---------------------|--------------------------------------|-------")
        for i, producto in enumerate(productos, start=1):
            tipo = producto[0]
            nombre = producto[1]
            descripcion = producto[2]
            precio = producto[3]
            print(f"{i:2d} | {tipo:<5}| {nombre:<20}| {descripcion:<38}| {precio:.2f}---{producto[len(producto)-1]}")
        print("Elige el producto ")

    except (Exception, psycopg2.Error) as error:
        print("Error al agregar producto:", error)


def facturar():
    pass
def verReportesCuenta():
    pass
def verMesasDisponibles(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT mesa_id FROM Mesas WHERE ocupada = false")
        mesas_disponibles = cursor.fetchall()
        
        if mesas_disponibles:
            print("Mesas disponibles:")
            for mesa in mesas_disponibles:
                print(f"Mesa {mesa[0]}")
        else:
            print("No hay mesas disponibles en este momento.")
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener las mesas disponibles:", error)
    pass
def JuntarMesas(conexion):
    try:
        cursor = conexion.cursor()
        
        cursor.execute("SELECT mesa_id, capacidad FROM Mesas WHERE movible = TRUE AND ocupada = FALSE")
        mesas_disponibles = cursor.fetchall()
        
        if not mesas_disponibles:
            print("No hay mesas disponibles para juntar en este momento.")
            return

        print("Mesas disponibles para juntar:")
        for mesa in mesas_disponibles:
            print(f"Mesa {mesa[0]} - Capacidad: {mesa[1]}")

        mesas_a_juntar = input("Ingrese los IDs de las mesas que desea juntar, separados por comas: ")
        mesas_a_juntar = [int(id) for id in mesas_a_juntar.split(',')]

        capacidades_seleccionadas = []
        for mesa_id in mesas_a_juntar:
            for mesa in mesas_disponibles:
                if mesa[0] == mesa_id:
                    capacidades_seleccionadas.append(mesa[1])

        nueva_capacidad = sum(capacidades_seleccionadas)
        print("Mesas juntadas correctamente. Nueva capacidad:", nueva_capacidad)

    except (Exception, psycopg2.Error) as error:
        print("Error al juntar las mesas:", error)
    pass
def VerPedidos():
    pass
def verPlatosEntrantes():
    pass
def recuentoDePlatos():
    
    pass

def verTragosEntrantes():
    pass
def recuentoTragos():
    pass

def platosMasVendidos(conexion):
    try:
        cursor = conexion.cursor()

        # Consulta para obtener los platos más vendidos
        consulta = """
        SELECT dp.plato_id, p.nombre AS nombre_plato, SUM(dp.cantidad) AS total_pedidos
        FROM Detalles_Pedido dp
        JOIN Platos p ON dp.plato_id = p.plato_id
        GROUP BY dp.plato_id, p.nombre
        ORDER BY total_pedidos DESC
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        print("Platos más vendidos:")
        for plato in resultados:
            print(f"{plato[1]}: {plato[2]} pedidos")

    except (Exception, psycopg2.Error) as error:
        print("Error al obtener los platos más vendidos:", error)
    pass

def reporteHorario(conexion):
    try:
        cursor = conexion.cursor()

        consulta = """
        SELECT DATE_PART('hour', fecha_apertura) AS hora, COUNT(*) AS cantidad_pedidos
        FROM Cuentas
        GROUP BY DATE_PART('hour', fecha_apertura)
        ORDER BY cantidad_pedidos DESC
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        print("Horario con más pedidos:")
        for hora, cantidad_pedidos in resultados:
            print(f"{int(hora)}:00 - {(int(hora) + 1) % 24}:00: {cantidad_pedidos} pedidos")

    except (Exception, psycopg2.Error) as error:
        print("Error al generar el reporte de horario:", error)
    pass


def promedioTiempo(conexion):
    try:
        cursor = conexion.cursor()

        consulta = """
        SELECT AVG(EXTRACT(EPOCH FROM (fecha_cierre - fecha_apertura))) AS promedio_tiempo_comida
        FROM Cuentas
        WHERE fecha_cierre IS NOT NULL
        """
        cursor.execute(consulta)
        resultado = cursor.fetchone()

        if resultado[0] is not None:
            promedio_segundos = resultado[0]
            promedio_minutos = promedio_segundos / 60
            print(f"El promedio de tiempo que las personas pasan en una mesa es de {promedio_minutos:.2f} minutos.")
        else:
            print("No hay suficientes datos para calcular el promedio de tiempo.")

    except (Exception, psycopg2.Error) as error:
        print("Error al calcular el promedio de tiempo:", error)
    pass
def reporteQuejasPersona(conexion):
    try:
        cursor = conexion.cursor()
        consulta = """
        SELECT persona_implicada, COUNT(*) AS cantidad_quejas
        FROM Quejas
        GROUP BY persona_implicada
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        print("Recuento de quejas por persona implicada:")
        for persona_implicada, cantidad_quejas in resultados:
            print(f"{persona_implicada}: {cantidad_quejas} quejas")

    except (Exception, psycopg2.Error) as error:
        print("Error al generar el reporte de quejas por persona implicada:", error)
    pass
def reporteQuejasPlato(conexion):
    try:
        cursor = conexion.cursor()
        consulta = """
        SELECT plato_bebida_implicado, COUNT(*) AS cantidad_quejas
        FROM Quejas
        GROUP BY plato_bebida_implicado
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        print("Recuento de quejas por plato implicado:")
        for plato_bebida_implicado, cantidad_quejas in resultados:
            print(f"{plato_bebida_implicado}: {cantidad_quejas} quejas")

    except (Exception, psycopg2.Error) as error:
        print("Error al generar el reporte de quejas por plato implicado:", error)
    
    pass


def reporteEficienciaMeseros(conexion):
    try:
        cursor = conexion.cursor()
        consulta = """
        SELECT AVG(calificacion_amabilidad) AS promedio_amabilidad, AVG(calificacion_exactitud) AS promedio_exactitud
        FROM Encuestas
        """
        cursor.execute(consulta)
        resultados = cursor.fetchone()
        promedio_amabilidad = resultados[0]
        promedio_exactitud = resultados[1]
        print(f"Promedio de calificación de amabilidad: {promedio_amabilidad}")
        print(f"Promedio de calificación de exactitud: {promedio_exactitud}")

    except (Exception, psycopg2.Error) as error:
        print("Error al generar el reporte de eficiencia de meseros:", error)
    pass
def agregarQueja(conexion):
    try:
        cursor = conexion.cursor()

        opcion = input("¿Sobre qué desea quejarse?").lower()
        if opcion == 'plato':
            cursor.execute("SELECT plato_id, nombre FROM Bebidas")
        opciones = cursor.fetchall()

        print(f"Opciones de {opcion}s disponibles:")
        for opcion in opciones:
            print(f"{opcion[0]} - {opcion[1]}")

        
        seleccion = int(input(f"Ingrese el ID de la {opcion} sobre la cual desea quejarse: "))

        if seleccion not in [opcion[0] for opcion in opciones]:
            print("ID de opción inválido.")
            return

        nombre_seleccionado = [opcion[1] for opcion in opciones if opcion[0] == seleccion][0]


        clasificacion = int(input("Indique qué tan grave es su molestia (1 - 5): "))
        if clasificacion < 1 or clasificacion > 5:
            print("La clasificación debe estar entre 1 y 5.")
            return

        persona_implicada = input("Indique quién está implicado: ")
        motivo = input("Ingrese el motivo de la queja: ")

        cursor.execute("INSERT INTO Quejas ( cliente_id, motivo, clasificacion, persona_implicada, plato_bebida_implicado) VALUES (%s,%s,%s,%s,%s)",
                       (6,motivo, clasificacion, persona_implicada, nombre_seleccionado))  # Reemplaza el cliente_id con el ID real del cliente
        conexion.commit()

        print("Queja agregada exitosamente.")

    except (Exception, psycopg2.Error) as error:
        print("Error al agregar la queja:", error)
    pass
def verQuejas():
    pass
def menu():
    cnx=conectar_bd()
    print("1. Cuentas ")
    print("2. Mesas ")
    print("3. Cocina ")
    print("4. Bar ")
    print("5. General ")
    print("6. Salir ")
    seleccion=input("Ingresa la opcion -->")
    if seleccion=="1":
        print("1. Abrir cuenta ")
        print("2. Agregar producto ")
        print("3. Cerrar cuenta ")
        print("4. Facturar ")
        seleccion=input("Ingresa la opcion correcta ")
        if seleccion=="1":
            abrirCuenta(cnx)
            menu()
        elif seleccion=="2":
            agregarProducto(cnx)
            menu()
        elif seleccion=="3":
            cerrarCuenta(cnx)
            menu()
        elif seleccion=="4":
            facturar()
        else:
            menu()

    elif seleccion=="2":
        print("1. Ver disponibles")
        print("2. Juntar mesas")
        print("3. Ver pedidos")
        seleccion=input("Ingresa la opcion correcta ")
        if seleccion=="1":
            verMesasDisponibles(cnx)
        elif seleccion=="2":
            JuntarMesas(cnx)
        elif seleccion=="3":
            VerPedidos()
        else:
            menu()
    elif seleccion=="3":
        print("1. Ver platos entrantes ")
        print("2. Recuento de platos ")
        print("3. Ver inventario  ")
        seleccion=input("Ingresa la opcion correcta ")
        if seleccion=="1":
            verPlatosEntrantes()
        elif seleccion=="2":
            recuentoDePlatos()
        elif seleccion=="3":
            verInventario()
        else:
            menu()
    elif seleccion=="4":
        print("1. Ver tragos entrantes")
        print("2. Recuento de tragos ")
        print("3. Ver inventario")
        seleccion=input("Ingresa la opcion correcta ")
        if seleccion=="1":
            verTragosEntrantes()
        elif seleccion=="2":
            recuentoTragos()
        elif seleccion=="3":
            verInventarioTragos()
        else:
            menu()
    elif seleccion=="5":
        print("1. Reportes ")
        print("2. Quejas ")
        seleccion=input("Ingresa la opcion correcta ")
        if seleccion=="1":
            print("1. Reporte de platos mas vendidos ")
            print("2. Horario en el que se ingresan mas pedidos ")
            print("3. Promedio de tiempo que tardan en comer ")
            print("4. Reporte de quejas por persona ")
            print("5. Reporte de quejas por plato ")
            print("6. Reporte de eficiencia de los meseros")
            seleccion=input("Ingresa la opcion que deseas ")
            if seleccion=="1":
                platosMasVendidos(cnx)
            elif seleccion=="2":
                reporteHorario(cnx)
            elif seleccion=="3":
                promedioTiempo(cnx)
            elif seleccion=="4":
                reporteQuejasPersona(cnx)
            elif seleccion=="5":
                reporteQuejasPlato(cnx)
            elif seleccion=="6":
                reporteEficienciaMeseros(cnx)
            else:
                menu()
        elif seleccion=="2":
            print("1. Agregar queja ")
            print("2. Ver quejas ")
            seleccion=input("Ingresa la opcion correcta ")
            if seleccion=="1":
                agregarQueja(cnx)
            elif seleccion=="2":
                verQuejas()
            else:
                menu()
 
        else:
            menu()
    elif seleccion=="6":
        print("Feliz dia ")
    else:
        print("Ingresa una opcion correcta ")
        menu()
def iniciar_sesion(conexion):
    cursor = conexion.cursor()
    usuario = input("Usuario: ")
    contraseña = getpass.getpass("Contraseña: ")  
    try:
        cursor.execute("SELECT usuario_id, tipo_usuario FROM Usuarios WHERE nombre_usuario = %s AND contraseña = %s", (usuario, contraseña))
        usuario = cursor.fetchone()
        if usuario:
            print("Inicio de sesión exitoso. Bienvenido,", usuario[1])
            menu()
        else:
            print("Usuario o contraseña incorrectos.")
    except (Exception, psycopg2.Error) as error:
        print("Error al iniciar sesión:", error)
        


def register(conexion):
    try:
        cursor = conexion.cursor()

        # Solicitar al usuario ingresar los datos
        usuario = input("Ingresa un nombre de usuario: ")
        contraseña = getpass.getpass("Ingresa una contraseña: ")
        confirmar_contraseña = getpass.getpass("Confirma tu contraseña: ")
        tipo_usuario = input("Ingresa el tipo de usuario: ")

        if contraseña != confirmar_contraseña:
            print("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")
            return

        hashed_password = encriptar_contraseña(contraseña)
        cursor.execute("INSERT INTO Usuarios (nombre_usuario, contraseña, tipo_usuario) VALUES (%s, %s, %s)", (usuario, hashed_password, tipo_usuario))
        conexion.commit()
        print("Usuario registrado exitosamente.")

    except (Exception, psycopg2.Error) as error:
        print("Error al registrar usuario:", error)

def encriptar_contraseña(contraseña):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
    return hashed_password



def main():
    conexion = conectar_bd()
    if conexion:
        iniciar_sesion(conexion)
        conexion.close()  

if __name__ == "__main__":
    main()
