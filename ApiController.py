from flask import Flask, jsonify, request
from backend import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API para la entidad Usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios_api():
    usuarios = obtener_usuarios()
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def crear_usuario_api():
    data = request.json
    nuevo_usuario = crear_usuario(data['username'], data['password'], data['roles'])
    return jsonify(nuevo_usuario)

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario_api(usuario_id):
    usuario = obtener_usuario_por_id(usuario_id)
    return jsonify(usuario)

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario_api(usuario_id):
    data = request.json
    usuario_actualizado = actualizar_usuario(usuario_id, data['username'], data['password'], data['roles'])
    return jsonify(usuario_actualizado)

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario_api(usuario_id):
    eliminar_usuario(usuario_id)
    return '', 204  # No Content

# API para la entidad Áreas
@app.route('/areas', methods=['GET'])
def obtener_areas_api():
    areas = obtener_areas()
    return jsonify(areas)

@app.route('/areas', methods=['POST'])
def crear_area_api():
    data = request.json
    nueva_area = crear_area(data['nombre'], data['fumadores'])
    return jsonify(nueva_area)

@app.route('/areas/<int:area_id>', methods=['GET'])
def obtener_area_api(area_id):
    area = obtener_area_por_id(area_id)
    return jsonify(area)

@app.route('/areas/<int:area_id>', methods=['PUT'])
def actualizar_area_api(area_id):
    data = request.json
    area_actualizada = actualizar_area(area_id, data['nombre'], data['fumadores'])
    return jsonify(area_actualizada)

@app.route('/areas/<int:area_id>', methods=['DELETE'])
def eliminar_area_api(area_id):
    eliminar_area(area_id)
    return '', 204  # No Content
# API para la entidad Mesas
@app.route('/mesas', methods=['GET'])
def obtener_mesas_api():
    mesas = obtener_mesas()
    return jsonify(mesas)

@app.route('/mesas', methods=['POST'])
def crear_mesa_api():
    data = request.json
    nueva_mesa = crear_mesa(data['area_id'], data['capacidad'], data['movible'])
    return jsonify(nueva_mesa)

@app.route('/mesas/<int:mesa_id>', methods=['GET'])
def obtener_mesa_api(mesa_id):
    mesa = obtener_mesa_por_id(mesa_id)
    return jsonify(mesa)

@app.route('/mesas/<int:mesa_id>', methods=['PUT'])
def actualizar_mesa_api(mesa_id):
    data = request.json
    mesa_actualizada = actualizar_mesa(mesa_id, data['area_id'], data['capacidad'], data['movible'])
    return jsonify(mesa_actualizada)

@app.route('/mesas/<int:mesa_id>', methods=['DELETE'])
def eliminar_mesa_api(mesa_id):
    eliminar_mesa(mesa_id)
    return '', 204  # No Content

# API para la entidad Platos
@app.route('/platos', methods=['GET'])
def obtener_platos_api():
    platos = obtener_platos()
    return jsonify(platos)

@app.route('/platos', methods=['POST'])
def crear_plato_api():
    data = request.json
    nuevo_plato = crear_plato(data['nombre'], data['descripcion'], data['precio'])
    return jsonify(nuevo_plato)

@app.route('/platos/<int:plato_id>', methods=['GET'])
def obtener_plato_api(plato_id):
    plato = obtener_plato_por_id(plato_id)
    return jsonify(plato)

@app.route('/platos/<int:plato_id>', methods=['PUT'])
def actualizar_plato_api(plato_id):
    data = request.json
    plato_actualizado = actualizar_plato(plato_id, data['nombre'], data['descripcion'], data['precio'])
    return jsonify(plato_actualizado)

@app.route('/platos/<int:plato_id>', methods=['DELETE'])
def eliminar_plato_api(plato_id):
    eliminar_plato(plato_id)
    return '', 204  # No Content
# API para la entidad Bebidas
@app.route('/bebidas', methods=['GET'])
def obtener_bebidas_api():
    bebidas = obtener_bebidas()
    return jsonify(bebidas)

@app.route('/bebidas', methods=['POST'])
def crear_bebida_api():
    data = request.json
    nueva_bebida = crear_bebida(data['nombre'], data['descripcion'], data['precio'])
    return jsonify(nueva_bebida)

@app.route('/bebidas/<int:bebida_id>', methods=['GET'])
def obtener_bebida_api(bebida_id):
    bebida = obtener_bebida_por_id(bebida_id)
    return jsonify(bebida)

