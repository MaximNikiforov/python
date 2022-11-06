# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factor():
    num = int(input("Введите число: "))
    i = 2
    factor_list = []
    a = num
    while i <= a:
        if a % i == 0:
            factor_list.append(i)
            a //= i
            i = 2
        else:
            i += 1
    return f"Простые множители числа {num}: \n{factor_list}"


print(factor())
