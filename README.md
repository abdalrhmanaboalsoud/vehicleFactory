# Vehicle Factory

This project is an implementation of a vehicle factory, which can create different types of vehicles such as cars and motorcycles. The project uses object-oriented programming principles like inheritance and abstraction.

## Code Structure

The project consists of three main classes: `Factory`, `Car`, and `Motor`.

### Factory Class

The `Factory` class is an abstract base class that defines the common attributes and methods for all types of vehicles. It has the following attributes:

- `_ALLOWED_FUEL_TYPES`: A set of allowed fuel types.
- `_number_of_vehicle`: A class variable that keeps track of the total number of vehicles created.
- `_fuel_type`: The type of fuel the vehicle uses.
- `_model_name`: The model name of the vehicle.

The `Factory` class also has a method `set_model_name` to set the model name of the vehicle.

### Car Class

The `Car` class inherits from the `Factory` class and represents a car. It has additional attributes:

- `_color`: The color of the car.
- `_num_doors`: The number of doors the car has (default is 4).

The `Car` class also has methods to set the color and number of doors, and a class method to print the total number of cars created.

### Motor Class

The `Motor` class, representing a motorcycle, also inherits from the `Factory` class. It has an additional attribute:

- `_wheels`: The number of wheels the motorcycle has (default is 2).

The `Motor` class also has methods to set and get the model, and a class method to print the total number of motorcycles created.

## Tests

The project includes unit tests written using the `pytest` framework. The tests cover the functionality of the `Factory`, `Car`, and `Motor` classes. Pytest fixtures are used to create `Car` and `Motor` instances for the tests.
