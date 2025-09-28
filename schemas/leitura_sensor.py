from pydantic import BaseModel
from models.leitura_sensor import StatusLeitura
from datetime import datetime

class LeituraSensorBase(BaseModel):
    status: StatusLeitura
    temperatura: float
    umidade: float | None = None
    vibracao: float
    data_coleta: datetime
    t_equipamento_id: int
    t_sensor_id: int

class LeituraSensorCreate(LeituraSensorBase):
    pass

class LeituraSensor(LeituraSensorBase):
    id: int

    class Config:
        orm_mode = True
