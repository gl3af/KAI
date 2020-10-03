# 5 вариант
import random

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
while n <= 0 and m <= 0:
    print("Некорректный ввод!")
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))

a = [[0] * m for i in range(n)]

a_neg = 0
a_pos = 0

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(-100, 100)
        print(a[i][j], end=" ")
        if a[i][j] > 0:
            a_pos += 1
        if a[i][j] < 0:
            a_neg += 1
    print()
print(f"Отрицательных: {a_neg}, положительных: {a_pos}")
