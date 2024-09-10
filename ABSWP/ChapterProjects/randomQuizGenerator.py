#! python3

#randomQuizGenerator.py - Creates quizzes with questions and answers in
#random order, along with answer keys.

import random

#The quiz data. Keys are states and values are their capitals.
capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttarakhand': 'Dehradun',
    'Uttar Pradesh': 'Lucknow',
    'West Bengal': 'Kolkata',
    'Andaman and Nicobar Islands': 'Port Blair',
    'Chandigarh': 'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
    'Delhi': 'New Delhi',
    'Jammu and Kashmir': 'Srinagar',
    'Ladakh': 'Leh',
    'Lakshadweep': 'Kavaratti',
    'Puducherry': 'Puducherry'
}

#Generate 35 quiz files

for quizNum in range(35):
    #TODO: Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    #TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    #TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    #TODO: Loop through all states, making a question for each.
    for questionNum in range(len(capitals.keys())):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #TODO: write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for choice in range(4):
            quizFile.write(f'   {"ABCD"[choice]}. { answerOptions[choice]}\n')
            quizFile.write('\n')
        
            #TODO: write the answer key to a file.
        answerKeyFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')
    quizFile.close()
    answerKeyFile.close()
