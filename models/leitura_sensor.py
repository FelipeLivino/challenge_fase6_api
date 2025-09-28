import enum
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from models.base import Base

class StatusLeitura(str, enum.Enum):
    ATIVO = "ATIVO"
    INATIVO = "INATIVO"

class LeituraSensor(Base):
    __tablename__ = "t_leitura_sensor"
    __table_args__ = {'schema': 'reply'}

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(StatusLeitura), nullable=False)
    temperatura = Column(Numeric, nullable=False)
    umidade = Column(Numeric)
    vibracao = Column(Numeric, nullable=False)
    data_coleta = Column(DateTime(timezone=True), nullable=False)
    t_equipamento_id = Column(Integer, ForeignKey("reply.t_equipamento.id"), nullable=False)
    t_sensor_id = Column(Integer, ForeignKey("reply.t_sensor.id"), nullable=False)

    equipamento = relationship("Equipamento")
    sensor = relationship("Sensor")
