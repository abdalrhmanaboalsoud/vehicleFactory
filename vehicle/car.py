from .factory import Factory

class Car(Factory):
    def __init__(self, fuel_type,model_name, color, num_doors=4):
        super().__init__(fuel_type, model_name)
        self._model_name = model_name
        self._color = color
        self._num_doors = num_doors

    def set_color(self, new_color):
        self._color = new_color

    def set_num_doors(self, new_num_doors):
        if new_num_doors not in (2, 4):
            raise ValueError("Number of doors must be either 2 or 4")
        self._num_doors = new_num_doors

    @classmethod
    def print_total_cars(cls):
        print(f"Total number of cars created: {cls._number_of_vehicle}")

    def __str__(self):
        return f"Model: {self._model_name}, Color: {self._color}, Fuel Type: {self._fuel_type}, Number of Doors: {self._num_doors}"
    
car1 = Car("petrol", "Toyota Corolla", "red")
car2 = Car("electric", "Tesla Model S", "blue", num_doors=2)

print(car1)
print(car2)
Car.print_total_cars()
