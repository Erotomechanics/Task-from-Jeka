from index import mycursor, mydb
from class_Person import Person


def data_input():
    person = Person(*input('Введите данные о человеке ').split())
    person_data = (person.name, person.age, person.profession, person.blood_type)
    sqlFormula = 'INSERT person (name, age, profession, blood_type) VALUES (%s, %s, %s, %s)'
    mycursor.execute(sqlFormula, person_data)
    mydb.commit()


def data_output():
    mycursor.execute('SELECT * FROM person')
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    input()
