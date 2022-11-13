import string
import sys

def text_analyzer(*arg):
    """ This function counts the number of upper characters, lower characters,\n punctuation and spaces in a given text. """
    upperLetters = 0
    lowerLetters = 0
    punctuations = 0
    spaces = 0

    buffer = ""
    if len(arg) == 1 :
        if type(arg[0]) != str :
            print('AssertionError: argument is not a string')
            return
        buffer = arg[0]
    elif len(arg) == 0 :
        print('What is the text to analyze?')
        buffer = input(">> ")
    else:
        print("Usage: text_analyzer([string])")
        return

    for c in buffer :
        if c.isupper() == True :
            upperLetters += 1
        elif c.islower() == True :
            lowerLetters += 1
        elif c.isspace() == True :
            spaces += 1
        elif c in string.punctuation :
            punctuations += 1

    print(f'The text contains {len(buffer)} character(s):')
    print(f'- {upperLetters} upper letter(s)')
    print(f'- {lowerLetters} lower letter(s)')
    print(f'- {punctuations} punctuation mark(s)')
    print(f'- {spaces} space(s)')

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        text_analyzer(sys.argv[1])
    elif len(sys.argv) == 1 :
        text_analyzer()
    else :
        print("Usage: text_analyzer([string])")