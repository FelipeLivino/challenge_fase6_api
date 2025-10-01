import joblib
import pandas as pd
from schemas import leitura_sensor as leitura_sensor_schema

MODEL_PATH = "./model/best_model.pkl"

# make singleton to dont instantiate twice
model_executor = None
class ModelExecutor:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model = pd.read_pickle(model_path)

    
    def convert_to_sensor_list(self, leitura_sensor_obj: dict):
        sensor_list = [
            leitura_sensor_obj.get("temperatura", None),   # sensor_temperature
            leitura_sensor_obj.get("umidade", None),      # sensor_humidity
            leitura_sensor_obj.get("vibracao", None),           # sensor_ph
        ]
    
        return sensor_list

    def predict_leitura_sensor(self, leitura_sensor: leitura_sensor_schema.LeituraSensorBase) -> pd.DataFrame:
        X = self.convert_to_sensor_list(leitura_sensor.model_dump())
        prediction = self.predict([X])[0]

        return prediction

        
    def predict(self, X: list) -> list:
        if len(X[0]) != 3:
            raise ValueError("X has wrong format")
            
        return self.model.predict(X).tolist()

    @staticmethod
    def get_instance():
        global model_executor
        if model_executor is None:
            model_executor = ModelExecutor()
        return model_executor
