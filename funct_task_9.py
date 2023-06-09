#Написать программу, которая запрашивает у пользователя фразу или слово и проверяет, является ли
# это палиндромом.
def reversed(text):
    res = ''
    for i in range(len(text)-1, -1, -1):
        res += text[i]
    return res

text = input()
if text == reversed(text):
    print('это палиндром')
else:
    print('это не палиндром')
