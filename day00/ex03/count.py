from string import punctuation
import sys

def text_analyzer(string = None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if string == None :
        try: string = input('What is the text to analyze?\n>> ')
        except: exit(0)
    if type(string) != str :
        print('AssertionError: argument is not a string')
    else:
        print(f'''\
\
The text contains {len(string)} character(s):
- {len([c for c in string if c.isupper()])} upper letter(s)
- {len([c for c in string if c.islower()])} lower letter(s)
- {len([c for c in string if c in punctuation])} punctuation mark(s)
- {len([c for c in string if c.isspace()])} space(s)\
\
''')

if __name__ == '__main__' :
    if len(sys.argv) < 3 :
        text_analyzer(''.join(sys.argv[1:]))
    else :
        print("Usage: python count.py [string](optional)")
        exit(1)