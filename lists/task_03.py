from random import randint
m = [
#    0  1  2
    [0, 1, 2], # 0
    [0, 1, 2], # 1
    [0, 1, 2], # 2
]

for x in range(len(m)):
    for y in range(len(m[x])):
        m[x][y] = randint(0, 20)
print(m)

min1 = m[0][0]
max1 = m[0][0]
for x in range(len(m)):
    for y in range(len(m[x])):
        if m[x][y] < min1:
            min1 = m[x][y]
        if m[x][y] > max1:
            max1 = m[x][y]

print("Min:", min1)
print("Max:", max1)
