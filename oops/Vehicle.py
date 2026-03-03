class Vehicle:
    def __init__(self, make, model, year, color=None):
        self._make = make  # Private attribute
        self._model = model
        self._year = year
        self._color = color

    # Encapsulation: Getters and Setters
    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    # Methods
    def start_engine(self):
        print(f"{self._make} {self._model}'s engine started.")

    def stop_engine(self):
        print(f"{self._make} {self._model}'s engine stopped.")

    def drive(self, speed=0):
        print(f"{self._make} {self._model} is driving at {speed} km/h.")