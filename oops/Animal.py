class Animal:

    species = "Dogs" # class-level attribute

    def __init__(self, name, color):
        self.name = name # instance-level attribute
        self.color = color # instance-level attribute

    def __eq__(self, value, /):
        return self.name == value.name and self.color == value.color

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, color={self.color})"

    def __hash__(self):
        return hash((self.name, self.color))


