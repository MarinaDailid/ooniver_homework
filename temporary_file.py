user = {
    'name': '',
    'lastname': '',
    'work':'',
    'age':'',
}

print("Данные пользователя 1")
user['name'] = input("Введите свое имя:")
user['lastname'] = input("Введите свою фамилию:")
user['work'] = input("Введите название места работы:")
user['age'] = input("Введите свой возраст:")
print(user['work'])
print('----------')
print(user['lastname'], user['name'], ',', user['age'])

user2 = {}
print("Данные пользователя 2")
user2['name'] = input("Введите свое имя:")
user2['lastname'] = input("Введите свою фамилию:")
user2['work'] = input("Введите название места работы:")
user2['age'] = input("Введите свой возраст:")

avg = (int(user['age']) + int(user2['age'])) // 2
print(avg)