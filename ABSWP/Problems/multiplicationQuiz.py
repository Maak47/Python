#! python3

#multiplicationQuiz.py - without pyinputplus This program will
    # prompt the user with 10 multiplication questions, ranging from 0 × 0 to
    # 9 × 9. You’ll need to implement the following features:
    # •	 If the user enters the correct answer, the program displays “Correct!”
    # for 1 second and moves on to the next question.
    # •	 The user gets three tries to enter the correct answer before the
    # program moves on to the next question.
    # •	 Eight seconds after first displaying the question, the question is
    # marked as incorrect even if the user enters the correct answer after
    # the 8-second limit.

import random, time 

numberOfQuestions = 10
correctAnswer = 0

for question in range(numberOfQuestions):
    a = random.randint(0, 9)
    b = random.randint(0, 9)

    result = int(input('#%s: %s x %s = ' %(question, a, b)))
    tries = 1
    while tries < 3:
        timeStamp = time.time()
        if time.time() - timeStamp > 8:
            print('Out of Time!')
        elif result == a * b:
            print('Correct')
            correctAnswer += 1            
            break
        else:
            print('Incorrect!')
            result = input()
            tries += 1
            if tries == 3:
                print('Out of Tries!')
                tries = 0
            continue
print('Score: %s / %s' % (correctAnswer, numberOfQuestions))


        
    
         

    



