# ne afiseaza printul
assert 2 * 2 == 5
print('hello world')
# ne afiseaza assersion error
"""assert "m" in "hello "
print('hello world')"""

import unittest


def f(x):
    return x * 2


print(f"f(2)= {f(2)}")
print(f"f(100)= {f(100)}")
print(f"f(-5)= {f(-5)}")
print(f"f(3.14)= {f(3.14)}")
