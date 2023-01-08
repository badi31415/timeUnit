#!/usr/bin/env python
from timeUnit import timeUnit as tu

def test_add_int():
    a1 = tu()
    a1 += 1
    astr ="%s" % a1
    assert(astr == "00:00:00:01")
    a1 += 59
    astr ="%s" % a1
    assert(astr == "00:00:01:00")
    a1 += (59*60)
    astr ="%s" % a1
    assert(astr == "00:01:00:00")
    a1 += (60*60)
    astr ="%s" % a1
    assert(astr == "00:02:00:00")
    a1 += 24*(60*60)
    astr ="%s" % a1
    assert(astr == "01:02:00:00")


    a2 = tu(60)
    a2str ="%s" % a2
    assert(a2str == "00:00:01:00")
    a2 = tu(3600)
    a2str ="%s" % a2
    assert(a2str == "00:01:00:00")
    a2 = tu(24*3600)
    a2str ="%s" % a2
    assert(a2str == "01:00:00:00")
