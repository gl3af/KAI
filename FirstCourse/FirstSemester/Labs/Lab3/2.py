# 5 вариант
import random
n = int(input('Введите длину списка > 0: '))
while n <= 0:
    print('Отрицательное кол-во элементов... А вы смешной!')
    n = int(input('Введите длину списка > 0: '))

nums_list = list()
for i in range(n):
    nums_list.append(random.randint(-100, 100))
print(nums_list)

pos_count = 0
for i in range(n):
    if nums_list[i] > 0 and pos_count < 1:
        pos_count += 1
    elif nums_list[i] > 0 and pos_count >= 1:
        nums_list.append(nums_list[i])

pos_count = 0
i = 0
while i < n:
    if nums_list[i] > 0 and pos_count < 1:
        pos_count += 1
    elif nums_list[i] > 0 and pos_count >= 1:
        del nums_list[i]
        i -= 1
        n -= 1
    i += 1

print(nums_list)
