#!/usr/bin/env python

# Built-in python functions

# Most import -- help() and dir()

# help(foo) -- return the docstring for foo.  Most built-ins are documented
# this way.
help(open)      # display the docs for 'open' (used to open files)
help("foo".lstrip)     # display the docs for the string method lstrip

# dir(foo) -- show the attributes of foo                       
# dir() -- the current namespace
dir("foo")      # display all the methods and attributes available on 
                #  the string "foo" 
# this is invaluable as you play with new objects and interfaces

myList = ["a", "b", "c"]

# other useful builtin functions

enumerate(myList) # returns a list of tuples which contain an index and an item 
                  # from the list
for index, item in enumerate(myList):
    print "item", item, "at index", index

# print out
# item a at index 0
# item b at index 1
# item c at index 2


# filter(func, sequence) -- takes each element of a sequence and passes it to 
# 'func'.  If 'func' returns true, that element is put in the returned list.  
# If 'func' returns false, it's dropped

def checkDigit(x):
    return x.isdigit()                

print filter(checkDigit, "abc123")  # prints out "123"

# map(func, sequence) -- takes each element of the sequence and passes it to 
# 'func'.  The return values of 'func' are passed back in a list.

def makeUpperCase(x):
    return x.upper()

print map(makeUpperCase, "abc123")  # prints out "ABC123"
            # Warning -- contrived example -- .upper() works on whole strings


# reduce(func, sequence[, initial]) -- takes the sequence and uses func to reduce
# it to a single value.  For example
#
def addTwo(x,y):
    return x+y
print reduce( addTwo, [1,2,3,4,5]) # would execute ((((1+2)+3)+4)+5)
                                    # and print out 15
# the optional 'initial' paramater primes the sequence
