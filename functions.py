#!/usr/bin/env python

# Functions

# Basic function definition and invocation

def squared(x):
    return x*x
    
print squared(2)        # prints 4

# Parameters can have defaults.

def squared(x=4):
    return x*x

print squared(2)       # prints 4
print squared()        # prints 16

# If you pass parameters by name, order doesn't matter

def cat3(string1="", string2="", string3=""):
    return string1 + string2 + string3

print cat3(string3="ghi", string1="abc", string2="def") # prints abcdefghi

# So it's safer, especially with lots of args, to name them explicitly.
# Protects against situations where the number of args might change during dev.
# Also easier to read.

# Nesting functions

def sortMyList(theList=[]):
    def sortIgnoreCase(x,y):
        return cmp(x.upper(), y.upper())
    theList.sort(cmp=sortIgnoreCase)
    return theList
    
aList = ["Abc","ABD","ABe"]
print sortMyList(aList)

# Scoping rules are such that sortIgnoreCase is only visible inside sortMyList.
# This is good for not polluting the name space, so you're free to use short 
# names for local functions.


# Functions are objects
def hello():
  return "Hello World!"
# 'hello' is the function object.  hello() is the return value.
# Important to remember that help(hello) returns the doc for the hello function.
# help(hello()) returns the doc for the string "Hello World!"

# Functions have attributes

hello.awesome = True
print hello.awesome         # prints True

# This is often used by frameworks to tag functions.  Some web frameworks will
# tag functions to indicate if they're exposed to web clients or internal


