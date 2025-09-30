from sqlalchemy.orm import Session
from models import leitura_sensor as leitura_sensor_model
from schemas import leitura_sensor as leitura_sensor_schema

def get_leitura_sensor(db: Session, leitura_sensor_id: int):
    return db.query(leitura_sensor_model.LeituraSensor).filter(leitura_sensor_model.LeituraSensor.id == leitura_sensor_id).first()

def get_leitura_sensors_by_equipamento_id(db: Session, equipamento_id: int, skip: int = 0, limit: int = 100):
    return db.query(leitura_sensor_model.LeituraSensor) \
        .filter(leitura_sensor_model.LeituraSensor.t_equipamento_id == equipamento_id) \
        .order_by(leitura_sensor_model.LeituraSensor.data_coleta.desc()) \
        .offset(skip) \
        .limit(limit) \
        .all()

def get_leitura_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(leitura_sensor_model.LeituraSensor).order_by(leitura_sensor_model.LeituraSensor.data_coleta.desc()).offset(skip).limit(limit).all()

def create_leitura_sensor(db: Session, leitura_sensor: leitura_sensor_schema.LeituraSensorCreate):
    db_leitura_sensor = leitura_sensor_model.LeituraSensor(**leitura_sensor.model_dump())
    db.add(db_leitura_sensor)
    db.commit()
    db.refresh(db_leitura_sensor)
    return db_leitura_sensor

def update_leitura_sensor(db: Session, leitura_sensor_id: int, leitura_sensor: leitura_sensor_schema.LeituraSensorCreate):
    db_leitura_sensor = db.query(leitura_sensor_model.LeituraSensor).filter(leitura_sensor_model.LeituraSensor.id == leitura_sensor_id).first()
    if db_leitura_sensor:
        for key, value in leitura_sensor.model_dump().items():
            setattr(db_leitura_sensor, key, value)
        db.commit()
        db.refresh(db_leitura_sensor)
    return db_leitura_sensor

def delete_leitura_sensor(db: Session, leitura_sensor_id: int):
    db_leitura_sensor = db.query(leitura_sensor_model.LeituraSensor).filter(leitura_sensor_model.LeituraSensor.id == leitura_sensor_id).first()
    if db_leitura_sensor:
        db.delete(db_leitura_sensor)
        db.commit()
    return db_leitura_sensor
