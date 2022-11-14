from sys import argv

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

if __name__ == '__main__' :
    if len(argv) == 1:
        print('ERROR')
        exit(1)

    allstring = ' '.join(arg for arg in argv[1:])

    if not all(c.isalnum() or c.isspace() for c in allstring) :
        print('ERROR')
        exit(1)

    print(' '.join(MORSE_CODE_DICT[c.upper()] for c in allstring))