#! python3
# Created by: MiniSpaceHamster
''' 
pigLatin.py - Receives a user input message and returns a sting converted to 
pig latin. If the word begins with a consonant or group of consonants, the 
consonants are moved to the end of the word followed by 'ay'. If the word begins 
with a vowel, 'yay' is added to the word.
'''
import pyperclip

def convertMessage(message):
    '''
    convertMessage(message) - Receives a string and returns a string converted
    to pig latin using pigLatin(word). The case and puntuation of the original 
    message are preserved.
    '''
    messageSplit = []
    newMessage = ''
    word = ''
    
    # Split the message into words keeping the puctuation in place.
    for char in message:
        # Construct word from sequential alphanumaric characters.
        if char.isalnum():
            word += str(char) 
        # Spaces or punctuation adds word to messageSplit and resets word.
        else:
            if len(word) > 0:
                messageSplit.append(word)
                word = ''
            messageSplit.append(str(char))
    # Catch single word messages without punctuation.
    if len(word) > 0:
        messageSplit.append(word)
    # Test to ensure only words are passed to pigLatin() coverter.
    for item in messageSplit:
        if item.isalpha():
            newMessage += pigLatin(item)
        else:
            newMessage += item
    return newMessage

def pigLatin(word):
    '''
    pigLatin(word) - Receives a string returns a word converted to pig latin. 
    If the word begins with a vowel, 'yay' is added to the end of the word; 
    otherwise, consonants are moved to the end of the word and 'ay' is added 
    to the end. The original case of the word is preserved; however, single 
    vowel words are not treated as all caps e.g. 'I' will be 'Iyay'.
    '''
    word = word
    # Check the case of the word prior to manipulating the string.
    allCaps = word.isupper()
    titleCase = word.istitle()
    
    VOWELS = 'aeiouAEIOU'
    VOWELSY = VOWELS + 'yY'   
    
    # If the word starts with a vowel, add 'yay' or 'YAY' depending on case.
    if word[0] in VOWELS:
        if allCaps and len(word) > 1:
            word += 'YAY'
            return word
        else:
            word += 'yay'
            return word
    # Move consonants to the end of the word and stop at the first vowel or y. 
    for char in word:
        if word[0] not in VOWELSY:
            if allCaps:
                word += word[0]
            else:
                word += word[0].lower()
            word = word[1:]
        else:
            break
    # If the word starts with a consonant, add 'ay' or 'AY' depending on case.         
    if allCaps:
        word += 'AY'
    elif titleCase:
        word += 'ay'
        word = word.title()
    else:
        word += 'ay'
    return word

def unConvertMessage(message):
    pass

def unPigLatin(word):
    pass

if __name__ == '__main__':
    
    message = input(
        'Please enter your message or press enter to paste from clipboard: '
        )
    if len(message) < 1:
        message = pyperclip.paste()
        pyperclip.copy(convertMessage(message))
    print(convertMessage(message))
            
            
            
            
            
            
            
    