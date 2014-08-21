#!/usr/bin/env python

# Exceptions

# Exceptions are very common in python and used often in the course of 
# regular programming to handle error conditions, and other semi-expected
# situations

# In general, 
#
#  try:
#     < do some work which might error >
#  except:
#     < handle and/or report the error > 
#

try:
    1/0
except Exception, e:
    print "Uh-oh:", e

# This fails due to the divide by zero error.  Because we catch the 
# exception, the script will continue to process.  If we didn't catch
# the exception, it would bubble up the call stack to the top level
# where the system error handler would catch it.  It prints out the 
# exception description and the call stack, then causes python to exit.

# Recovering from error
a = {}      # empty dictionary
try:    
    b = a["foo"]
except KeyError, e:
    b = "bar"
    
# When you access a key in a dictionary that doesn't have that key, it 
# throws a KeyError.  This demonstrates how you can use a try/except block
# to gracefully recover from a missing key, use a default instead, and
# keep going.
#
# In practice, we'd use
# b = a.get("foo", "bar")
# but this is how it's implemented.

# Catching multiple errors
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError, e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error"
    raise

# This shows how to catch separate errors for a single block of code.
# The IOError probably comes from an issue with the open() call --
# like a missing or unreadable file.  The ValueError will be thrown 
# if the argument to int() doesn't make sense.  In each case, you can
# handle the error appropriately to the error.
#
# The final except prints out a message and then calls 'raise', which 
# takes the last exception and raises it again, so it can bubble up through 
# the exception handling layers

# Ignore errors
try:
    #execute some stuff
    1/0
except:
    pass

# Creating your own Exceptions

# Sometimes it's useful to have your own exceptions so you can signal error
# conditions during a low level operation and easily handle it at a high 
# level.  Usually, it's sufficient just to make an empty subclass of Exception.


class MyException(Exception):
    pass

try:
    raise MyException("Error -- Invalid animal 'BearCat'.")
except MyException, e:
    print "Caught error:", e
    
