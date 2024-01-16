def collatz(number):
    if number % 2 == 0:
        number = number // 2 
    elif number % 2 == 1:
        number = 3 * number + 1
    return number    

try:
    number = int(input('Enter a number: \n'))
    while True:
        number = collatz(number)
        if number != 1:
            print(number)
        else:
            print(number)
            break
except ValueError:
    print('---x Enter a positive integer x---')
    