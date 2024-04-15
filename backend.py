import psycopg2
from psycopg2 import sql
import datetime

# Configuración de la conexión a la base de datos
conexion = psycopg2.connect(
    dbname="proyecto2",
    user="postgres",
    password="riv22500/",
    host="localhost",  # Cambia esto si tu base de datos está en otro host
    port="5432"        # Cambia esto si tu base de datos está en otro puerto
)

# Función para ejecutar una consulta y obtener los resultados
def ejecutar_consulta(consulta, parametros=None):
    try:
        with conexion.cursor() as cursor:
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            if cursor.description:
                column_names = [desc[0] for desc in cursor.description]
                return [dict(zip(column_names, row)) for row in cursor.fetchall()]
            else:
                return None
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta:", e)

# Operaciones CRUD para la entidad Usuarios
def crear_usuario(username, password_hash, roles):
    consulta = sql.SQL("""
        INSERT INTO Usuarios (username, password_hash, roles)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (username, password_hash, roles))

def obtener_usuarios():
    consulta = sql.SQL("""
        SELECT * FROM Usuarios
    """)
    return ejecutar_consulta(consulta)

def obtener_usuario_por_id(usuario_id):
    consulta = sql.SQL("""
        SELECT * FROM Usuarios
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (usuario_id,))

def actualizar_usuario(usuario_id, username, password_hash, roles):
    consulta = sql.SQL("""
        UPDATE Usuarios
        SET username = %s, password_hash = %s, roles = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (username, password_hash, roles, usuario_id))

def eliminar_usuario(usuario_id):
    consulta = sql.SQL("""
        DELETE FROM Usuarios
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (usuario_id,))

# Operaciones CRUD para la entidad Áreas
def crear_area(nombre, fumadores):
    consulta = sql.SQL("""
        INSERT INTO Areas (nombre, fumadores)
        VALUES (%s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, fumadores))

def obtener_areas():
    consulta = sql.SQL("""
        SELECT * FROM Areas
    """)
    return ejecutar_consulta(consulta)

def obtener_area_por_id(area_id):
    consulta = sql.SQL("""
        SELECT * FROM Areas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (area_id,))

def actualizar_area(area_id, nombre, fumadores):
    consulta = sql.SQL("""
        UPDATE Areas
        SET nombre = %s, fumadores = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, fumadores, area_id))

def eliminar_area(area_id):
    consulta = sql.SQL("""
        DELETE FROM Areas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (area_id,))
# Operaciones CRUD para la entidad Mesas
def crear_mesa(area_id, capacidad, movible):
    consulta = sql.SQL("""
        INSERT INTO Mesas (area_id, capacidad, movible)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (area_id, capacidad, movible))

def obtener_mesas():
    consulta = sql.SQL("""
        SELECT * FROM Mesas
    """)
    return ejecutar_consulta(consulta)

def obtener_mesa_por_id(mesa_id):
    consulta = sql.SQL("""
        SELECT * FROM Mesas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (mesa_id,))

def actualizar_mesa(mesa_id, area_id, capacidad, movible):
    consulta = sql.SQL("""
        UPDATE Mesas
        SET area_id = %s, capacidad = %s, movible = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (area_id, capacidad, movible, mesa_id))

def eliminar_mesa(mesa_id):
    consulta = sql.SQL("""
        DELETE FROM Mesas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (mesa_id,))

# Operaciones CRUD para la entidad Platos
def crear_plato(nombre, descripcion, precio):
    consulta = sql.SQL("""
        INSERT INTO Platos (nombre, descripcion, precio)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, descripcion, precio))

def obtener_platos():
    consulta = sql.SQL("""
        SELECT * FROM Platos
    """)
    return ejecutar_consulta(consulta)

def obtener_plato_por_id(plato_id):
    consulta = sql.SQL("""
        SELECT * FROM Platos
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (plato_id,))

