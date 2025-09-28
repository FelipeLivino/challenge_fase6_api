import enum
from sqlalchemy import Column, Integer, String, Date, Enum
from models.base import Base

class StatusSensor(str, enum.Enum):
    ATIVO = "ATIVO"
    INATIVO = "INATIVO"

class Sensor(Base):
    __tablename__ = "t_sensor"
    __table_args__ = {'schema': 'reply'}

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    status = Column(Enum(StatusSensor), nullable=False)
    data_ativacao = Column(Date)
