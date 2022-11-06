# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


from task4 import random_polinominal

random_polinominal(4, 'task5_1.txt')
random_polinominal(3, 'task5_2.txt')


def read_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        a = data.read().split(' ')
        b = []
        dic = {}
    k = 3
    while k <= len(a):
        b.insert(0, a[-k])
        k += 2
    for el in b:
        try:
            dic[''] = int(el)
        except ValueError:
            x = int(el.find('x'))
            dic[el[x:]] = int(el[:x])
    return dic


def sum_file(dic1, dic2, file):
    dic_sum = {}
    for key, value in dic1.items():
        try:
            dic_sum[key] = value + dic2[key]
        except KeyError:
            dic_sum[key] = value
    for key, value in dic2.items():
        try:
            g = dic_sum[key]
        except KeyError:
            dic_sum[key] = value
    with open(file, 'w', encoding='utf-8') as data:
        for key, value in dic_sum.items():
            data.write(str(value) + key + ' + ')
        data.seek(data.tell() - 3)
        data.write(' = 0')
    return print(f'Сумма многочленов в файл {file} записана')


file_1 = read_file('task5_1.txt')
file_2 = read_file('task5_2.txt')
sum_file(file_1, file_2, 'task5_3.txt')
