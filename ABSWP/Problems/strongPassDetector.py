#! python3

#strongPassDetector.py - makes sure that the password is Strong

# 1. Atleast 8 character long
# 2. Contains both uppercase and lowercase
# 3. Has atleast one digit

import re

def strongPass(str):
    if len(str) < 8:
        return False
    if not re.search(r'[a-z]', str):
        return False
    if not re.search(r'[A-Z]', str):
        return False
    if not re.search(r'[0-9]', str):
        return False
    return True

print(strongPass('ThisisSTRONG123'))
print(strongPass('thisisweak'))
print(strongPass('12345678'))
print(strongPass('THISISWEAK'))


