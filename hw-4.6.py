# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle

my_list = []


def first_func(a):
    n = 0
    global my_list
    for el in count(a):
        if n == 10:
            break
        else:
            n += 1
            my_list.append(el)
    print(my_list)


def second_func():
    global my_list
    n = 0
    for el in cycle(my_list):
        if n == len(my_list):
            break
        else:
            print(f'{n+1}-й элемент списка: {el}')
            n += 1


first_func(155)
second_func()
