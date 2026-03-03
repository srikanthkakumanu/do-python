# Parent class 1
class Engine:
   def start_engine(self):
       print("Engine started.")

# Parent class 2
class Wheels:
   def rotate_wheels(self):
       print("Wheels are rotating.")

# Child class inheriting from both Engine and Wheels
class Car(Engine, Wheels):
   def drive(self):
       print("Car is now driving.")

# Another child class inheriting from both Engine and Wheels
class Bike(Engine, Wheels):
   def ride(self):
       print("Bike is now riding.")

# Demonstration
if __name__ == "__main__":
   car = Car()
   car.start_engine() # From Engine
   car.rotate_wheels() # From Wheels
   car.drive() # From Car
   print("---")
   bike = Bike()
   bike.start_engine() # From Engine
   bike.rotate_wheels() # From Wheels
   bike.ride() # From Bike