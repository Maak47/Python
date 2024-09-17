#! python3

#delUnneededFiles.py - python script that deletes files that are more than a threshold of size.
    #Usage - python delUnneededFiles.py <source_folder> <size in MBs>

import os, sys, send2trash 
from pathlib import Path

def delFunc(source, size_mb):
    sourceFolder = Path(source)
    sizeBytes = size_mb  * (1024 * 1024)
    for folderName, _, filenames in os.walk(sourceFolder):
        for filename in filenames:
            filePath = Path(folderName) / filename
            try:
                fileSize = os.path.getsize(filePath)
                if fileSize > sizeBytes:
                    print(f"{filename} ({fileSize / (1024 * 1024):.2f} MB)")
                    # send2trash.send2trash(str(filePath))
            except OSError as e:
                print(f"Error accessing {filename}: {e}")
                 
if len(sys.argv) != 3:
    print('Usage: python delUnneededFiles.py <source_folder> <size>')
    sys.exit()

delFunc(sys.argv[1], int(sys.argv[2]))