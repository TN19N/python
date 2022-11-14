import string
import sys

if __name__ == '__main__' :
    if len(sys.argv) != 3 or not sys.argv[2].isdigit() :
        print ('ERROR')
        exit(1)

    words = [''.join([c for c in word if not c in string.punctuation]) for word in sys.argv[1].split(' ')]
    minLen = int(sys.argv[2])

    print ([word for word in words if len(word) > minLen])