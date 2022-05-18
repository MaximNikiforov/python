# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

my_list = list(map(int, input('Введите список чисел через пробел: ').split()))
new_list = [el for (index, el) in enumerate(my_list) if my_list.index(el) > 0 and el > my_list[index-1]]
print(my_list)
print(new_list)
