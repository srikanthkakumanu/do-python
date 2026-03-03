class Person:

    # instance attributes: id, name, age, address, gender are instance attributes that are unique each person object.
    def __init__(self, id=None, name=None, age=0, address=None, gender=None):
        super().__init__()
        self.__id = id
        self.__name = name
        self._age = age
        self._address = address
        self.gender = gender

    def __get_id(self):
        return self.__id

    def __set_id(self, id):
        self.__id = id

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    def __get_age(self):
        return self._age

    def __set_age(self, age):
        self._age = age

    def __get_address(self):
        return self._address

    def __set_address(self, address):
        self._address = address

    def __get_gender(self):
        return self.gender

    def __set_gender(self, gender):
        self.gender = gender

    def __str__(self):
        return f"Person(id={self.__id}, name={self.__name}, age={self._age}, address={self._address}, gender={self.gender})"

    def __hash__(self):
        return hash((self.__id, self.__name, self._age, self._address, self.gender))

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.__id == other.__id and self.__name == other.__name and \
                   self._age == other._age and self._address == other._address and \
                   self.gender == other.gender
        return False

    def greet(self):
        return f'Hi, {self.__name}'

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")