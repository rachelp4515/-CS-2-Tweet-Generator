import random

num = random.randint(5,10)
words = []

with open('/usr/share/dict/words') as f:
    for line in f:
        words.append(line.strip())
        sentence = random.choices(words, k=num)

print(" ".join(sentence))