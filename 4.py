def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items


capacity = int(input('Введите грузоподъемность рюкзака: '))

equipment = {'Веревка': 1,
                     'Палатка': 8,
                     'Топор': 4,
                     'Нож': 1,
                     'Вода': 5,
                     'Аптечка': 1,
                     'Телефон': 1,
                     'Фонарь': 2,
                     'Лодка': 10,
                     'Удочка': 3}


print(pack_backpack(equipment, capacity))
