import os
from pathlib import Path

os.chdir(Path('C:/Users/maak/spam'))
listOfFiles = os.listdir()

#remove the dummy files
for file in listOfFiles:
    os.unlink(file)

#create the dummy files
for i in  range(100):
    if i + 1 < 10:
        newFile = open((f'spam00{i+1}.txt'), 'w')
    else:
        newFile = open((f'spam0{i+1}.txt'), 'w')
    newFile.write(f'This is dummy spam{i+1}.')
    newFile.close
