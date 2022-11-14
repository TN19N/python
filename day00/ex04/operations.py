from sys import argv

if __name__ == '__main__' :
    if len(argv) > 3 :
        print('AssertionError: too many arguments')
        exit(1)
    if len(argv) < 3 :
        print('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
        exit(1)

    A = 0
    B = 0
    try:
        A = int(argv[1])
        B = int(argv[2])
    except:
        print('AssertionError: only integers')
        exit(1)

    print(f'''\
Sum:        {A + B}
Difference: {A - B}
Product:    {A * B} 
Quotient:   {'ERROR (division by zero)' if B == 0 else A / B}
Remainder:  {'ERROR (modulo by zero)' if B == 0 else A % B}\
''')
