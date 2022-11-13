import sys

if len(sys.argv) == 1 :
    print("Usage: python whois.py [number]")
elif len(sys.argv) > 2 :
    print("AssertionError: more than one argument are provided")
else :
    if len(sys.argv[1]) != 0 and sys.argv[1][0] == '-': 
        sys.argv[1] = sys.argv[1][1:]
    if sys.argv[1].isdigit() == True :
        if int(sys.argv[1]) % 2 == 0 :
            print("I'm Even.")
        else :
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")