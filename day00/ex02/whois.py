from sys import argv

if __name__ == '__main__' :
    if len(argv) > 2 :
        print("AssertionError: more than one argument are provided")
        exit(1)
    try:
        print(f"I'm {'Zero' if int(argv[1]) == 0 else ['Even','Odd'][int(argv[1]) % 2]}.")
    except:
        if len(argv) == 1 :     print("Usage: python whois.py [number]")       
        else :                  print("AssertionError: argument is not an integer")
        exit(1)