#! python3

#insertGaps.py - insert gaps into numbered files so that a new file can be added.

import os, shutil, re
from pathlib import Path

def insertGaps(directory, position=2, ):
    files = os.listdir(Path(directory))
    numList, prefix, suffix = numRegex(files)


    if position < 1 or position > len(numList) + 1:
        print(f'Invalid position: Position should be between 1 and {len(numList) + 1}')
        return

    tempDir = Path(directory)  /'tempDirectory'
    os.mkdir(tempDir)

    maxDigits = len(str(len(numList) + 1))
    
    for idx, val in enumerate(numList):
        newNum = int(val) + 1 if idx >= position - 1 else int(val) 
        print(f'{files[idx]} is converted into {prefix}{str(newNum).zfill(maxDigits)}{suffix}')
        shutil.move(Path(directory) / files[idx], tempDir / f'{prefix}{str(newNum).zfill(maxDigits)}{suffix}')
    
    for file in os.listdir(tempDir):
        shutil.move(tempDir / file, Path(directory))

    os.rmdir(tempDir)
def numRegex(list):
    numRegex = re.compile(r'^([a-zA-z]+)(\d+)(\.\w+)?')
    numList = []

    for file in list:
        match = numRegex.search(file)
        if match:
            numList.append(match.group(2))
    prefix = numRegex.search(list[0]).group(1)
    suffix = numRegex.search(list[0]).group(3) 

    return numList, prefix, suffix

    
#Test
if __name__ == '__main__':
    insertGaps('C:\\Users\\maak\\spam')


