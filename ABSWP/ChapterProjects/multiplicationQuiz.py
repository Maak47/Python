#! python3

#multiplicationQuiz.py

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionnumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    prompt = '#%s: %s x %s = ' % (questionnumber, num1, num2)
    try:
        # Right answers are handled by allowRegexes.
        #Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException: 
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        #This block runs if no exceptions were raised in the try block/
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))