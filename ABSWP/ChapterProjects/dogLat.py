#English to Dog Latin

print('Enter the English message to translate into dog Latin')

message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

dogLatin = [] # A list of the words in dog Latin

for word in message.split():
    prefixNonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonletters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        dogLatin.append(prefixNonletters)
        continue

    #Seperate the non-letters at the end of this word:
    suffixNonletters = ''
    while not word[-1].isalpha():
        suffixNonletters += word[-1]
        word = word[:-1]

    #Remember if the word was in uppercase of title case.
    wasUpper =  word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower() # Make the word lowercase for translation.

    #Seperate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the dog Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'woo'
    else:
        'uuf'
    
    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    #Add the non-letters back to the start or end of the word.
    dogLatin.append(prefixNonletters + word + suffixNonletters)

# Join all the words back together into a single string:

print(' '.join(dogLatin))


