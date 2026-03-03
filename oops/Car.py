from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, color=None, num_doors=4):
        # Constructor overriding: Call parent __init__ and add more
        super().__init__(make, model, year, color)
        self._num_doors = num_doors

    # Encapsulation for new attribute
    def get_num_doors(self):
        return self._num_doors

    def set_num_doors(self, num_doors):
        self._num_doors = num_doors

    # Method overriding
    def drive(self, speed=50):
        # Method overloading: Default speed different
        print(f"{self._make} {self._model} car is driving at {speed} km/h.")

    def honk(self):
        print("Honk! Honk!")
