#! python3

#stripRegex.py - regular expressions implementation of strip()

# If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the 
# beginning and end of the string. Otherwise, the characters 
# specified in the second argument to the function will be 
# removed from the string

import re

#TODO: function for strip
def stripRegex(string, arg=None):
    if arg is None:
        stripRegex = re.compile(r'^\s+|\s+$')
        return stripRegex.sub('', string)
    else:
        stripRegex = re.compile(rf'^{re.escape(arg)}+|{re.escape(arg)}+$')
        return stripRegex.sub('', string)


print(stripRegex('???WHAT??THEFUCK???', '?'))