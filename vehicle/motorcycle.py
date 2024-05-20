from .factory import Factory


class Motor(Factory):
    def __init__(self, model_name, fuel_type, wheels=2):
        super().__init__(fuel_type, model_name)
        self._wheels = wheels
        self._model_name = model_name

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model
    
    def __str__(self):
        return f"Model: {self._model_name}, Fuel Type: {self._fuel_type}, Wheels: {self._wheels}"
    
    @classmethod
    def print_total_motorcycles(cls):
        print(f"Total number of motorcycles created: {cls._number_of_vehicle}")

        
        
moto = Motor("DUD", "petrol")
print(moto)
Motor.print_total_motorcycles()