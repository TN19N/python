import sys

if len(sys.argv) == 1 :
    print("Usage: python whois.py [number]")
elif len(sys.argv) > 2 :
    print("AssertionError: more than one argument are provided")
else :
    if sys.argv[0] == '-' or sys.argv[0] == '+' : 
        sys.argv[0] = sys.argv[0][1:]
    if sys.argv[0].isdigit() == True :
        if int(sys.argv[0]) % 2 == 0 :
            print("I'm Even.")
        else :
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")