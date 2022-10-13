# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def checkStatement():
    result = 'Утверждение истинно'
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not (x or y or z)) != (not x and not y and not z):
                    result = 'Утверждение ложно'
                    return print(result)
    return print(result)


checkStatement()
