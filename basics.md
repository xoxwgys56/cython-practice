---
description: basic usage of `cython`
---

# Basics

> before read this document you can check code [here](https://github.com/xoxwgys56/cython-practice/tree/main/basic)

### Setup

install `cython` in your local. I used python@3.9.10

```shell
# create venv
python3 -m venv venv
source ./venv/bin/activate
pip3 install cython

# create empty files
touch setup.py main.py helloworld.pyx
```

type like below inside of `setup.py`. every time we build `cython` script, we use this.

{% code title="setup.py" %}
```python
from setuptools import setup
# you might be got error with below line.
# but there is no issue when build `cython` script. so go ahead.
from Cython.Build import cythonize

# define build target
setup(
    ext_modules=cythonize("helloworld.pyx")
)
```
{% endcode %}

in `helloworld.pyx` write down like below. nothing special:

{% code title="helloworld.pyx" %}
```python
print("Hello Cython")
```
{% endcode %}

in `main.py` we call built result:

```python
import pyximport; pyximport.install()
import helloworld

if __name__ == "__main__":
    """
    as you see in `helloworld.pyx` print "Hello Cython" 
    when call the script. so actually, we do not need write this.
    """
    pass
```

### Build

after finished setup, let's compile `cython` script. command like below:

```shell
python setup.py build_ext --inplace
```

after build `cython` you can see `helloworld.c` file and `/build`. and other stuffs. in this time, we do not cover about that.

### Run

let's call `cython`.

```shell
python3 main.py
# Hello Cython
```



### References

* [Cython Basic Tutorial](https://cython.readthedocs.io/en/latest/src/tutorial/cython\_tutorial.html#cython-hello-world)
