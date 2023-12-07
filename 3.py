# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


import decimal
import time


CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0


def log(text):
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time_string}: {text}\n')
        print(text)


def richness():
    global account
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        log(f'Удержан налог на богатство {RICHNESS_TAX * 100}% в сумме {percent} рублей')


def bonus():
    global count
    global account
    count += 1
    if count and count % COUNT_OPER == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        log(f'Начислено {bonus_percent} за {COUNT_OPER}-ю операцию')


def deposit():
    global account
    amount = 1
    while amount % MULTIPLICITY != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    account += amount
    log(f'Пополнение карты на {amount} рублей')
    bonus()
    richness()
    print(f'Баланс: {account} рублей')


def withdraw():
    global account
    amount = 1
    while amount % MULTIPLICITY != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                    MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
    if account >= withdraw_tax + amount:
        account -= (amount + withdraw_tax)
        log(f'Снятие с карты {amount} рублей. Комиссия {withdraw_tax} рублей')
        bonus()
        richness()
        print(f'Баланс: {account} рублей')
    else:
        print(f'Недостаточно денег для выполнения операции \nБаланс: {account} рублей')


def start():
    while True:
        command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
        if command == CMD_EXIT:
            print(f'Возьмите карту. Баланс: {account} рублей')
            break
        elif command == CMD_DEPOSIT:
            deposit()
        elif command == CMD_WITHDRAW:
            withdraw()


start()
