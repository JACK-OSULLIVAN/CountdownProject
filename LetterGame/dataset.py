from pprint import pprint

with open("words.txt") as file:
    data = file.read()
    print(type(data))

word_list = data.split()

word_dict = {}

for word in word_list:
    word_length = len(word)
    if word_length in word_dict:
        word_dict[word_length].append(word)
    else:
        word_dict[word_length] = [word]

pprint(word_dict)
