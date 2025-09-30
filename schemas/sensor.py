from pydantic import BaseModel
from models.sensor import StatusSensor
from datetime import date

class SensorBase(BaseModel):
    nome: str
    status: StatusSensor
    data_ativacao: date | None = None

class SensorCreate(SensorBase):
    pass

class Sensor(SensorBase):
    id: int

    class Config:
        from_attributes = True
