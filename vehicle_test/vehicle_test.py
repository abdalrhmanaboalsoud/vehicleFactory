import pytest
from vehicle.factory import Factory
from vehicle.car import Car
from vehicle.motorcycle import Motor


@pytest.fixture
def car():
    return Car("petrol", "Toyota Corolla", "red")

@pytest.fixture
def motor():
    return Motor("DUD", "petrol")

def test_factory():
    with pytest.raises(ValueError):
        f = Factory("invalid fuel type", "model")

def test_car(car):
    assert car._model_name == "Toyota Corolla"
    assert car._color == "red"
    assert car._fuel_type == "petrol"
    assert car._num_doors == 4

def test_motor(motor):
    assert motor._model_name == "DUD"
    assert motor._fuel_type == "petrol"
    assert motor._wheels == 2

    motor.set_model("new model")
    assert motor.get_model() == "new model"
