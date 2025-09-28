from pydantic import BaseModel
from models.equipamento import StatusEquipamento

class EquipamentoBase(BaseModel):
    marca: str
    modelo: str
    status: StatusEquipamento

class EquipamentoCreate(EquipamentoBase):
    pass

class Equipamento(EquipamentoBase):
    id: int

    class Config:
        orm_mode = True
