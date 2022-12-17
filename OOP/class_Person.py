class Person:
    def __init__(self, name, age, profession, blood_type):
        self.name = name
        self.age = age
        self.profession = profession
        self.blood_type = blood_type

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
    def blood_type(self):
        return self._blood_type

    @blood_type.setter
    def blood_type(self, blood_type):
        self._blood_type = blood_type

    def add_age(self):
        self.age += 5
