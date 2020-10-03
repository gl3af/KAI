n = int(input("Введите число n >= 2: "))
while n < 2:
    print('Неправильно!!!!')
    n = int(input("Введите число n >= 2: "))

a = list()
b = list()
for i in range(n + 1):
    a.append(i)

for i in range(2, n + 1):
    if a[i] != 0:
        p = i
        for j in range(2*p, n + 1, p):
            a[j] = 0

print("Все кратные 7 на промежутке [1,n]: ", end=" ")
for i in range(7, n + 1, 7):
    print(i, end=" ")

print(f"\nМаксимальное простое на промежутке [0,n]: {max(a)}")
