import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type one of the r, p, s or q only.")

    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    if playerMove == computerMove:
        print("It is a tie.")
        ties = ties + 1
    elif (
        (playerMove == "r" and computerMove == "s")
        or (playerMove == "s" and computerMove == "p")
        or (playerMove == "p" and computerMove == "r")
    ):
        print("You Win!!!")
        wins = wins + 1
    elif (
        (playerMove == "r" and computerMove == "p")
        or (playerMove == "s" and computerMove == "r")
        or (playerMove == "p" and computerMove == "s")
    ):
        print("You Lose!!!")
        losses = losses + 1
