import random
import sys

def shuffle(input):
    random.shuffle(input)
    output = " ".join(input)
    print(output)

def getInput():
    input = sys.argv
    return input[1:]


shuffle(getInput())

