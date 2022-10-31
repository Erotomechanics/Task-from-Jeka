class Person:
    def __init__(self, name, age, profession, id):
        self.name = name
        self.age = age
        self.profession = profession
        self.id = id
        self.__kgb = 5

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession):
        self._profession = profession

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def add_age(self):
        self.age += 5


class Doctor(Person):
    def __init__(self, name, age, id, profession):
        super().__init__(name, age, id, profession)
        self.pacients = []
        self.number_of_operations = 0
print()
sfdfghf