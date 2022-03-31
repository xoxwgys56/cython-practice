from setuptools import setup
from Cython.Build import cythonize


modules = ["helloworld", "fib", "primes"]

setup(
    ext_modules=cythonize(f"{modules[2]}.pyx")
)