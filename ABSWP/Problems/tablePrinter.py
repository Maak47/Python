tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
 ]


#mine
def printTable(tableList):
    colWidths = []

    for data in tableList:
        maxWidth = len(max(data, key=len)) 
        colWidths.append(maxWidth)
    for y in range(len(tableList[0])):
        for x in range(len(tableList)):
            print(tableList[x][y].rjust(colWidths[x]), end= ' ')
        print()
        
#Internet
# def printTable(tableList):
#     colWidths = [0] * len(tableList)

#     for xdata in range(len(tableList)):
#         for ydata in range(len(tableList[0])):
#             if len(tableList[xdata][ydata]) > colWidths[xdata]:
#                 colWidths[xdata] = len(tableList[xdata][ydata])
#     for ydata in range(len(tableList[0])):
#         for xdata in range(len(tableList)):
#             print(tableList[xdata][ydata].rjust(colWidths[xdata]), end = ' ')
#         print()

printTable(tableData)

