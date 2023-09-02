#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    res = 0

    match op:
        case '*':
            res = mul(a, b)
        case'-':
            res = sub(a, b)
        case '+':
            res = add(a, b)
        case '/':
            res = div(a, b)
        case _:
            res = None

    if res is None:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        print(f'{a} {op} {b} = {res}')
        exit(0)
