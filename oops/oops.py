from Vehicle import Vehicle
from Car import Car
from Person import Person
from Animal import Animal
from MotorBike import MotorBike
from Engine import Engine
from Engine import Wheels
from Engine import Automobile

def vehicles():
    # Vehicle example
    vehicle = Vehicle("Generic", "ModelX", 2020, "Black")
    vehicle.start_engine()
    vehicle.drive(60)
    vehicle.stop_engine()

    # Encapsulation example
    print(f"Vehicle color: {vehicle.get_color()}")
    vehicle.set_color("Red")
    print(f"Updated vehicle color: {vehicle.get_color()}")

    # Car example (inheritance)
    car = Car("Toyota", "Camry", 2022, "Blue", 4)
    car.start_engine()
    car.drive()  # Overridden method, default speed 50
    car.drive(80)  # Method overloading
    car.honk()
    car.stop_engine()

    # MotorBike example (inheritance)
    bike = MotorBike("Yamaha", "RX100", 2002, "Blue", 2)
    bike.start_engine()
    bike.drive()  # Overridden method, default speed 50
    bike.drive(100)  # Method overloading
    bike.honk()
    bike.stop_engine()

    # Constructor overloading example
    car2 = Car("Honda", "Civic", 2021)  # Using defaults for color and num_doors

def persons():
    person = Person("1", "Dave", 21, "Irvine, CA", "M")
    print(person.__str__())
    person.welcome()

def animals():
    dog = Animal('Juli', 'Brown')
    dog.species = 'Dogs'
    print(dog)
    print(dog.species)
    del dog # Can delete the objects

# Multiple inheritance
def auto_mobiles():
    try:
        am = Automobile(150, 4, "Toyota")
        am.drive()
    except ValueError as e:
        print("Error:", e)

    # Show Method Resolution Order
    print("\nMRO for Automobile class:", Automobile.mro())

# Examples
if __name__ == "__main__":
    # vehicles()
    # persons()
    # animals()

    auto_mobiles()