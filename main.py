from fastapi import FastAPI
from core.database import engine
from models import equipamento, sensor, leitura_sensor
from api.v1.api import api_router
from sqlalchemy import event
from sqlalchemy.schema import CreateSchema
from model.ModelExecutor import ModelExecutor

@event.listens_for(engine, 'connect')
def connect(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('CREATE SCHEMA IF NOT EXISTS reply')
    cursor.close()

equipamento.Base.metadata.create_all(bind=engine)
sensor.Base.metadata.create_all(bind=engine)
leitura_sensor.Base.metadata.create_all(bind=engine)

print("load do modelo")
model = ModelExecutor.get_instance()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(api_router, prefix="/api/v1")