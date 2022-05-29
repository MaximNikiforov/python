# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("5.2.txt", 'w+') as file_2:
    text_list = ['Hello, World!', 'string', 'text text text', '247 words']
    file_2.writelines([text + '\n' for text in text_list])
    file_2.seek(0)

    file_list = file_2.readlines()
    print(f'В файле {len(file_list)} строк.')
    for n, i in enumerate(file_list):
        print(f'В {n+1} строке - {len(i.split())} слов.')
