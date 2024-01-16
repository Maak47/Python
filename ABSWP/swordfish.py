while True:
    print('Who are you?')
    name = input()
    if name != 'maak':
        continue
    print('Hello, Maak. What is the password? (Its a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

