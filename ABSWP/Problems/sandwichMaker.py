#! python3

#sandwichMaker.py - program to ask users for their sandwich preferences using pyinputplus library

import pyinputplus as pyip

breadPrompt = 'What type of Bread you want?\n'
filetPrompt = 'What type of patty/filet you want?\n'
cheesePrompt = 'Do you want cheese?\n'
cheeseTypePrompt = 'What cheese do you want?\n'
mayoPrompt = 'Do you want mayo?\n'
mustardPrompt = 'Do you want mustard?\n'
lettucePrompt = 'Do you want lettuce?\n'
tomatoPrompt = 'Do you want tomato?\n'
numOfsandwichPrompt = 'How many sandwiches do you want?\n'

breadPrices = {'wheat': 20, 'white': 15, 'sourdough': 30,}
filetPrices = {'chicken': 50, 'turkey': 55, 'beef': 40, 'tofu': 30,}
cheesePrices = {'cheddar': 25, 'swiss': 30, 'mozzarella': 28,}
condiments = {'mayo': 10, 'mustard': 5}
vegetables = {'lettuce': 5, 'tomato': 10}

while True:
    bread = pyip.inputMenu(prompt=breadPrompt, choices=['wheat', 'white', 'sourdough'])
    filet = pyip.inputMenu(prompt=filetPrompt, choices=['chicken', 'turkey', 'beef', 'tofu'])
    cheese = pyip.inputYesNo(cheesePrompt)
    if cheese == 'yes':
        cheeseType = pyip.inputMenu(prompt=cheeseTypePrompt, choices=['cheddar', 'swiss', 'mozzarella'])
    mayo = pyip.inputYesNo(mayoPrompt)
    mustard = pyip.inputYesNo(mustardPrompt)
    lettuce = pyip.inputYesNo(lettucePrompt)
    tomato = pyip.inputYesNo(tomatoPrompt)
    numOfsandwich = pyip.inputInt(numOfsandwichPrompt, min=1)

    totalCost = breadPrices[bread] + filetPrices[filet]
    if cheese == 'yes':
        totalCost += cheesePrices[cheeseType]
    if mayo == 'yes':
        totalCost += condiments['mayo']
    if mustard == 'yes':
        totalCost += condiments['mustard']
    if lettuce == 'yes':
        totalCost += vegetables['lettuce']
    if tomato == 'yes':
        totalCost += vegetables['tomato']
    totalCost *= numOfsandwich

    print('Your Total is: ₹%s' %totalCost)
    if pyip.inputYesNo('Order Again?\n') == 'no':
        break
    totalCost = 0

print('Have an Appetizing meal.')
    
