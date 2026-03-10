from Vehicle import Vehicle

class MotorBike(Vehicle):
    def __init__(self, make, model, year, color=None, gears=4): # Constructor
        # Constructor overriding: Call parent __init__ and add more
        super().__init__(make, model, year, color)
        self.gears = gears

    # Encapsulation for new attribute
    def get_gears(self):
        return self.gears

    def set_gears(self, gears):
        self.gears = gears

    # Method overriding
    def drive(self, speed=20):
        # Method overloading: Default speed different
        print(f"{self._make} {self._model} MotorBike is driving at {speed} km/h.")

    def honk(self):
        print("Honk! Honk!")
