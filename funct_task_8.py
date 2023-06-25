#Напишите программу для вычисления квадратных уравнений.
def equa(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (b * -1 + D**0.5)/2 * a
        x2 = (b * -1 - D**0.5)/2 * a
        return x1, x2
    elif D == 0:
        x = b * -1/ 2*a
        return x

print(equa(5, 3, -26))
