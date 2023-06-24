#Создайте список из трех студентов. Данные для каждого студента запрашивает программа в консоли.
# Сущность студента — словарь. Ключи у словаря: имя, фамилия, возраст, курс, оценка по математике,
# оценка по английскому и оценка по физкультуре (оценки можете сгенерировать рандомно).
# Посчитайте для каждого студента средний бал и добавьте его к сущности студента в словаре.

student_1 ={'name': 'Igor', 'last_name': 'Savenya', 'Age': 20, 'course': 4,
            'score': {'math': 5, 'English': 9,
           'physical education grade': 7}}
student_2={'name': 'Alex', 'last_name': 'Soltan', 'Age': 20, 'course': 4,
            'score': {
                'math' : 2,
                'english': 5,
                'physical': 6
            }
           }
student_3 = {'name': 'Marina', 'last_name': 'Dailid', 'Age': 20, 'course': 4,
            'score': {
                'math' : 10,
                'english':10,
                'physical': 10
            }
           }
avg_1 = sum(student_1['score'].values()) / len(student_1['score'])
print(avg_1)
student_1['avg'] = avg_1
avg_2 = sum(student_2['score'].values()) / len(student_2['score'])
student_2['avg']= avg_2
avg_3 = sum(student_3['score'].values()) / len(student_3['score'])
student_3['avg']= avg_3
print(student_1)
print(student_2)
print(student_3)
