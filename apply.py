#!/usr/bin/env python

from cube import cube

shape = cube
# shape points to cube class

dims = [3,4,5]

# You can use a python list to pass args to a function
# Instead of 
# c1 = shape(3,4,5), you can do this:
c1 = shape(*dims)
print "c1 is", c1

params = {
    "depth" : 7,
    "width" : 5,
    "height" : 6,
}

# Likewise, you can pass a dictionary instead of keyword arguments.
# The great thing about this is that order doesn't matter.
# Instead of 
# c2 = shape(depth=7, width=5, height=6), you can do this:
c2 = shape(**params)
print "c2 is", c2

# works the other way too
# functions can accept argument lengths of unknown length
# and/or with unknown keyword args

def argsAndKwargs(*aList, **aDict):
    for i in aList:
        print "aList:", i
    for k,v in aDict.items():
        print "aDict - key:", k,"value:", v

argsAndKwargs(1, "foo", 3.141, bar="baz", one=1, fox="quick brown")

# prints out:
# aList: 1
# aList: foo
# aList: 3.141
# aDict - key: fox value: quick brown
# aDict - key: bar value: baz
# aDict - key: one value: 1
