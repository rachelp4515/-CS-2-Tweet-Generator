import random
from dict_words import dictogram
from pprint import pprint

hist = dictogram("fish.txt")

def random_word(hist):
    return random.choice(list(hist.keys()))

# print(random_word(hist))



def sample(hist):
    words = list(hist.keys())
    weights = []
    total = 0
    for word in words:
        weights.append(hist[word] + total)
        total += hist[word]
    num = random.randint(1, total)
    weight_index = 0
    while num > weights[weight_index]:
        weight_index += 1
    return words[weight_index]
    





pprint(sample(hist)) 

test_db = {}
for i in range(10000):
    word = sample(hist)
    if word in test_db:
        test_db[word] += 1
    else:
        test_db[word] = 1
pprint(test_db)


