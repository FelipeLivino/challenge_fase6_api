from sqlalchemy.orm import Session
from models import sensor as sensor_model
from schemas import sensor as sensor_schema

def get_sensor(db: Session, sensor_id: int):
    return db.query(sensor_model.Sensor).filter(sensor_model.Sensor.id == sensor_id).first()

def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sensor_model.Sensor).offset(skip).limit(limit).all()

def create_sensor(db: Session, sensor: sensor_schema.SensorCreate):
    db_sensor = sensor_model.Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def update_sensor(db: Session, sensor_id: int, sensor: sensor_schema.SensorCreate):
    db_sensor = db.query(sensor_model.Sensor).filter(sensor_model.Sensor.id == sensor_id).first()
    if db_sensor:
        for key, value in sensor.dict().items():
            setattr(db_sensor, key, value)
        db.commit()
        db.refresh(db_sensor)
    return db_sensor

def delete_sensor(db: Session, sensor_id: int):
    db_sensor = db.query(sensor_model.Sensor).filter(sensor_model.Sensor.id == sensor_id).first()
    if db_sensor:
        db.delete(db_sensor)
        db.commit()
    return db_sensor