@app.route('/bebidas/<int:bebida_id>', methods=['PUT'])
def actualizar_bebida_api(bebida_id):
    data = request.json
    bebida_actualizada = actualizar_bebida(bebida_id, data['nombre'], data['descripcion'], data['precio'])
    return jsonify(bebida_actualizada)

@app.route('/bebidas/<int:bebida_id>', methods=['DELETE'])
def eliminar_bebida_api(bebida_id):
    eliminar_bebida(bebida_id)
    return '', 204  # No Content

# API para la entidad Clientes
@app.route('/clientes', methods=['GET'])
def obtener_clientes_api():
    clientes = obtener_clientes()
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def crear_cliente_api():
    data = request.json
    nuevo_cliente = crear_cliente(data['nombre'], data['nit'], data['direccion'])
    return jsonify(nuevo_cliente)

@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def obtener_cliente_api(cliente_id):
    cliente = obtener_cliente_por_id(cliente_id)
    return jsonify(cliente)

@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def actualizar_cliente_api(cliente_id):
    data = request.json
    cliente_actualizado = actualizar_cliente(cliente_id, data['nombre'], data['nit'], data['direccion'])
    return jsonify(cliente_actualizado)

@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def eliminar_cliente_api(cliente_id):
    eliminar_cliente(cliente_id)
    return '', 204  # No Content
# API para la entidad Pedidos
@app.route('/pedidos', methods=['GET'])
def obtener_pedidos_api():
    pedidos = obtener_pedidos()
    return jsonify(pedidos)

@app.route('/pedidos', methods=['POST'])
def crear_pedido_api():
    data = request.json
    nuevo_pedido = crear_pedido(data['mesa_id'], data['cliente_id'])
    return jsonify(nuevo_pedido)

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def obtener_pedido_api(pedido_id):
    pedido = obtener_pedido_por_id(pedido_id)
    return jsonify(pedido)

@app.route('/pedidos/<int:pedido_id>', methods=['PUT'])
def actualizar_pedido_api(pedido_id):
    data = request.json
    pedido_actualizado = actualizar_pedido(pedido_id, data['mesa_id'], data['cliente_id'])
    return jsonify(pedido_actualizado)

@app.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
def eliminar_pedido_api(pedido_id):
    eliminar_pedido(pedido_id)
    return '', 204  # No Content

# API para la entidad PedidoPlatos
@app.route('/pedidos/<int:pedido_id>/platos', methods=['POST'])
def agregar_plato_a_pedido_api(pedido_id):
    data = request.json
    agregar_plato_a_pedido(pedido_id, data['plato_id'], data['cantidad'])
    return '', 204  # No Content

@app.route('/pedidos/<int:pedido_id>/platos', methods=['GET'])
def obtener_platos_de_pedido_api(pedido_id):
    platos_pedido = obtener_platos_de_pedido(pedido_id)
    return jsonify(platos_pedido)

@app.route('/pedidos/<int:pedido_id>/platos/<int:plato_id>', methods=['DELETE'])
def eliminar_plato_de_pedido_api(pedido_id, plato_id):
    eliminar_plato_de_pedido(pedido_id, plato_id)
    return '', 204  # No Content
# API para la entidad PedidosBebidas
@app.route('/pedidos/<int:pedido_id>/bebidas', methods=['POST'])
def agregar_bebida_a_pedido_api(pedido_id):
    data = request.json
    agregar_bebida_a_pedido(pedido_id, data['bebida_id'], data['cantidad'])
    return '', 204  # No Content

@app.route('/pedidos/<int:pedido_id>/bebidas', methods=['GET'])
def obtener_bebidas_de_pedido_api(pedido_id):
    bebidas_pedido = obtener_bebidas_de_pedido(pedido_id)
    return jsonify(bebidas_pedido)

@app.route('/pedidos/<int:pedido_id>/bebidas/<int:bebida_id>', methods=['DELETE'])
def eliminar_bebida_de_pedido_api(pedido_id, bebida_id):
    eliminar_bebida_de_pedido(pedido_id, bebida_id)
    return '', 204  # No Content

# API para la entidad Cuentas
@app.route('/cuentas', methods=['POST'])
def crear_cuenta_api():
    data = request.json
    pedido_id = data.get('pedido_id')
    total = data.get('total')
    propina = data.get('propina')
    cerrada = data.get('cerrada', False)
    id_mesa = data.get('id_mesa')  # Nuevo campo id_mesa
    
    # Insertar datos en la tabla cuentas
    nueva_cuenta = crear_cuenta(pedido_id, total, propina, cerrada, id_mesa)
    
    return jsonify(nueva_cuenta)


@app.route('/cuentas', methods=['GET'])
def obtener_cuentas_api():
    cuentas = obtener_cuentas()
    return jsonify(cuentas)

