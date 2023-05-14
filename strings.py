# a = "Александр Сергеевич Пушкин"
# b = a [::2]
# print(b)
#
# string = "Александр Сергеевич Пушкин"
# print(string.split(" ", maxsplit=0))
#
a = range(0, 100)
for b in a:
    if b<2:
        continue
    c = range(2, b)
    simple = True
    for D in c:
        if b%D==0:
            simple = False
            break

    if simple == True:
        print(b)