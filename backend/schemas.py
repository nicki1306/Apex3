from pydantic import BaseModel

class VehicleCreate(BaseModel):
    brand: str
    model: str
    plate_number: str