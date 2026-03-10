# Demonstration of multiple inheritance
class Engine:

    def __init__(self, horse_power): # Constructor
        if not isinstance(horse_power, (int, float)) or horse_power <= 0:
            raise ValueError('Horse Power must be a positive number.')
        self.horse_power = horse_power

    def start_engine(self):
        print(f'Engine with {self.horse_power} HP started.')

class Wheels:
    def __init__(self, wheel_count):
        if not isinstance(wheel_count, int) or wheel_count <= 0:
            raise ValueError("Wheel count must be a positive integer.")
        self.wheel_count = wheel_count

    def rotate_wheels(self):
        print(f"{self.wheel_count} wheels are rotating.")

# multiple inheritance
class Automobile(Engine, Wheels):
    def __init__(self, horse_power, wheel_count, brand):
        # Call constructors of both parents explicitly
        Engine.__init__(self, horse_power)
        Wheels.__init__(self, wheel_count)
        self.brand = brand

    def drive(self):
        self.start_engine()
        self.rotate_wheels()
        print(f"{self.brand} automobile is now driving.")

