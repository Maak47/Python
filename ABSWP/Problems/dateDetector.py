#! python3

#dateDetector - detects dates from DD/MM/YYYY format.

import re 


def dateFunc(str):
    #TODO: Regex for date
    dateRegex = re.compile(r'''
    (\d?\d)          #day
    /   
    (\d?\d)          #month
    /
    (\d\d\d\d)      #year                      
                           ''', re.VERBOSE)

    #TODO: Save the date in day, month, year variables
    day, month, year = dateRegex.search(str).groups()


    #TODO: Validate the date
    if  not 1 <= int(month) <= 12:
        return False

    if int(month) in [4, 6, 9, 11]:
        if not 1 <= int(day) <= 30:
            return False
    if int(month) == 2:
        if not 1 <= int(day) <= 29:
            return False
        if int(day) == 29 and (int(year) % 4 != 0 or (int(year) % 100 == 0 and int(year) % 400 != 0)):
            return False
    else:
        if not 1 <= int(day) <= 31:
            return False
    
    if not 1000 <= int(year) <= 2999:
        return False

    return True

print(dateFunc('80/12/4002'))



