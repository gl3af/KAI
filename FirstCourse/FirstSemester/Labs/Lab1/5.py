number = int(input("Введите число: "))
sum_of_digits = 0
product = 1

while number > 0:
    sum_of_digits += number % 10
    product *= number % 10
    number //= 10

print("Сумма цифр: ", sum_of_digits)
print("Произведение цифр: ", product)
