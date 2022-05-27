# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("5.4.1.txt", 'w+') as file_4_1:
    file_4_1.writelines(['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4\n'])
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("5.4.1.txt") as file_4_1:
    with open("5.4.2.txt", 'w') as file_4_2:
        while True:
            a = file_4_1.readline().split()
            if not a:
                break
            else:
                a[0] = translate[a[0]]
                file_4_2.write(f'{" ".join(a)}\n')
