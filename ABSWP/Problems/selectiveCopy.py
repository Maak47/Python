#! python3

#selectiveCopy.py - Copy certain files with extensions like .pdf, jpg from a foldertree to a new folder.
#Usage: python selectiveCopy.py <source_folder> <destination_folder>
    #ex: python selectiveCopy.py C:\Users\maak\Downloads C://Users//maak//Desktop
import os, shutil, re, sys
from pathlib import Path




def selectiveCopy(srcFolder, desFolder):
    source = Path(srcFolder)
    destination = Path(desFolder)
    destinationFolders = {
        'image': destination / 'imageCopyToFolder',
        'text': destination / 'textCopyToFolder',
        'pdf': destination / 'pdfCopyToFolder',
    }

    for folder in destinationFolders.values():
        folder.mkdir(parents=True, exist_ok=True)
    extensionRegex = re.compile(r'^(.*)\.(pdf|jpg|jpeg|png|txt)$', re.IGNORECASE)

    #TODO: go through a folder.
    for folderName, _, filenames in os.walk(source):
        for filename in filenames:
            file = extensionRegex.search(filename)
            if  file is not None:
            #TODO: copy files and save it to a new folder.
                if file.group(2) in ['jpg', 'jpeg', 'png']:
                    print(f'{filename} is getting copied to {destinationFolders["image"]}')
                    shutil.copy(Path(folderName) / filename, destinationFolders['image'])
                elif file.group(2) == 'txt':
                    print(f'{filename} is getting copied to {destinationFolders["text"]}')
                    shutil.copy(Path(folderName) / filename, destinationFolders['text'])
                elif file.group(2) == 'pdf':
                    print(f'{filename} is getting copied to {destinationFolders["pdf"]}')
                    shutil.copy(Path(folderName) / filename, destinationFolders['pdf'])
                else:
                    print('No files of interests found..')
                    break

if len(sys.argv) != 3:
    print('Usage: python selectiveCopy.py <source_folder> <destination_folder>')
    sys.exit(1)

srcFolder = sys.argv[1]

desFolder = sys.argv[2]

selectiveCopy(srcFolder, desFolder)