from fastapi import APIRouter
from api.v1.endpoints import equipamento, sensor, leitura_sensor

api_router = APIRouter()
api_router.include_router(equipamento.router, prefix="/equipamentos", tags=["equipamentos"])
api_router.include_router(sensor.router, prefix="/sensores", tags=["sensores"])
api_router.include_router(leitura_sensor.router, prefix="/leituras_sensores", tags=["leituras_sensores"])