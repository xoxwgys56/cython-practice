from __future__ import print_function

def fib(n):
    """print the fib series up to `n`"""
    a, b = 0, 1
    while b <  n:
        print(b, end=' ')
        a, b = b, a + b

    print()