# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def Fibonacci(num):
    fib_list = [0, 1]
    i = 2
    negafib_list = [1, 0]
    while i <= num:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        negafib_list.insert(0, negafib_list[-i+1] - negafib_list[-i])
        i += 1
    negafib_list.pop(-1)
    return negafib_list + fib_list


print(Fibonacci(int(input("Введите число: \n"))))
