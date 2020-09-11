# Вариант 5
x = -1
d = 0.1

while x <= 1:
    sum = 0
    for i in range(100000):
        if i % 2 == 0:
            sum += round(x, 1) ** (2*i + 1) / (2 * i + 1)
        else:
            sum -= round(x, 1) ** (2*i + 1) / (2 * i + 1)

    print("X: ", round(x, 1), " y(x): ", round(sum,2))
    x += d