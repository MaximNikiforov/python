from pprint import pprint

name_employee = ('Кирилл Панфилов', 'Андрей Беляев', 'Виталий Кузьмин')
salary = (100000, 150000, 5000)
bonus = ('2.5%', '1.5%', '5%')

bonus = {name_employee[i]: salary[i] + salary[i] * (float(bonus[i][:-1]) / 100) for i in range(len(name_employee))}

pprint(bonus)
