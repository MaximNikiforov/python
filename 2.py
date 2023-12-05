import random


def only_double(my_list: list) -> list:
    return list(set(filter(lambda x: my_list.count(x) > 1, my_list)))


rand_list = [random.randint(0, 9) for _ in range(15)]
print(rand_list)
print(only_double(rand_list))
