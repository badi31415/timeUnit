#!/usr/bin/env python
"""
    @author: %(username)s

"""
from timeUnit import timeUnit as tu

def beispiel():
    a1 = tu()
    print(a1)
    a1 += 1
    astr ="%s" % a1
    print("%s" % a1)
    a1 += 59
    astr ="%s" % a1


if __name__ == '__main__':
    beispiel()
