from sys import argv

if __name__ == '__main__' :
    if len(argv) == 1 :
        print("Usage: python exec.py [ARG 1] [ARG2] ... ")
        exit(1)
    print(f"{' '.join(argv[1:])[::-1].swapcase()}")