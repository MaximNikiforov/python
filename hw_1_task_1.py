# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial


n_1 = factorial(52) / (factorial(4)*factorial(52 - 4))
m_1 = factorial(13) / (factorial(4)*factorial(13 - 4))
print(f'Вероятность того, что все карты - крести = {m_1/n_1 :.4f}')

n_2 = factorial(52) / (factorial(4)*factorial(52 - 4))
m_2 = factorial(48) / (factorial(4)*factorial(48 - 4))
print(f'Вероятность, что среди 4-х карт окажется хотя бы один туз = {1 - m_2/n_2 :.4f}')
