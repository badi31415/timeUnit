#!/usr/bin/env python
class timeUnit:
    """
    A class to handle a timer or clock class
    """
    t2d = 24*60*60
    d2h = 60*60
    h2m = 60
    m2s = 60

    def __init__(self, init_val=0):
        self.__hms = init_val
        print("Init %d %s" % (int(self),self))

    def __add__(self, other):
        """
        A function to add clocks or to add seconds.
        """
        add_s = int(self)+int(other)
        print("Add %d to %s = %d" % (other, self, add_s))
        return timeUnit(add_s)

    def __int__(self):
        return self.__hms

    def __str__(self):
        """
        Produce string representation of self
        """
        s = self.__hms
        d = s // timeUnit.t2d
        s -= d * timeUnit.t2d
        print("d= %d, (s= %d)" %(d, s))
        h = s // timeUnit.d2h
        s -= h * timeUnit.d2h
        print("h= %d, (s= %d)" % (h, s))
        m = s // timeUnit.h2m
        s -= m * timeUnit.h2m
        print("m= %d, (s= %d)" % (m, s))
        return "%02d:%02d:%02d:%02d" % (d, h, m, s)
