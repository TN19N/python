import sys

if __name__ == '__main__' :
    if len(sys.argv) > 2 :
        print("AssertionError: more than one argument are provided")
        exit(1)
    try:
        print(f"I'm {'Zero' if int(sys.argv[1]) == 0 else ['Even','Odd'][int(sys.argv[1]) % 2]}.")
    except:
        if len(sys.argv) == 1 :     print("Usage: python whois.py [number]")       
        else :                  print("AssertionError: argument is not an integer")
        exit(1)