import enum
from sqlalchemy import Column, Integer, String, Enum
from models.base import Base

class StatusEquipamento(str, enum.Enum):
    DESLIGADO = "DESLIGADO"
    NORMAL = "NORMAL"
    ATENCAO = "ATENCAO"
    FALHA = "FALHA"

class Equipamento(Base):
    __tablename__ = "t_equipamento"
    __table_args__ = {'schema': 'reply'}

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    status = Column(Enum(StatusEquipamento), nullable=False)
