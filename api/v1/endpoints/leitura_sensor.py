from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import leitura_sensor as leitura_sensor_crud
from schemas import leitura_sensor as leitura_sensor_schema
from core.database import get_db
from model.ModelExecutor import ModelExecutor

router = APIRouter()

@router.post("/")
def create_leitura_sensor(leitura_sensor: leitura_sensor_schema.LeituraSensorBase, db: Session = Depends(get_db)):
    model_executor = ModelExecutor.get_instance()
    prediction = model_executor.predict_leitura_sensor(leitura_sensor)
    leitura_data_for_db = {
        **leitura_sensor.model_dump(),
        "status": prediction
    }

    leitura_data_for_db = leitura_sensor_schema.LeituraSensorCreate(**leitura_data_for_db)
    return leitura_sensor_crud.create_leitura_sensor(db=db, leitura_sensor=leitura_data_for_db)

@router.get("/", response_model=List[leitura_sensor_schema.LeituraSensor])
def read_leitura_sensors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leitura_sensors = leitura_sensor_crud.get_leitura_sensors(db, skip=skip, limit=limit)
    return leitura_sensors

@router.get("/{leitura_sensor_id}", response_model=leitura_sensor_schema.LeituraSensor)
def read_leitura_sensor(leitura_sensor_id: int, db: Session = Depends(get_db)):
    db_leitura_sensor = leitura_sensor_crud.get_leitura_sensor(db, leitura_sensor_id=leitura_sensor_id)
    if db_leitura_sensor is None:
        raise HTTPException(status_code=404, detail="LeituraSensor not found")
    return db_leitura_sensor

@router.put("/{leitura_sensor_id}", response_model=leitura_sensor_schema.LeituraSensor)
def update_leitura_sensor(leitura_sensor_id: int, leitura_sensor: leitura_sensor_schema.LeituraSensorCreate, db: Session = Depends(get_db)):
    db_leitura_sensor = leitura_sensor_crud.update_leitura_sensor(db, leitura_sensor_id=leitura_sensor_id, leitura_sensor=leitura_sensor)
    if db_leitura_sensor is None:
        raise HTTPException(status_code=404, detail="LeituraSensor not found")
    return db_leitura_sensor

@router.delete("/{leitura_sensor_id}", response_model=leitura_sensor_schema.LeituraSensor)
def delete_leitura_sensor(leitura_sensor_id: int, db: Session = Depends(get_db)):
    db_leitura_sensor = leitura_sensor_crud.delete_leitura_sensor(db, leitura_sensor_id=leitura_sensor_id)
    if db_leitura_sensor is None:
        raise HTTPException(status_code=404, detail="LeituraSensor not found")
    return db_leitura_sensor
