
# What is the least/most frequent word(s)?
# How many different words are used?
# What is the average (mean/median/mode) frequency of words in the text?



from distutils.command.clean import clean
from pprint import pprint


def histogram(source_text):
    with open(source_text, 'r') as f:
        source = f.read().lower()
        split_source = source.split()
        hist = {}
        for word in split_source:
            clean_word = word.strip("""'",..:-——_‘’“?!();""")
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
pprint(hist)
print(unique_words(hist))
print(frequency("fish", hist))
