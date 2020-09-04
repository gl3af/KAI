number = int(input("Введите число: "))
result = 0
multiplier = 100

while number > 0:
    result += number % 10 * multiplier
    multiplier /= 10
    number //= 10

print("Развёрнутое число: ", result)
