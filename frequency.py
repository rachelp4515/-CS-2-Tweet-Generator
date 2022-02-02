import random
from distutils.command.clean import clean
from pprint import pprint


def histogram(source_text):
    with open(source_text, 'r') as f:
        source = f.read().lower()
        split_source = source.split()
        hist = {}
        for word in split_source:
            clean_word = word.strip("""'",..:-—“?!();""")
            if clean_word in hist:

                hist[clean_word] += 1
            else:
                hist[clean_word] = 1
        return hist

def unique_words(histogram):
   return len(histogram.keys())

def frequency(word, histogram):
    return histogram[word]

hist = histogram("fish.txt")
# pprint(hist)
# print(f' Unique Words: {unique_words(hist)}')
# print(f' Your word appears {frequency("alice", hist)} times.')

def random_word(hist):
    return random.choice(list(hist.keys()))

# print(random_word(hist))


    

def weight(hist):
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
    





pprint(weight(hist)) 

test_db = {}
for i in range(10000):
    word = weight(hist)
    if word in test_db:
        test_db[word] += 1
    else:
        test_db[word] = 1
pprint(test_db)


