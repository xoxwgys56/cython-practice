import pyximport; pyximport.install()
# import helloworld
import fib as cython_fib
import primes as cython_primes


if __name__ == '__main__':
    # cython_fib.fib(2000)
    for prime in cython_primes.primes(10):
        print(prime)