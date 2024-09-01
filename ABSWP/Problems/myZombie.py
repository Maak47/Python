#! python3 

#myZombie.py

import zombiedice
import random

# class StopsAfterTwoBrains:
#     def __init__(self, name):
#         # All zombies must have a name
#         self.name = name

#     def turn(self, gameState):
#         #Gamestate is a dict with info about the state of the game.
#         #You can choose to ignore   it in your code.
#         diceRollResults = zombiedice.roll() #first roll
#         # roll() returns a dictionary with keys 'brains', 'shotgun', and
#         # 'footsteps' with how many rolls of each type there were.
#         # The 'rolls' key is a list of (color, icon) tuples with the
#         # exact roll result information.
#         # Example of a roll() return value:
#         # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
#         # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
#         # ('green', 'shotgun')]}
    
#         # Replace THIS ZOMBIE CODE WITH YOUR OWN:
#         brains = 0
#         while diceRollResults is not None:
#             brains += diceRollResults['brains']

#             if brains > 2:
#                 break
#             else: 
#                 diceRollResults = zombiedice.roll()


# •	 A bot that initially decides it’ll roll the dice one to four times, but will
# stop early if it rolls two shotguns
class ConfusedAndScared:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        for rolls in range(random.randint(0, 4)):
            diceResults = zombiedice.roll()
            shotgun = 0
            if diceResults is not None:
                shotgun += diceResults['shotgun']
                if shotgun == 2:
                    break
                else:
                    continue

# •	 A bot that stops rolling after it has rolled more shotguns than brains
class CalculatedZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        diceResults = zombiedice.roll()
        brains = 0
        shotgun = 0
        while shotgun < brains:
            diceResults = zombiedice.roll()
            brains += diceResults['brains']
            shotgun += diceResults['shotgun']
        pass

class AggressiveZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        while brains < 13:  # aim for 13 brains
            diceResults = zombiedice.roll()
            brains += diceResults['brains']
            if diceResults['shotgun'] > 0:  # if we get a shotgun, stop
                break
#•	 A bot that, after the first roll, randomly decides if it will continue
# or stop
class RandomBot:
    def __init__(self,name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        if random.randint(0, 1) == 0:
            zombiedice.roll()
        else: 
            pass
        
# •	 A bot that stops rolling after it has rolled two brains
class StopAfterTwoBrains:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceResults = zombiedice.roll()
        brains = 0
        while diceResults is not None:
            brains += diceResults['brains']
            if brains > 2:
                break
            else:
                diceResults = zombiedice.roll()

# •	 A bot that stops rolling after it has rolled two shotguns
class AfterTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()
                continue
zombies = (
#  zombiedice.examples.RandomCoinFlipZombie(name='Random'),
#  zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
#  zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
#  zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
ConfusedAndScared(name='ConfusedAndScared'),
StopAfterTwoBrains(name='TwoBrains'),
RandomBot(name='RandomBot'),
AfterTwoShotguns(name='AfterTwoShotguns'),
AggressiveZombie(name='AggressiveZombie'),

CalculatedZombie(name='CalculatedZombie'),
 # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
        