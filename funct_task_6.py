#Напишите программу которая принимает неопределенное количество аргументов и
# именованный параметр action, значения для него: ‘+’ или ‘*’,
# что значит нужно вернуть сумму или произведение из переданных аргументов.
# Реализовать тремя функциями.

def myfunc(*args, action):
   if action == "+":
       return mysum(args)
   else: return mymultiply(args)

def mysum(args):
    return sum(args)
def mymultiply(args):
    s = 1
    for elem in args:
        s *= elem
    return s

print(myfunc(1, 2, 3, action='+'))

b = myfunc(1, 2, 3, 4, action='*')
print(b) 
