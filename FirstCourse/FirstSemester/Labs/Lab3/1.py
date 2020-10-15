seq = input("Введите фразу с точкой на конце: ")
while seq[-1] != '.':
    print("Нет точки!")
    seq = input("Введите фразу с точкой на конце: ")

print("Длина строки: ", len(seq))
words = []
word = ''
for i in range(len(seq)):
    if seq[i].isalpha():
        word += seq[i]
    elif len(word) != 0:
        words.append(word)
        word = ''

print(words)
len_words = [len(item) for item in words]
print("Кол-во слов: ", len(words))
print("Длина самого короткого: ", min(len_words), "\nДлина самого длинного: ", max(len_words))
new_seq = seq.replace('*', '')
double_seq = ''
for i in range(len(new_seq)):
    double_seq += new_seq[i] * 2
print("Строка без *, удвоенная в каждой позиции: ", double_seq)
