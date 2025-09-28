from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import sensor as sensor_crud
from schemas import sensor as sensor_schema
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=sensor_schema.Sensor)
def create_sensor(sensor: sensor_schema.SensorCreate, db: Session = Depends(get_db)):
    return sensor_crud.create_sensor(db=db, sensor=sensor)

@router.get("/", response_model=List[sensor_schema.Sensor])
def read_sensors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sensors = sensor_crud.get_sensors(db, skip=skip, limit=limit)
    return sensors

@router.get("/{sensor_id}", response_model=sensor_schema.Sensor)
def read_sensor(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = sensor_crud.get_sensor(db, sensor_id=sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

@router.put("/{sensor_id}", response_model=sensor_schema.Sensor)
def update_sensor(sensor_id: int, sensor: sensor_schema.SensorCreate, db: Session = Depends(get_db)):
    db_sensor = sensor_crud.update_sensor(db, sensor_id=sensor_id, sensor=sensor)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

@router.delete("/{sensor_id}", response_model=sensor_schema.Sensor)
def delete_sensor(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = sensor_crud.delete_sensor(db, sensor_id=sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor
