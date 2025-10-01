from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import equipamento as equipamento_crud
from schemas import equipamento as equipamento_schema
from core.database import get_db
from crud import leitura_sensor as leitura_sensor_crud
from schemas import leitura_sensor as leitura_sensor_schema

router = APIRouter()

@router.post("/", response_model=equipamento_schema.Equipamento)
def create_equipamento(equipamento: equipamento_schema.EquipamentoCreate, db: Session = Depends(get_db)):
    return equipamento_crud.create_equipamento(db=db, equipamento=equipamento)

@router.get("/{equipamento_id}/leituras", response_model=List[leitura_sensor_schema.LeituraSensor])
def read_leitura_sensors_by_equipamento_id(equipamento_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leitura_sensors = leitura_sensor_crud.get_leitura_sensors_by_equipamento_id(db, equipamento_id=equipamento_id, skip=skip, limit=limit)
    return leitura_sensors

@router.get("/", response_model=List[equipamento_schema.Equipamento])
def read_equipamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipamentos = equipamento_crud.get_equipamentos(db, skip=skip, limit=limit)
    return equipamentos

@router.get("/{equipamento_id}", response_model=equipamento_schema.Equipamento)
def read_equipamento(equipamento_id: int, db: Session = Depends(get_db)):
    db_equipamento = equipamento_crud.get_equipamento(db, equipamento_id=equipamento_id)
    if db_equipamento is None:
        raise HTTPException(status_code=404, detail="Equipamento not found")
    return db_equipamento

@router.put("/{equipamento_id}", response_model=equipamento_schema.Equipamento)
def update_equipamento(equipamento_id: int, equipamento: equipamento_schema.EquipamentoCreate, db: Session = Depends(get_db)):
    db_equipamento = equipamento_crud.update_equipamento(db, equipamento_id=equipamento_id, equipamento=equipamento)
    if db_equipamento is None:
        raise HTTPException(status_code=404, detail="Equipamento not found")
    return db_equipamento

@router.delete("/{equipamento_id}", response_model=equipamento_schema.Equipamento)
def delete_equipamento(equipamento_id: int, db: Session = Depends(get_db)):
    db_equipamento = equipamento_crud.delete_equipamento(db, equipamento_id=equipamento_id)
    if db_equipamento is None:
        raise HTTPException(status_code=404, detail="Equipamento not found")
    return db_equipamento
