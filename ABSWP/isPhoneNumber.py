#! python3

#isPhoneNumber.py

def isUSPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
# print('Is 351-515-4242 a phone number?')
# print(isPhoneNumber('351-515-4242'))
# print('Is Moshi Moshi a phone number?')
# print(isPhoneNumber('Moshi-Moshi'))

def isINCarrierNumber(text):
    if len(text) != 13:
        return False
    if text[0] != '+':
        return False
    if text[1:3] != '91':
        return False
    if not text[1:].isdecimal():
        return False
    return True
message = 'Call me at 415-555-1011 tomorrow. 415-515-9999 is my office.'
messageIn = 'Call me after 9pm on +919174414933, +919993203040 is my office.'
for i in range(len(messageIn)):
    chunk = messageIn[i:i+13]
    if isINCarrierNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')