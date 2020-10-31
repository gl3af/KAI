import time
import threading
from random import randint

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
strings = list()


def main():
    while True:
        string = ''
        for j in range(10):
            char = letters[randint(0, 51)]
            string += char
        strings.append(string)
        time.sleep(1)


def console_writer():
    while True:
        time.sleep(1)
        print(strings)


def file_writer():
    while True:
        time.sleep(5)
        with open('output.txt', 'w') as f:
            strings.sort()
            f.write('\n'.join(strings))


thread_main = threading.Thread(target=main, name='name')
thread_console = threading.Thread(target=console_writer, name='cw')
thread_file = threading.Thread(target=file_writer, name='fw')

thread_main.start()
thread_console.start()
thread_file.start()
