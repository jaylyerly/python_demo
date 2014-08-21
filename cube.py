#!/usr/bin/env python

class cube(object):
  
    def __init__(self, width=0, height=0, depth=0, debug=False):
        self.width = width
        self.height = height
        self.depth = depth
        self.debug = debug
    
    def __setattr__(self, name, value):
        if name in ["width", "height", "depth"]:
            self.isDirty = True
        return object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        if name == "volume" and self.isDirty:
            self._calculateVolume()
        return object.__getattribute__(self, name)
  
    def _calculateVolume(self):
        if self.debug: print "\n*Calculating volume...*\n"
        self.isDirty=False
        self.volume = self.width * self.height * self.depth
   
    def __repr__(self):
        return "cube(width=%s,height=%s,depth=%s,debug=%s)" % \
            (self.width, self.height, self.depth, self.debug)

    def __str__(self):
        return "cube(%sx%sx%s)" % \
            (self.width, self.height, self.depth)
  
if __name__ == '__main__':
  c = cube(3,4,5,debug=True)
  print "Created cube."
  print "Cube volume is", c.volume
  c.width = 10
  c.height = 10
  c.depth = 10
  print "Updated cube."
  print "Cube volume is", c.volume
  print "Cube volume is still", c.volume
  print "Cube volume is still", c.volume
  print "String representation is", str(c)
  print "Repr representation is", repr(c)
