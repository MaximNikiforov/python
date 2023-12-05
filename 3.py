import string

with open('example.txt', 'r', encoding='UTF-8') as file:
    data = file.read()

for char in string.punctuation:
    data = data.lower().replace(char, ' ')

counter_dict = {}

for word in data.split():
    counter_dict[word] = counter_dict.get(word, 0) + 1

counter_dict = tuple(sorted(counter_dict.items(), key=lambda item: item[1]))
for index, word in enumerate(counter_dict[-1:-10:-1], 1):
    print(f'{index}. {word[0]:>10} - {word[1]} раз')
