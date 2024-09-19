#! python3

#insertGaps.py - insert gaps into numbered files so that a new file can be added.

import os, shutil, re
from pathlib import Path

def insertGaps(directory, position=2):
    path = Path(directory)    
    #TODO: list the directory with with os.listdir()
    listOfFiles = os.listdir(path)

    #TODO: add the numbers from filenames to a list
    numRegex = re.compile(r'^(.*?)(\d*)([0-9])\.(\w+)$', re.IGNORECASE)
    numList = []
    preNum = numRegex.search(listOfFiles[0]).group(2)
    prefix = ''
    suffix = ''
    for file in listOfFiles:
        match = numRegex.search(file)
        if match:
            numList.append(match.group(3))
            if not prefix:
                prefix = match.group(1)
            suffix = match.group(4)
            
    print(numList)
    print(preNum)
    print(f'prefix = {prefix}')
    print(f'suffix = {suffix}')
    print(f'position = {position}')

    #TODO: create a gap in the list
     # Convert position to string for comparison
    position_str = str(position)

    # Check if position exists in numList
    if position_str in numList:
        numList.remove(position_str)
        numList.append(str(max(map(int, numList)) + 1))
    else:
        print(f'No {position} found..')
        return  # Exit the function if position not found

    print(numList)
    
    # #TODO: rename the files to new numList:
    for index, file in enumerate(listOfFiles):
        print(f'Changing {file} to {prefix}{preNum}{numList[index]}.{suffix}')
        # shutil.move(Path(path) / file, Path(path) / f'{prefix}{preNum}{numList[index]}\.{suffix}')

#Test
if __name__ == '__main__':
    insertGaps('C:\\Users\\maak\\spam')


