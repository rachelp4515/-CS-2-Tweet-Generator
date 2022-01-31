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

hist = histogram("alice.txt")
# pprint(hist)
# print(f' Unique Words: {unique_words(hist)}')
# print(f' Your word appears {frequency("alice", hist)} times.')

def random_word(hist):
    return random.choice(list(hist.keys()))

# print(random_word(hist))


    

def weight(hist):
    return random.choices(list(hist.keys()), weights=list(hist.values()))[0]
    # pairs = enumerate(hist) 
    # keys = [i[0] for i in pairs] 
    # values = [i[1] for i in pairs]  
    # return random.choices(keys, values)[0] 
 
pprint(weight(hist))

# test_db = {}
# for i in range(300):
#     word = weight(hist)
#     if word in test_db:
#         test_db[word] += 1
#     else:
#         test_db[word] = 1
# pprint(test_db)


