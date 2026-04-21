from sqlalchemy import Column, Integer, String
from database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    plate_number = Column(String, unique=True, index=True)