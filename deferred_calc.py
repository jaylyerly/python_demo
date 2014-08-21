#!/usr/bin/env python

from cube import cube

c = cube(3, 4, 5, debug = True)
print "Created cube."
print "Cube volume is", c.volume
c.width = 10
c.height = 10
c.depth = 10
print "Updated cube."
print "Cube volume is", c.volume
print "Cube volume is still", c.volume
print "Cube volume is still", c.volume
