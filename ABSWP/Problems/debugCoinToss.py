#! python3

#debugCoinToss.py - a simple cointoss program focused debugging using raises and logging

import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of the loop')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('Start of the coin toss')
toss = random.randint(0,1) #0 is tails, 1 is heads
if guess == 'heads':
    guess = 1

logging.debug('Does ' + str(guess) + ' equals ' + str(toss) + '?')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess == 'heads':
        
        guess = 1
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('End of the program')
