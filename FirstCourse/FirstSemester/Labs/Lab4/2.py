# 5 вариант
import time


def through_recursion(n):
    if n == 0:
        return 1
    else:
        return through_recursion(n // 2) + through_recursion(n // 3)


def through_list(n):
    a = [0] * (n + 1)
    a[0] = 1
    for i in range(1, n + 1):
        a[i] = a[i // 2] + a[i // 3]
    return a[n]


def main():
    n = int(input("Введите число n >= 0: "))
    while n < 0:
        print("Неверный ввод")
        n = int(input("Введите число n >=0: "))
    start_time = time.time()
    print(through_recursion(n))
    end_time = time.time()
    print("recursion time =", end_time - start_time, "seconds")
    start_time = time.time()
    print(through_list(n))
    end_time = time.time()
    print("list time =", end_time - start_time, "seconds")


if __name__ == '__main__':
    main()
