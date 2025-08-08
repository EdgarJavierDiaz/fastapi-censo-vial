from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a PostgreSQL
# Reemplaza 'usuario', 'contraseña', 'localhost', '5432' y 'nombre_base' con tus datos reales
DATABASE_URL = "postgresql://edgar:Indispinsuri2025@localhost:5432/censo_vial"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base declarativa
Base = declarative_base()
