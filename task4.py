# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


from random import randint


def degree(digit, deg: int):
    indexes = {"0": "\u2070",
               "1": "\u00B9",
               "2": "\u00B2",
               "3": "\u00B3",
               "4": "\u2074",
               "5": "\u2075",
               "6": "\u2076",
               "7": "\u2077",
               "8": "\u2078",
               "9": "\u2079",
               "-": "\u207B"
               }
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char] or ""
    return digit + degrees


def random_polinominal(k, file):
    rand_coef = [randint(0, 100) for _ in range(k + 1)]
    polinominal = []
    while k >= 0:
        if rand_coef[- k - 1] != 0:
            if k > 1:
                x = str(rand_coef[- k - 1]) + 'x'
                polinominal.append(degree(x, int(k)))
            elif k == 1:
                polinominal.append(str(rand_coef[- k - 1]) + 'x')
            else:
                polinominal.append(str(rand_coef[-1]))
            k -= 1
        else:
            k -= 1
    with open(file, 'w', encoding='utf-8') as data:
        for el in polinominal[:-1]:
            data.write(el + ' + ')
        data.write(polinominal[-1] + ' = 0')
    return print(f'Многочлен в файл {file} записан')


#random_polinominal(int(input("Введите степень k: ")), 'task4.txt')            # чтобы не мешал 5 задаче
