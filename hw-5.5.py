# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("5.5.txt", 'w+') as file_5:
    print('7 5 1 -4 2 1.4 6 9 7 2.2', file=file_5)
    file_5.seek(0)
    print(f'Сумма = {sum([float(i) for i in file_5.readline().split()]):g}')
