#!/usr/bin/env python

class cube(object):
  
    def __init__(self, width=0, height=0, depth=0, debug=False):
        self.width = width
        self.height = height
        self.depth = depth
  
    def calculateVolume(self):
        return self.width * self.height * self.depth
   
    def __repr__(self):
        return "cube(width=%s,height=%s,depth=%s)" % \
            (self.width, self.height, self.depth)

    def __str__(self):
        return "cube(%sx%sx%s)" % \
            (self.width, self.height, self.depth)
  
if __name__ == '__main__':
  c = cube(3,4,5)
  print "Created cube."
  print "Cube volume is", c.calculateVolume()
  c.width = 10
  c.height = 10
  c.depth = 10
  print "Updated cube."
  print "Cube volume is", c.calculateVolume()
  print "String representation is", str(c)
  print "Repr representation is", repr(c)
