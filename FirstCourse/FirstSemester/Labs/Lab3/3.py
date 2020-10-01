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

pos_min = 0
min_pos = 101
pos_max = 0
max_neg = -101
for i in range(n):
    if 0 < nums_list[i] < min_pos:
        pos_min = i
        min_pos = nums_list[i]
    if max_neg < nums_list[i] < 0:
        pos_max = i
        max_neg = nums_list[i]

print(pos_min, pos_max)
if pos_min < pos_max:
    i = pos_min + 1
    while i < pos_max:
        del nums_list[i]
        pos_max -= 1
elif pos_min > pos_max:
    i = pos_max + 1
    while i < pos_min:
        del nums_list[i]
        pos_min -= 1

print(nums_list)
