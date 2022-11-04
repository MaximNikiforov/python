# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def to_binary(num):
    s = ""
    while num != 0:
        s = str(num % 2) + s
        num //= 2
    return s


print(to_binary(int(input("Введите число: \n"))))
