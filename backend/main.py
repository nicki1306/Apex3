from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Apex API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENDPOINT 
@app.post("/vehicles/")
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    
    db_vehicle = models.Vehicle(
        brand=vehicle.brand,
        model=vehicle.model,
        plate_number=vehicle.plate_number
    )
    
    # sesión 
    db.add(db_vehicle)
    
    db.commit()
    
    db.refresh(db_vehicle)
    
    return {"mensaje": "¡Vehículo registrado con éxito!", "vehiculo": db_vehicle}

@app.get("/vehicles/")
def read_vehicles(db: Session = Depends(get_db)):

    vehiculos = db.query(models.Vehicle).all()
    

    return vehiculos

# traer UN SOLO VEHÍCULO POR SU ID
@app.get("/vehicles/{vehicle_id}")
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    
    # Filtro
    vehiculo = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    
    # Si no existe
    if vehiculo is None:
        return {"error": "Vehículo no encontrado en la base de datos"}
        
    return vehiculo

@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not db_vehicle:
        return {"error": "Vehículo no encontrado"}
    db.delete(db_vehicle)
    db.commit()
    return {"message": "Vehículo eliminado"}