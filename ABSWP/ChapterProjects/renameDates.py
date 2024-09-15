#! python3

# renameDates.py - program that renames filenames with the American Style date(MM/DD/YYYY) to 
#                   European Style date(DD/MM/YYYY).

import os, shutil, re
# Create regex that matches files with American date format.

datePattern = re.compile(r'''^(.*?)      #all text before the date
                        ((0|1)?\d)-     #one or two digits for the month
                        ((0|1|2|3)?\d)- #one or two digits for the day
                        ((19|20)\d\d)   #four digits for the year
                        (.*?)$          #all text after the date
                      ''', re.VERBOSE)

# Loop Over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip file without a date.
    if mo == None:
        continue

    # Get the different parts of  the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart   = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"....')
    #shutil.move(amerFilename,  euroFilename) #uncomment after testing
    