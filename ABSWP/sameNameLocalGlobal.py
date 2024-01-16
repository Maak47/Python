def spam():
    global eggs
    eggs = 'spam'


def bacon():
    eggs = 'bacons'
    print('%s, its a local variable' % eggs)


def ham():
    print(eggs)


eggs = '42'
spam()
bacon()
print(eggs)
