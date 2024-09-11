#! python3

#madLibs.py - reads text files and lets the user add their own text anywhere the word
#             ADJECTIVE, NOUN, ADVERB and VERB appears in the text file and saves the
#             result in a text file

madLibsTextFile = open('./Problems/preMadLibs.txt')
madLibsText = madLibsTextFile.read()
madLibsTextFile.close()





if 'ADJECTIVE' in madLibsText:
   adjectiveInput = str(input('Enter an adjective:\n'))
   madLibsText = madLibsText.replace('ADJECTIVE', adjectiveInput)
    
if 'NOUN' in madLibsText:
    nounInput = str(input('Enter a noun:\n'))
    madLibsText = madLibsText.replace('NOUN', nounInput)
    
if 'ADVERB' in madLibsText:
    adverbInput = str(input('Enter an adverb:\n'))
    madLibsText = madLibsText.replace('ADVERB', adverbInput)
    
if 'VERB' in madLibsText:
    verbInput = str(input('Enter a verb:\n'))
    madLibsText = madLibsText.replace('VERB', verbInput)    

print('MadLibs now:\n' + madLibsText + '\nSaving the file "postMadlibs.txt".')
postScriptFile = open('./Problems/postMadlibs.txt', 'w')
postScriptFile.write(madLibsText)
postScriptFile.close()