words_lines = list()
words = list()
with open('input.txt', 'r', encoding='utf-8') as file_in:
    lines = (file_in.read() + '.').split('\n')
    j = 0
    for line in lines:
        line = line + "."
        word = ''
        for i in range(len(line)):
            if line[i].isalpha():
                word += line[i]
            elif len(word) != 0:
                words.append(word)
                word = ''
        words_lines.append([])
        for word in words:
            words_lines[j].append(word)
        j += 1
        words.clear()


with open('output.txt', 'w', encoding='utf-8') as file_out:
    word_to_delete = input("Введите слово для удаления: ")
    for word_line in words_lines:
        for word in word_line:
            if word != word_to_delete:
                file_out.write(word + " ")
        file_out.write('\n')
