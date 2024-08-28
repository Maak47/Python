# CoinflipStreak(string based)
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    #Code that creates a list of 100 'heads' or tails' values.
    dataset = []
    for data in range(100):
        if random.randint(0, 1) == 0:
            dataset.append('H')
        else:
            dataset.append('T')
    # print(dataset)
    datasetString = ''
    for data in dataset:
        datasetString += data
    # print(datasetString) 
    #Code that checks if there is a streak of 6 'heads' or tails in a row.
    if 'HHHHHH' in datasetString:
        numberOfStreaks += 1
    elif 'TTTTTT' in datasetString:
        numberOfStreaks += 1
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