def actualizar_plato(plato_id, nombre, descripcion, precio):
    consulta = sql.SQL("""
        UPDATE Platos
        SET nombre = %s, descripcion = %s, precio = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, descripcion, precio, plato_id))

def eliminar_plato(plato_id):
    consulta = sql.SQL("""
        DELETE FROM Platos
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (plato_id,))
# Operaciones CRUD para la entidad Bebidas
def crear_bebida(nombre, descripcion, precio):
    consulta = sql.SQL("""
        INSERT INTO Bebidas (nombre, descripcion, precio)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, descripcion, precio))

def obtener_bebidas():
    consulta = sql.SQL("""
        SELECT * FROM Bebidas
    """)
    return ejecutar_consulta(consulta)

def obtener_bebida_por_id(bebida_id):
    consulta = sql.SQL("""
        SELECT * FROM Bebidas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (bebida_id,))

def actualizar_bebida(bebida_id, nombre, descripcion, precio):
    consulta = sql.SQL("""
        UPDATE Bebidas
        SET nombre = %s, descripcion = %s, precio = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, descripcion, precio, bebida_id))

def eliminar_bebida(bebida_id):
    consulta = sql.SQL("""
        DELETE FROM Bebidas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (bebida_id,))

# Operaciones CRUD para la entidad Clientes
def crear_cliente(nombre, nit, direccion):
    consulta = sql.SQL("""
        INSERT INTO Clientes (nombre, nit, direccion)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, nit, direccion))

def obtener_clientes():
    consulta = sql.SQL("""
        SELECT * FROM Clientes
    """)
    return ejecutar_consulta(consulta)

def obtener_cliente_por_id(cliente_id):
    consulta = sql.SQL("""
        SELECT * FROM Clientes
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (cliente_id,))

def actualizar_cliente(cliente_id, nombre, nit, direccion):
    consulta = sql.SQL("""
        UPDATE Clientes
        SET nombre = %s, nit = %s, direccion = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (nombre, nit, direccion, cliente_id))

def eliminar_cliente(cliente_id):
    consulta = sql.SQL("""
        DELETE FROM Clientes
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (cliente_id,))
# Operaciones CRUD para la entidad Pedidos
def crear_pedido(mesa_id, cliente_id):
    consulta = sql.SQL("""
        INSERT INTO Pedidos (mesa_id, cliente_id)
        VALUES (%s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (mesa_id, cliente_id))

def obtener_pedidos():
    consulta = sql.SQL("""
        SELECT * FROM Pedidos
    """)
    return ejecutar_consulta(consulta)

def obtener_pedido_por_id(pedido_id):
    consulta = sql.SQL("""
        SELECT * FROM Pedidos
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (pedido_id,))

def actualizar_pedido(pedido_id, mesa_id, cliente_id):
    consulta = sql.SQL("""
        UPDATE Pedidos
        SET mesa_id = %s, cliente_id = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (mesa_id, cliente_id, pedido_id))

def eliminar_pedido(pedido_id):
    consulta = sql.SQL("""
        DELETE FROM Pedidos
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (pedido_id,))

# Operaciones CRUD para la entidad PedidoPlatos
def agregar_plato_a_pedido(pedido_id, plato_id, cantidad):
    consulta = sql.SQL("""
        INSERT INTO PedidoPlatos (pedido_id, plato_id, cantidad)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (pedido_id, plato_id, cantidad))

def obtener_platos_de_pedido(pedido_id):
    consulta = sql.SQL("""
        SELECT * FROM PedidoPlatos
        WHERE pedido_id = %s
    """)
    return ejecutar_consulta(consulta, (pedido_id,))

def eliminar_plato_de_pedido(pedido_id, plato_id):
    consulta = sql.SQL("""
        DELETE FROM PedidoPlatos
        WHERE pedido_id = %s AND plato_id = %s
    """)
    return ejecutar_consulta(consulta, (pedido_id, plato_id))
# Operaciones CRUD para la entidad PedidosBebidas
def agregar_bebida_a_pedido(pedido_id, bebida_id, cantidad):
    consulta = sql.SQL("""
        INSERT INTO PedidoBebidas (pedido_id, bebida_id, cantidad)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (pedido_id, bebida_id, cantidad))

def obtener_bebidas_de_pedido(pedido_id):
    consulta = sql.SQL("""
        SELECT * FROM PedidoBebidas
        WHERE pedido_id = %s
    """)
    return ejecutar_consulta(consulta, (pedido_id,))

