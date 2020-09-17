phrase = input("Введите фразу: ")
while len(phrase) < 10:
    print('Фраза слишком короткая!')
    phrase = input("Введите фразу: ")

print("Первые 4 символа: ", phrase[:4:])
print("Последние 4 символа: ", phrase[-4::])
if len(phrase) % 2 != 0:
    print("Символ по середине: ", phrase[len(phrase) // 2])
else:
    print("Символы по середине: ", phrase[len(phrase) // 2 - 1:len(phrase) // 2 + 1])
print("Символы с 3-го по 8-ой: ", phrase[2:8])
