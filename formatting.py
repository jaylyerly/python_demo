#!/usr/bin/env python

# Python Formatting

# Python code blocks are based on indentation -- not {} or () or [],
# only on indentation.

if True:
    print "Always print me!"
    
# So we don't go insane:
# Set your editor to use spaces instead of tabs.
# NO TABS.
# Use 4 spaces for a tab.

# Line continuation
# 
# By default, a python statement is a single line.
# To extend this to a second line, use a \ at the end

a = 1 + 2 + 4 + 5 \
    + 6 + 7 + 8
    
b = "The quick brown fox jumps over the" + \
    "lazy dog."    
    
# Line continuation is implied if you have an open (), {} or []

if ( a == a or  
     b == b ):
     print "True"
     
c = [ 
    "Monday",
    "Tuesday",
    ]
    
d = {
    "One Fish": "Two Fish",
    "Red Fish": "Blue Fish",
    }

# Comments

# <- The hash mark is a comment, everything after it is ignored.
# It can be on the same line as code, but everything to the right is ignored.