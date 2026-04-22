import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Variables del archivo .env al entorno del sistema
load_dotenv()

# URL de conexión
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError(
        "DATABASE_URL no está definida. "
        "Verificá que exista un archivo .env en la carpeta backend/ "
        "con la variable DATABASE_URL configurada."
    )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    Dependency de FastAPI que provee una sesión de base de datos.
    Se abre al iniciar un request y se cierra automáticamente al terminar,
    incluso si hay error (gracias al try/finally).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()