from pydantic import BaseModel
from models.leitura_sensor import StatusLeitura
from datetime import datetime

class LeituraSensorBase(BaseModel):
    temperatura: float
    umidade: float | None = None
    vibracao: float
    data_coleta: datetime
    t_equipamento_id: int
    t_sensor_id: int

class LeituraSensorCreate(LeituraSensorBase):
    status: StatusLeitura

class LeituraSensor(LeituraSensorCreate):
    id: int

    class Config:
        from_attributes = True
