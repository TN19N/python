import sys

str = ""

for i in range(1, len(sys.argv)):
    if i != 1:
        str += " "
    str += sys.argv[i]

if len(sys.argv) == 1 :
    print("Usage: python exec.py [ARG 1] [ARG2] ... ")
else :
    print(f"{str[::-1].swapcase()}")