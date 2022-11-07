from index import mycursor, mydb
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


user_input = str()
while True:
    print('1.) Вывод данных', '2.) Ввод данных', '3.) Выход',sep='\n')
    user_input = input()
    if user_input == '2':
        person = Person(*input('Введите данные о человеке ').split())
        person_data = (person.name, person.age, person.profession, person.blood_type)
        sqlFormula = 'INSERT person (name, age, profession, blood_type) VALUES (%s, %s, %s, %s)'
        mycursor.execute(sqlFormula, person_data)
        mydb.commit()
        continue
    elif user_input == '1':
        mycursor.execute('SELECT * FROM person')
        myresult = mycursor.fetchall()
        for row in myresult:
            print(row)
        input()
        continue
    elif user_input == '3':
        break
    else:
        print('Ошибка ввода, попробуйте ещё раз')
        continue
