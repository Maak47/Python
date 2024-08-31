#! python3

#bulletPointAdder.py - Adds Wikipedia bullet points to the start 
#start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()


# TODO: Seperate lines and adds stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the lines list
    lines[i] = '* ' + lines[i] #adds star and space to each string in lines list

text = '\n'.join(lines) #joins the lines list strings to a single string 

pyperclip.copy(text)
