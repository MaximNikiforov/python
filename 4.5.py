# 5) На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
# от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

import numpy as np

print(f'На {(190 - 178) / np.sqrt(25):g} сигм')
