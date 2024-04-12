from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from Controlador import Area, Mesa, ElementoMenu, Orden, ElementoOrden, Mesero, Encuesta, Queja

# Configura la conexión a la base de datos
engine = create_engine('postgresql://postgres:pelu1503@localhost:5432/proyecto2')

Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de ingreso de datos

# nueva área
nueva_area = Area(nombre='Salón Principal', permitir_fumar=False)
session.add(nueva_area)

# mesa en el área creada
nueva_mesa = Mesa(id_area=nueva_area.id, capacidad=4, movible=True)
session.add(nueva_mesa)

# nuevo elemento de menú
nuevo_elemento_menu = ElementoMenu(nombre='Hamburguesa', descripcion='Deliciosa hamburguesa con queso y tocino', precio=10.99)
session.add(nuevo_elemento_menu)

# nuevo mesero
nuevo_mesero = Mesero(nombre='Juan', id_area=nueva_area.id)
session.add(nuevo_mesero)

session.commit()

# Ejemplo de consulta (select)

# todas las áreas y las imprimimos
print("Áreas:")
for area in session.query(Area).all():
    print(area.id, area.nombre, area.permitir_fumar)

#todas las mesas y las imprimimos
print("\nMesas:")
for mesa in session.query(Mesa).all():
    print(mesa.id, mesa.id_area, mesa.capacidad, mesa.movible)

# todos los elementos de menú y los imprimimos
print("\nElementos de Menú:")
for elemento in session.query(ElementoMenu).all():
    print(elemento.id, elemento.nombre, elemento.descripcion, elemento.precio)

# todos los meseros y los imprimimos
print("\nMeseros:")
for mesero in session.query(Mesero).all():
    print(mesero.id, mesero.nombre, mesero.id_area)

session.close()
