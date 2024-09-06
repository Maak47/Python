#! python3

#idiot.py

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

    ##Spanish version
    # prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    # response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
    # if response == 'sí':
    #     continue
    # if response == 'no':
    #     break
print('Thank You. Have a nice day.')



