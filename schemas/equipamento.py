from pydantic import BaseModel
from models.equipamento import StatusEquipamento

class EquipamentoBase(BaseModel):
    marca: str
    modelo: str
    status: StatusEquipamento

class EquipamentoCreate(EquipamentoBase):
    pass

class EquipamentoStatusUpdate(BaseModel):
    status: StatusEquipamento
    

class Equipamento(EquipamentoBase):
    id: int

    class Config:
        from_attributes = True
