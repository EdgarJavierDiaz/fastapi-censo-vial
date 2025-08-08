from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker
import uuid
from datetime import datetime

# ⚠️ Reemplaza con tus credenciales reales
DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/tu_base_de_datos"

# Conexión y sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Base
Base = declarative_base()

# Modelos
class TramoVial(Base):
    __tablename__ = "tramos_viales"
    id = Column(Integer, primary_key=True, index=True)
    objectid = Column(Integer)
    categoria = Column(Integer)
    codigotramo = Column(String(20))
    postereferenciainicial = Column(Float)
    distancia_inicial = Column(Float)
    postereferenciafinal = Column(Float)
    distancia_final = Column(Float)
    nombreruta = Column(Text)
    sector = Column(Text)
    administrador = Column(String(50))
    fuente = Column(String(50))
    globalid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    nombretramo = Column(Text)
    created_user = Column(String(50))
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    last_edited_user = Column(String(50))
    last_edited_date = Column(TIMESTAMP, default=datetime.utcnow)
    territorial = Column(Integer)
    revisionestado = Column(String(50))
    shape_length = Column(Float)

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    cargo = Column(String(100))
    telefono = Column(String(20))
    correo = Column(String(100))
    region = Column(String(50))
    activo = Column(Boolean, default=True)

class ReporteFuncionario(Base):
    __tablename__ = "reportes_funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    tramo_id = Column(Integer, ForeignKey("tramos_viales.id"))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    fecha_reporte = Column(TIMESTAMP, default=datetime.utcnow)
    estado_tramo = Column(String(50))
    observaciones = Column(Text)
    foto_url = Column(Text)
    ubicacion_lat = Column(Float)
    ubicacion_lon = Column(Float)

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Insertar datos de prueba
tramo = TramoVial(
    objectid=1,
    categoria=2,
    codigotramo="TRM001",
    postereferenciainicial=0.0,
    distancia_inicial=0.0,
    postereferenciafinal=1.0,
    distancia_final=100.0,
    nombreruta="Ruta Nacional 1",
    sector="Sector Norte",
    administrador="Admin Vial",
    fuente="Fuente Oficial",
    nombretramo="Tramo Norte",
    created_user="admin",
    last_edited_user="admin",
    territorial=1,
    revisionestado="Revisado",
    shape_length=100.0
)

funcionario = Funcionario(
    nombre="Juan Pérez",
    cargo="Inspector",
    telefono="123456789",
    correo="juan.perez@example.com",
    region="Norte"
)

session.add(tramo)
session.add(funcionario)
session.commit()

reporte = ReporteFuncionario(
    tramo_id=tramo.id,
    funcionario_id=funcionario.id,
    estado_tramo="Bueno",
    observaciones="Sin novedades",
    foto_url="http://example.com/foto.jpg",
    ubicacion_lat=10.1234,
    ubicacion_lon=-75.1234
)

session.add(reporte)
session.commit()

print("✅ Datos de prueba insertados correctamente.")
