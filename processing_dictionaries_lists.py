#создание 4 переменных account1, account2, account3, account4
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}


#создание 4 переменных user1, user2, user3, user4
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}


#создание списка user_list, где будут содержаться данные user1, user2, user3, user4
user_list = [user1, user2, user3, user4] 


# создание переменных для разбивки элементов из списка user_list по индексам
user_list1 = user_list[0]
user_list2 = user_list[1]
user_list3 = user_list[2]
user_list4 = user_list[3]



entry_key = input('Введите ключ (name или account): ')
entry_key_lower = entry_key.lower()


#вывод информации о всех пользователях или аккаунтах
if entry_key_lower == 'name':
    print(f"""Значение ключа {entry_key} для юзера 1 = {user1['name']}
Значение ключа {entry_key} для юзера 2 = {user2['name']}
Значение ключа {entry_key} для юзера 3 = {user3['name']}
Значение ключа {entry_key} для юзера 4 = {user4['name']}""")
elif entry_key_lower == 'account':
    print(f"""Значение ключа {entry_key} для аккаунта 1 = {account1['login']}
Значение ключа {entry_key} для аккаунта 2 = {account2['login']}
Значение ключа {entry_key} для аккаунта 3 = {account3['login']}
Значение ключа {entry_key} для аккаунта 4 = {account4['login']}""")
else:
    print('Введенный ключ не найден')


#вывод информации по порядковому номеру
serial_number = int(input('Введите порядковый номер: '))
if serial_number == 1:
    print(f"""Данные по юзеру № {serial_number}:
имя: {user_list1['name']}
возраст: {user_list1['age']}
логин: {''.join([x for x in user_list1['account'].get('login')])}
пароль: {''.join([y for y in user_list1['account'].get('password')])}""")
elif serial_number == 2:
    print(f"""Данные по юзеру № {serial_number}:
имя: {user_list2['name']}
возраст: {user_list2['age']}
логин: {''.join([x for x in user_list2['account'].get('login')])}
пароль: {''.join([y for y in user_list2['account'].get('password')])}""")
elif serial_number == 3:
    print(f"""Данные по юзеру № {serial_number}:
имя: {user_list3['name']}
возраст: {user_list3['age']}
логин: {''.join([x for x in user_list3['account'].get('login')])}
пароль: {''.join([y for y in user_list3['account'].get('password')])}""")
elif serial_number == 4:
    print(f"""Данные по юзеру № {serial_number}:
имя: {user_list4['name']}
возраст: {user_list4['age']}
логин: {''.join([x for x in user_list4['account'].get('login')])}
пароль: {''.join([y for y in user_list4['account'].get('password')])}""")
else:
    print('Пользователь с указанным номером не найден')


#перемещение данных указанного пользователя в конец списка
user_movement = int(input('Введите номер пользователя, которого нужно поместить в конец: '))
if user_movement == 1:
    print(f"""Список до изменения:
{user_list}
Пользователь с именем {user_list1['name']} перемещен в конец
Список после изменения:
{user_list2, user_list3, user_list4, user_list1}""")
elif user_movement == 2:
    print(f"""Список до изменения:
{user_list}
Пользователь с именем {user_list2['name']} перемещен в конец
Список после изменения:
{user_list1, user_list3, user_list4, user_list2}""")
elif user_movement == 3:
    print(f"""Список до изменения:
{user_list}
Пользователь с именем {user_list3['name']} перемещен в конец
Список после изменения:
{user_list1, user_list2, user_list4, user_list3}""")
elif user_movement == 4:
    print(f"""Список не изменён:
Пользователь с именем {user_list4['name']} находится в конце списка
{user_list}""")
else:
    print('Пользователь с указанным номером не найден')


#рассчитываем средний возраст указанных пользователей
ages = [user_list1['age'], user_list2['age'], user_list3['age'], user_list4['age']]
average_age = sum(ages) / len(ages)
print(f'Средний возраст всех юзеров - {average_age}')