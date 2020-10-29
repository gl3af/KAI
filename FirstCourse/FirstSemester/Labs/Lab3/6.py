import random

t = []
for x in range(0, 3):
    t.append([])
    for y in range(0, 5):
        t[x].append([])
        for z in range(0, 7):
            t[x][y].append(0)

for x in range(0, 3):
    for y in range(0, 5):
        for z in range(0, 7):
            t[x][y][z] = random.randint(0, 10001)

i = 0
j = 0
k = 0
t_max = t[0][0][0]
for x in range(0, 3):
    for y in range(0, 5):
        for z in range(0, 7):
            if t[x][y][z] > t_max:
                i = x
                j = y
                k = z
                t_max = t[x][y][z]

for z in range(0, 7):
    for x in range(0, 3):
        for y in range(0, 5):
            print(t[x][y][z], end=" ")
        print()
    print()
print(f"Максимум: {t_max}, координаты: ({i}, {j}, {k})")

