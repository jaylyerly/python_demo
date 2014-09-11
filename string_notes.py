#!/usr/bin/env python

# Notes about python strings

# Multiline strings can be defined with either triple double quotes (""")
# or triple single quotes (''')

a = """Space: the final frontier. 
These are the voyages of the starship Enterprise. 
Its five-year mission: to explore strange new worlds, 
to seek out new life and new civilizations, 
to boldly go where no man has gone before.
"""

# This string will include new line characters as well.
# Triple quotes like this are often used to comment out blocks of code.

# Strings are iterable, so you can treat them like you treat a list.

a = "Don't Panic."

print a[:5]         # prints Don't
print a[6:12]       # prints Panic.
print a[-6:]        # prints Panic.

for letter in a:
    print letter,   # prints D o n ' t   P a n i c .
    

# Building strings

# You can multiply strings to repeat them

print "Don't", " "*20, "Panic."  # prints Don't                      Panic.

# You can concatenate strings with '+', but it's a really bad idea

print "Don't "+"Panic."     # prints Don't Panic.

# The + operator only works on two strings.  

try:
    print "Furious " + 5
except TypeError, e:
    print "Oops:", e
    
# Much safer to use the % format operator and embed %s in your string.
# This calls the str() function on the argument before insertion.
# The str() function _always_ works.

print "Furious %s" % 5          #print Furious 5

# If you need to put more than one object in a string, the right side
# argument must be a tuple.

print "%s %s" % ("Don't", "Panic")

# This is cumbersome with more than a couple arguments.  You can use 
# dictionary substitution instead. 

theDict = { 
    "color": "brown",
    "speed": "quick",
    "type" : "lazy",
    }  
    
theString = "The %(speed)s %(color)s fox jumps over the %(type)s dog."

print theString % theDict  # print The quick brown fox jumps over the lazy dog.

# Aside on dictionaries
# To print out the contents of a dictionary, these are equivalent

for k in theDict:                   # as an iterable, dictionaries iterate through the keys
    print "%s:\n\t%s" % (k, theDict[k])
    
for k,v in theDict.items():         # the items() method returns an a list of tuples containing (key,value)        
    print "%s:\n\t%s" % (k,v)
    
for t in theDict.items():           # since items() iterates through tuples, you can pass
    print "%s:\n\t%s" % t           # that tuple directly to the format operator