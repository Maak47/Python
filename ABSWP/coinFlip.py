#! python3

#coinFlip.py - displays number of heads in 1000 flips

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    if i == 500:
        print('Halfway Done!')
print('Heads came up ' + str(heads) + ' times.')