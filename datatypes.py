#!/usr/bin/env python

# integer
myInt = 1

# float
myFloat = 3.14;

# complex
myComplex = complex(1,2)      # 1 + 2j

# string
myString = "The quick brown fox..."

# tuple
myTuple = (myInt, myString, myFloat)
# imutable sequence
# most used to return multiple values from a function

# list
myList = [1, 2, 3]
# standard indexed array type functions 
# sortable
# reverse indices -- myList[-1] -- last item in list
# sliceable -- myList[2:4]

# dictionary
myDict = { "key1" : "value1", "key2" : "value2" }
# key value pair storage
# most useful method -- myDict.get("foo", "bar")
#   returns the value for key "foo", unless it doesn't
#   exist, then returns "bar"

# objects
myObject = object()
# 'object' is the base object from which everything inherits.
# Python supports multiple inheritence, which can be used to
# implement interfaces/protocols.