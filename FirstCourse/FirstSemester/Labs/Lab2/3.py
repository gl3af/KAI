string = input("Введите 6 чисел через запятую: ")
a = []
i = 0

while i < len(string):
    a.append(int(string[i]))
    i += 2

print("Четвёртый элемент: ", a[3])
print("В обратном порядке: ", a[::-1])
print("Сумма: ", sum(a), "\nСреднее арифметическое: ", sum(a)/len(a))