def eliminar_bebida_de_pedido(pedido_id, bebida_id):
    consulta = sql.SQL("""
        DELETE FROM PedidoBebidas
        WHERE pedido_id = %s AND bebida_id = %s
    """)
    return ejecutar_consulta(consulta, (pedido_id, bebida_id))

# Operaciones CRUD para la entidad Cuentas
def crear_cuenta(pedido_id, total, propina=None, cerrada=False):
    consulta = """
        INSERT INTO Cuentas (pedido_id, total, propina, cerrada)
        VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    return ejecutar_consulta(consulta, (pedido_id, total, propina, cerrada))


def obtener_cuentas():
    consulta = sql.SQL("""
        SELECT * FROM Cuentas
    """)
    return ejecutar_consulta(consulta)

def obtener_cuenta_por_id(cuenta_id):
    consulta = sql.SQL("""
        SELECT * FROM Cuentas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (cuenta_id,))

def actualizar_cuenta(cuenta_id, total, propina=None, cerrada=False):
    consulta = sql.SQL("""
        UPDATE Cuentas
        SET total = %s, propina = %s, cerrada = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (total, propina, cerrada, cuenta_id))

def eliminar_cuenta(cuenta_id):
    consulta = sql.SQL("""
        DELETE FROM Cuentas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (cuenta_id,))
