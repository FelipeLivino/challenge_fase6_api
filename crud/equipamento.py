from sqlalchemy.orm import Session
from models import equipamento as equipamento_model
from schemas import equipamento as equipamento_schema

def get_equipamento(db: Session, equipamento_id: int):
    return db.query(equipamento_model.Equipamento).filter(equipamento_model.Equipamento.id == equipamento_id).first()

def get_equipamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(equipamento_model.Equipamento).offset(skip).limit(limit).all()

def create_equipamento(db: Session, equipamento: equipamento_schema.EquipamentoCreate):
    db_equipamento = equipamento_model.Equipamento(**equipamento.dict())
    db.add(db_equipamento)
    db.commit()
    db.refresh(db_equipamento)
    return db_equipamento

def update_equipamento(db: Session, equipamento_id: int, equipamento: equipamento_schema.EquipamentoCreate):
    db_equipamento = db.query(equipamento_model.Equipamento).filter(equipamento_model.Equipamento.id == equipamento_id).first()
    if db_equipamento:
        for key, value in equipamento.dict().items():
            setattr(db_equipamento, key, value)
        db.commit()
        db.refresh(db_equipamento)
    return db_equipamento

def delete_equipamento(db: Session, equipamento_id: int):
    db_equipamento = db.query(equipamento_model.Equipamento).filter(equipamento_model.Equipamento.id == equipamento_id).first()
    if db_equipamento:
        db.delete(db_equipamento)
        db.commit()
    return db_equipamento
