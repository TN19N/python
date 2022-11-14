from string import punctuation
from sys import argv

if __name__ == '__main__' :
    if len(argv) != 3 or not argv[2].isdigit() :
        print ('ERROR')
        exit(1)

    words = [''.join([c for c in word if not c in punctuation]) for word in argv[1].split(' ')]
    minLen = int(argv[2])

    print ([word for word in words if len(word) > minLen])