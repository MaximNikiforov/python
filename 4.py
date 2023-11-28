import random

n = random.randint(0, 1000)
a = 1
while True:
    text = int(input("Угадайте число от 0 до 1000: "))
    if a >= 10:
        print("Вы проиграли! Загадано было", n)
        break
    elif text == n:
        print("Победа")
        break
    elif text > n:
        a += 1
        print(f'Число меньше вашего! Осталось {11 - a} попыток')
    elif text < n:
        a += 1
        print(f'Число больше вашего! Осталось {11 - a} попыток')
