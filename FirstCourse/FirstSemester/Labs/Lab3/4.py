n = int(input("Введите число n >= 2: "))
while n < 2:
    print('Неправильно!!!!')
    n = int(input("Введите число n >= 2: "))

a = list()
for i in range(n + 1):
    a.append(i)
