def fibonacci(limit: int):
    fibo = [0, 1]
    while limit > 0:
        yield fibo[-1]
        fibo.append(fibo[-1] + fibo[-2])
        limit -= 1


for number in fibonacci(10):
    print(number)
    