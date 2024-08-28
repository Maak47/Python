#CoinFlipStreak(string based 2)
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    flips = [random.choice(['H', 'T']) for _ in range(100)]
    if 'HHHHHH' in ''.join(flips) or 'TTTTTT' in ''.join(flips):
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# CoinFlipStreak(list based)

# import random

# numberOfStreaks = 0

# for experimentNumber in range(10000):
#     CoinFlip = [random.randint(0,1) for i in range(100)]
    
#     streak = 1
#     for i in range(1, len(CoinFlip)):
#         if CoinFlip[i] == CoinFlip[i - 1]:
#             streak += 1
#         else: 
#             streak = 1
#         if streak == 6:
#             numberOfStreaks += 1
#             break 

# print('Chance of streak: %s%%' % (numberOfStreaks / 100))


# CoinflipStreak(string based 1 )
# import random
# numberOfStreaks = 0
# for experimentNumber in range(10000):
#     #Code that creates a list of 100 'heads' or tails' values.
#     dataset = []
#     for data in range(100):
#         if random.randint(0, 1) == 0:
#             dataset.append('H')
#         else:
#             dataset.append('T')
#     # print(dataset)
#     datasetString = ''
#     for data in dataset:
#         datasetString += data
#     # print(datasetString) 
#     #Code that checks if there is a streak of 6 'heads' or tails in a row.
#     if 'HHHHHH' in datasetString:
#         numberOfStreaks += 1
#     elif 'TTTTTT' in datasetString:
#         numberOfStreaks += 1
        
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))