# Operaciones CRUD para la entidad FormasPago
def agregar_forma_pago_a_cuenta(cuenta_id, monto, forma):
    consulta = sql.SQL("""
        INSERT INTO FormasPago (cuenta_id, monto, forma)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (cuenta_id, monto, forma))

def obtener_formas_pago_de_cuenta(cuenta_id):
    consulta = sql.SQL("""
        SELECT * FROM FormasPago
        WHERE cuenta_id = %s
    """)
    return ejecutar_consulta(consulta, (cuenta_id,))

def eliminar_forma_pago_de_cuenta(cuenta_id, forma):
    consulta = sql.SQL("""
        DELETE FROM FormasPago
        WHERE cuenta_id = %s AND forma = %s
    """)
    return ejecutar_consulta(consulta, (cuenta_id, forma))

# Operaciones CRUD para la entidad Encuestas
def crear_encuesta(cliente_id, amabilidad, exactitud):
    consulta = sql.SQL("""
        INSERT INTO Encuestas (cliente_id, amabilidad, exactitud)
        VALUES (%s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (cliente_id, amabilidad, exactitud))

def obtener_encuestas():
    consulta = sql.SQL("""
        SELECT * FROM Encuestas
    """)
    return ejecutar_consulta(consulta)

def obtener_encuesta_por_id(encuesta_id):
    consulta = sql.SQL("""
        SELECT * FROM Encuestas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (encuesta_id,))

def actualizar_encuesta(encuesta_id, amabilidad, exactitud):
    consulta = sql.SQL("""
        UPDATE Encuestas
        SET amabilidad = %s, exactitud = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (amabilidad, exactitud, encuesta_id))

def eliminar_encuesta(encuesta_id):
    consulta = sql.SQL("""
        DELETE FROM Encuestas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (encuesta_id,))
# Operaciones CRUD para la entidad Quejas
def crear_queja(cliente_id, motivo, clasificacion, personal=None, plato_id=None, bebida_id=None):
    consulta = sql.SQL("""
        INSERT INTO Quejas (cliente_id, motivo, clasificacion, personal, plato_id, bebida_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (cliente_id, motivo, clasificacion, personal, plato_id, bebida_id))

def obtener_quejas():
    consulta = sql.SQL("""
        SELECT * FROM Quejas
    """)
    return ejecutar_consulta(consulta)

def obtener_queja_por_id(queja_id):
    consulta = sql.SQL("""
        SELECT * FROM Quejas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (queja_id,))

def actualizar_queja(queja_id, motivo, clasificacion, personal=None, plato_id=None, bebida_id=None):
    consulta = sql.SQL("""
        UPDATE Quejas
        SET motivo = %s, clasificacion = %s, personal = %s, plato_id = %s, bebida_id = %s
        WHERE id = %s
        RETURNING *
    """)
    return ejecutar_consulta(consulta, (motivo, clasificacion, personal, plato_id, bebida_id, queja_id))

def eliminar_queja(queja_id):
    consulta = sql.SQL("""
        DELETE FROM Quejas
        WHERE id = %s
    """)
    return ejecutar_consulta(consulta, (queja_id,))
#LOGIN
def login(username, password):
    consulta = sql.SQL("""
        SELECT * FROM Usuarios
        WHERE username = %s AND password_hash = %s
    """)
    resultado = ejecutar_consulta(consulta, (username, password))

    if resultado:
        return True
    else:
        return False
#REPORTES
# Reporte de los platos más pedidos por los clientes en un rango de fechas
def reporte_platos_mas_pedidos(fecha_inicio, fecha_fin):
    consulta = """
        SELECT pl.nombre AS plato, COUNT(pp.plato_id) AS veces_pedidos
        FROM Pedidos p
        JOIN PedidoPlatos pp ON p.id = pp.pedido_id
        JOIN Platos pl ON pp.plato_id = pl.id
        WHERE p.fecha_hora BETWEEN %s AND %s
        GROUP BY pl.nombre
        ORDER BY veces_pedidos DESC
        LIMIT 10;
    """
    return ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))

# Horario en el que se ingresan más pedidos entre un rango de fechas
def reporte_horario_pedidos(fecha_inicio, fecha_fin):
    consulta = """
        SELECT DATE_TRUNC('hour', fecha_hora) AS hora,
               COUNT(*) AS total_pedidos
        FROM Pedidos
        WHERE fecha_hora BETWEEN %s AND %s
        GROUP BY DATE_TRUNC('hour', fecha_hora)
        ORDER BY total_pedidos DESC
        LIMIT 1;
    """
    return ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))

# Reporte de las quejas agrupadas por persona para un rango de fechas
def reporte_quejas_por_persona(fecha_inicio, fecha_fin):
    consulta = """
        SELECT c.nombre AS cliente,
               q.motivo,
               COUNT(*) AS cantidad_quejas
        FROM Quejas q
        JOIN Clientes c ON q.cliente_id = c.id
        WHERE q.fecha_hora BETWEEN %s AND %s
        GROUP BY c.nombre, q.motivo
        ORDER BY cantidad_quejas DESC;
    """
    return ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))

# Reporte de las quejas agrupadas por plato para un rango de fechas
def reporte_quejas_por_plato(fecha_inicio, fecha_fin):
    consulta = """
        SELECT pl.nombre AS plato,
               q.motivo,
               COUNT(*) AS cantidad_quejas
        FROM Quejas q
        LEFT JOIN Platos pl ON q.plato_id = pl.id
        WHERE q.fecha_hora BETWEEN %s AND %s
        GROUP BY pl.nombre, q.motivo
        ORDER BY cantidad_quejas DESC;
    """
    return ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))
#Reporte de promedio de tiempo
def promedio_tiempo_comida_por_personas(fecha_inicio, fecha_fin):
    consulta = """
        SELECT ROUND(AVG(EXTRACT(EPOCH FROM (p.fecha_hora - c.fecha_hora)) / 60)::numeric, 2) AS tiempo_minutos,
               COUNT(*) AS cantidad_personas
        FROM Pedidos p
        JOIN Clientes c ON p.cliente_id = c.id
        WHERE p.cerrado = TRUE AND p.fecha_hora BETWEEN %s AND %s
        GROUP BY cantidad_personas
        ORDER BY cantidad_personas;
    """
    return ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))
# Reporte de eficiencia de meseros mostrando los resultados de las encuestas
def reporte_eficiencia_meseros():
    consulta = """
        SELECT EXTRACT(MONTH FROM e.fecha_hora) AS mes,
               e.amabilidad AS promedio_amabilidad,
               e.exactitud AS promedio_exactitud,
               c.nombre AS mesero
        FROM Encuestas e
        JOIN Clientes c ON e.cliente_id = c.id
        WHERE e.fecha_hora >= now() - INTERVAL '6 months'
        ORDER BY mesero, mes;
    """
    return ejecutar_consulta(consulta)







