from base import data_input, data_output

user_input = str()
while True:
    print('1.) Вывод данных', '2.) Ввод данных', '3.) Выход', sep='\n')
    user_input = input()
    if user_input == '2':
        data_input()
        continue
    elif user_input == '1':
        data_output()
        continue
    elif user_input == '3':
        break
    else:
        print('Ошибка ввода, попробуйте ещё раз')
        continue
