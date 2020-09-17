# Вариант 5
x = float(input('Введите  -1<=x<=1: '))
while abs(x) > 1:
    print('Некорректный  ввод!')
    x = float(input('Введите -1<=x<=1: '))

n = int(input('Введите натуральное число n: '))
while n <= 0:
    print('Некорректный  ввод! Необходимо ввести натуральное число!')
    n = int(input('Введите n: '))

previous_element = x
step = x ** 2
sum_ = previous_element
for i in range(1, n + 1):
    sum_ += ((-1) * previous_element * step / (2 * i + 1))
    previous_element *= -1 * step

print(f'Сумма ряда для x = {x} при n = {n} равна {sum_}')
