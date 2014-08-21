#!/usr/bin/env python

# Importing packages

# Python is built on packages.  To get access to a package, you import that package.  Importing loads
# the code into memory (it gets parsed) and some of it becomes available in the current namespace, 
# depending on how it was loaded.

# Simple import

import math

print math.pi       # prints 3.14159265359
print math.e        # prints 2.71828182846

# Anything in the math package is available using the 'math.' prefix.
# You can use dir(math) to see all the things in the math package.
# You can use help(math) to see the docs for the package.
# You can use help(math.cosh) to see docs for a particular function.

# Import into current namespace

# You may only need one or two items from a namespace and you'd like to import them into the current 
# namespace so they don't need to be referenced with the 'math.' prefix everywhere.
# You can import these explicitly into the current namespace.

from math import pi
print pi        # prints 3.14159265359

# You can also import as a different name using 'as'.

from math import e as shazam
print shazam         # prints 2.71828182846

# Also works for package names

import math as voodoo
print voodoo.pi         # prints 3.14159265359

# Never import *

# It is legal to import everything from a package into the current namespace by importing *

from math import *

# This is a crutch for the lazy and weak-minded.  You should avoid this because it pollutes the current 
# namespace and can cause unexpected name collisions.  There are times when it's useful, but you should
# have a good reason to do it.

# Importing and Exceptions

# Sometimes there are multiple modules that do the same thing, but you'd rather use one if it is available.
# The pickle module is used to serialize Python objects.  On some platforms, there is a cPickle module
# that has the same API, but it's faster because it's written in C.  You can try to import cPickle and
# fall back to pickle if it's not there.  Using aliasing, you can refer to both as pickle in the rest of 
# the code.

try:
   import cPickle as pickle
except ImportError, e:
   import pickle
 
# Another common pattern is to attempt to import a package to probe for available features and set a boolean
# flag accordingly.  For example, you could disable JSON parsing as an option if the JSON parser isn't 
# available.

hasJSON = True
try:
    import simplejson
except ImportError, e:
    hasJSON = False
    
# Import Search Path

# When you import a module, python looks at the import search path for a module with a matching name.  The 
# search path is literally a Python list of strings.  Each string is a directory name to search.  The list
# is stored in the sys module as sys.path.  You can programmatically alter this list to change the search path.
import sys
print sys.path

# If you import a module and arent' sure it's the right one, you can check it's __file__ attribute.  This is
# the physical file that the Python interpreter loaded the module from.

import math
print math.__file__
# prints '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so'

# Importing only loads a file once

# If a module is loaded via 'import' multiple times, it only gets loaded once.  To actually import a module
# a second time (actually run it's initialization code again), use the reload() function.

