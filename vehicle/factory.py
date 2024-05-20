from abc import ABC, abstractmethod

class Factory(ABC):
    _ALLOWED_FUEL_TYPES = {"electric", "petrol", "diesel"}
    _number_of_vehicle = 0
    def __init__(self, fuel_type, model_name):
        if fuel_type not in self._ALLOWED_FUEL_TYPES:
            raise ValueError(f"Invalid fuel type: {fuel_type}. Allowed types are: {', '.join(self._ALLOWED_FUEL_TYPES)}")
        self._fuel_type = fuel_type
        Factory._number_of_vehicle +=1
        self._model_name = model_name
        
    def set_model_name(self, new_model_name):
        self._model_name = new_model_name