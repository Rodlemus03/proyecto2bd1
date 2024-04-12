from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Controlador import Area, Mesa, ElementoMenu, Orden, ElementoOrden, Mesero, Encuesta, Queja, Cliente
from datetime import datetime
import json

app = Flask(__name__)

# Configura la conexión a la base de datos
engine = create_engine('postgresql://postgres:pelu1503@localhost:5432/proyecto2')
Session = sessionmaker(bind=engine)
session = Session()

# Rutas API para la entidad Area
@app.route('/areas', methods=['GET'])
def get_areas():
    areas = session.query(Area).all()
    areas_serializable = [area_to_dict(area) for area in areas]
    return jsonify(areas_serializable)

def area_to_dict(area):
    return {
        'id': area.id,
        'nombre': area.nombre,
        'permitir_fumar': area.permitir_fumar,
        # Agrega más campos según sea necesario
    }

# Rutas API para la entidad Mesa
# Añade aquí las rutas para las demás entidades siguiendo el mismo patrón

if __name__ == '__main__':
    app.run(debug=True)
