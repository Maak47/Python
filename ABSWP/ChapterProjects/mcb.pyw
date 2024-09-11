#! python3

#multiClipBoard updatable.pyw - Saves and loads pieces of text to the clipboard.
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.
        #PRACTICE PROJECT
#       py.exe mcb.pyw delete <keyword> - deletes the keyword from the shelf 
#       py.exe mcb.pyw delete - deletes all the keywords from the shelf

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    
    #TODO: Delete keyword from the shelf <Practice Project>
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    #TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    #TODO: Delete all keywords <Practice Project>
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])    

mcbShelf.close()



