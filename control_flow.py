#!/usr/bin/env python

x = 3

# if, elif, else
# substitues for 'switch' statements 
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'
    
# backwards if syntax
y = 2 if x==3 else 4 
# y is 2
y = 2 if x==5 else 4 
# y is 4


# for loop 

seq = [1,2,3,4,5]

for i in seq:
    if i == 2: continue     # ends this iteration of the loop and starts the next
    print i
    if i == 3: break        # breaks out of the loop altogether

# If seq is a dictionary, i iterates through the keys.
# 
# With nested loops, continue and break operate on the innermost loop


# While loop

count = 0
while(count < 100):
    count += 1
    
# Executes loop while the condition is true.  
# Keywords continue and break work similar to for loop

# With
with open("control_flow.py") as f:
    data = f.read()
    #do something with data
    
# 'with' can be used with data types that know how to clean up in case of an error.
# File handles, in this example, know how to clean up after themselves.
# You can implement this in an object by implementing the __enter__ and __exit__
# calls.  For file handles, __exit__ always closes the handle.