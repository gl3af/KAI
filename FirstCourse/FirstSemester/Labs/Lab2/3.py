string = input("Введите 6 чисел через запятую: ")
a = string.split(',')

while len(a) != 6:
    print('Элементов должно быть 6!')
    string = input("Введите 6 чисел через запятую: ")
    a = string.split(',')

for i in range(len(a)):
    a[i] = int(a[i])
    ######

print("Четвёртый элемент: ", a[3])
print("В обратном порядке: ", a[::-1])
print("Сумма: ", sum(a), "\nСреднее арифметическое: ", sum(a)/len(a))
