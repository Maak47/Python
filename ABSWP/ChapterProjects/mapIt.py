#! python3

#mapIt.py - lauches a map in the browser using address from the commandline or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get the address from the commandLine
    address = '+'.join(sys.argv[1:])
    print(address)


#TODO: Get address from clipboard
else:
    address = '+'.join(pyperclip.paste().split(' '))
    
webbrowser.open('https://www.google.com/maps/place/' + address)