@app.route('/cuentas/<int:cuenta_id>', methods=['GET'])
def obtener_cuenta_api(cuenta_id):
    cuenta = obtener_cuenta_por_id(cuenta_id)
    return jsonify(cuenta)

@app.route('/cuentas/<int:cuenta_id>', methods=['PUT'])
def actualizar_cuenta_api(cuenta_id):
    data = request.json
    cuenta_actualizada = actualizar_cuenta(cuenta_id, data['total'], data.get('propina'), data.get('cerrada', False))
    return jsonify(cuenta_actualizada)

@app.route('/cuentas/<int:cuenta_id>', methods=['DELETE'])
def eliminar_cuenta_api(cuenta_id):
    eliminar_cuenta(cuenta_id)
    return '', 204  # No Content
# API para la entidad FormasPago
@app.route('/cuentas/<int:cuenta_id>/formas-pago', methods=['POST'])
def agregar_forma_pago_a_cuenta_api(cuenta_id):
    data = request.json
    agregar_forma_pago_a_cuenta(cuenta_id, data['monto'], data['forma'])
    return '', 204  # No Content

@app.route('/cuentas/<int:cuenta_id>/formas-pago', methods=['GET'])
def obtener_formas_pago_de_cuenta_api(cuenta_id):
    formas_pago = obtener_formas_pago_de_cuenta(cuenta_id)
    return jsonify(formas_pago)

@app.route('/cuentas/<int:cuenta_id>/formas-pago/<int:forma_pago_id>', methods=['DELETE'])
def eliminar_forma_pago_de_cuenta_api(cuenta_id, forma_pago_id):
    eliminar_forma_pago_de_cuenta(cuenta_id, forma_pago_id)
    return '', 204  # No Content

# API para la entidad Encuestas
@app.route('/encuestas', methods=['POST'])
def crear_encuesta_api():
    data = request.json
    nueva_encuesta = crear_encuesta(data['cliente_id'], data['amabilidad'], data['exactitud'])
    return jsonify(nueva_encuesta)

@app.route('/encuestas', methods=['GET'])
def obtener_encuestas_api():
    encuestas = obtener_encuestas()
    return jsonify(encuestas)

@app.route('/encuestas/<int:encuesta_id>', methods=['GET'])
def obtener_encuesta_api(encuesta_id):
    encuesta = obtener_encuesta_por_id(encuesta_id)
    return jsonify(encuesta)

@app.route('/encuestas/<int:encuesta_id>', methods=['PUT'])
def actualizar_encuesta_api(encuesta_id):
    data = request.json
    encuesta_actualizada = actualizar_encuesta(encuesta_id, data['amabilidad'], data['exactitud'])
    return jsonify(encuesta_actualizada)

@app.route('/encuestas/<int:encuesta_id>', methods=['DELETE'])
def eliminar_encuesta_api(encuesta_id):
    eliminar_encuesta(encuesta_id)
    return '', 204  # No Content
# API para la entidad Quejas
@app.route('/quejas', methods=['POST'])
def crear_queja_api():
    data = request.json
    nueva_queja = crear_queja(
        data['cliente_id'], 
        data['motivo'], 
        data['clasificacion'], 
        data.get('personal'),
        data.get('plato_id'),
        data.get('bebida_id')
    )
    return jsonify(nueva_queja)

@app.route('/quejas', methods=['GET'])
def obtener_quejas_api():
    quejas = obtener_quejas()
    return jsonify(quejas)

@app.route('/quejas/<int:queja_id>', methods=['GET'])
def obtener_queja_api(queja_id):
    queja = obtener_queja_por_id(queja_id)
    return jsonify(queja)

@app.route('/quejas/<int:queja_id>', methods=['PUT'])
def actualizar_queja_api(queja_id):
    data = request.json
    queja_actualizada = actualizar_queja(
        queja_id, 
        data['motivo'], 
        data['clasificacion'], 
        data.get('personal'),
        data.get('plato_id'),
        data.get('bebida_id')
    )
    return jsonify(queja_actualizada)

@app.route('/quejas/<int:queja_id>', methods=['DELETE'])
def eliminar_queja_api(queja_id):
    eliminar_queja(queja_id)
    return '', 204  # No Content
#Login
@app.route('/login', methods=['POST'])
def login_route():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if username and password:
            if login(username, password):
                return jsonify({'success': True, 'message': 'Login successful'})
            else:
                return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
        else:
            return jsonify({'success': False, 'message': 'Missing username or password'}), 400
    else:
        return jsonify({'success': False, 'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
