import sys

if __name__ == '__main__' :
    if len(sys.argv) > 3 :
        print('AssertionError: too many arguments')
        exit(1)
    if len(sys.argv) < 3 :
        print('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
        exit(1)
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() :
        print('AssertionError: only integers')
        exit(1)

    A = int(sys.argv[1])
    B = int(sys.argv[2])

    print('Sum:        ', A + B)
    print('Difference: ', A - B)
    print('Product:    ', A * B)
    if B == 0 :
        print('Quotient:    ERROR (division by zero)')
        print('Remainder:   ERROR (modulo by zero)')
    else :
        print('Quotient:   ', A / B)
        print('Remainder:  ', A % B)
