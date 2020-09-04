number = int(input("Введите число: "))
first_digit = number // 100
number = (number - first_digit * 100) * 10 + first_digit

print("Конечный результат: ", number)
