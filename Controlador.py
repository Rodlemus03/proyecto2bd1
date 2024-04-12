from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Area(Base):
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    permitir_fumar = Column(Boolean)
    mesas = relationship("Mesa")

class Mesa(Base):
    __tablename__ = 'mesas'
    id = Column(Integer, primary_key=True)
    id_area = Column(Integer, ForeignKey('areas.id'))
    capacidad = Column(Integer)
    movible = Column(Boolean)
    area = relationship("Area", back_populates="mesas")

class ElementoMenu(Base):
    __tablename__ = 'elemento_menu'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    precio = Column(Float)

class Orden(Base):
    __tablename__ = 'ordenes'
    id = Column(Integer, primary_key=True)
    id_mesa = Column(Integer, ForeignKey('mesas.id'))
    id_mesero = Column(Integer, ForeignKey('meseros.id'))
    timestamp = Column(DateTime, default=datetime.now)
    items = relationship("ElementoOrden")

class ElementoOrden(Base):
    __tablename__ = 'elemento_ordenes'
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer, ForeignKey('ordenes.id'))
    id_elemento_menu = Column(Integer, ForeignKey('elemento_menu.id'))
    cantidad = Column(Integer)
    orden = relationship("Orden", back_populates="items")
    elemento_menu = relationship("ElementoMenu")

class Mesero(Base):
    __tablename__ = 'meseros'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    id_area = Column(Integer, ForeignKey('areas.id'))
    area = relationship("Area")

class Encuesta(Base):
    __tablename__ = 'encuestas'
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer, ForeignKey('ordenes.id'))
    amabilidad_mesero = Column(Integer)
    exactitud_pedido = Column(Integer)
    orden = relationship("Orden")

class Queja(Base):
    __tablename__ = 'quejas'
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    fecha_hora = Column(DateTime, default=datetime.now)
    motivo = Column(String)
    clasificacion = Column(Integer)
    personal_afectado = Column(String)
    elemento_menu = Column(Integer, ForeignKey('elemento_menu.id'))  # Columna opcional si hay asociación con un elemento del menú
    cliente = relationship("Cliente")

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    quejas = relationship("Queja")

# Configura la conexión a la base de datos
engine = create_engine('postgresql://postgres:pelu1503@localhost:5432/proyecto2')
Base.metadata.create_all(engine)

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()
