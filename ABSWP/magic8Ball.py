import random


def getAnswers(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidingly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply Hazy try again"
    elif answerNumber == 5:
        return "Ask again"
    elif answerNumber == 6:
        return "Concentrate and try again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"


print(getAnswers(random.randint(1, 9)))
