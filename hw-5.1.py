# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

def t_func():
    while True:
        text = input('Введите текст: ')
        if text == '':
            break
        else:
            print(text, file=file_1)


try:
    with open("5.1.txt", 'w') as file_1:
        t_func()
except FileExistsError:
    with open("5.1.txt", 'x') as file_1:
        t_func()
