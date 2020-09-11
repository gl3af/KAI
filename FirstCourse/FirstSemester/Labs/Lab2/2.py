phrase = input("Введите фразу: ")

print("Первые 4 символа: ", phrase[:4:1])
print("Последние 4 символа: ", phrase[-4::1])
print("Символ по середине: ", phrase[len(phrase) // 2])
print("Символы с 3-го по 8-ой: ", phrase[2:8])