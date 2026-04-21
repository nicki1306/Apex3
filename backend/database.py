from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ACÁ ESTÁ LA MAGIA: Le agregamos "+pg8000" después de postgresql
SQLALCHEMY_DATABASE_URL = "postgresql+pg8000://postgres:paloma13@localhost:5432/apex3_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()