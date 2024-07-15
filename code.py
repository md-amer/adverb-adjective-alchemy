from random import choice
from time import sleep

with open('adverbs.txt') as f:
    adverbs = f.read().splitlines()

with open('adjectives.txt') as f:
    adjectives = f.read().splitlines()
    
while True:
    print(choice(adverbs)+' '+choice(adjectives))
    sleep(0.5)
