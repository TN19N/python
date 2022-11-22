from random import randint

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''

    if type(text) != str \
        or type(sep) != str \
        or not option in [None, 'shuffle', 'unique', 'ordered'] \
        or not text.isprintable() :
        yield 'ERROR'
        return

    words = text.split(sep)

    if option == 'shuffle':
        new = []
        while len(words) != 0:
            r = randint(0, len(words) - 1)
            new.append(words[r])
            del words[r]
        words = new
    elif option == 'unique':
        words = list(set(words))
    elif option == 'ordered':
        words.sort()

    for word in words :
        yield word