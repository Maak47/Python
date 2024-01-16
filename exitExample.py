import sys

while True:

    response = input("Type exit to exit: ")
    if response == "exit" or "Exit" or "EXIT":
        sys.exit()
    print("You Typed" + response + ".")
