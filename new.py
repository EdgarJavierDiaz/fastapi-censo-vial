from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Conexión a PostgreSQL
DATABASE_URL = "postgresql://edgar:Indispinsuri2025@localhost:5432/censo_vial"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de ejemplo
class ReporteVial(Base):
    __tablename__ = "reportes_viales"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    departamento = Column(String, index=True)
    municipio = Column(String)
    estado_via = Column(String)
    clima = Column(String)
    orden_publico = Column(String)
    observaciones = Column(String)

# Crear la tabla en la base de datos
if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tabla creada y conexión exitosa")
    except Exception as e:
        print("❌ Error:", e)
