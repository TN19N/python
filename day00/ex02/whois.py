from sys import argv

if __name__ == '__main__' :
    if len(argv) == 1 :
        print("Usage: python whois.py [number]")
    elif len(argv) > 2 :
        print("AssertionError: more than one argument are provided")
    else :
        try:
            print(f"I'm {'Zero' if int(argv[1]) == 0 else 'Odd' if int(argv[1]) % 2 == 1 else 'Even'}.")
        except:
            print("AssertionError: argument is not an integer")