def badFunction( x,y ):
    z=x+y
    if(z>10):
      print('result is:'+str(z))
    return      z

# unused import
import os
import sys

# undefined variable
print(undefined_variable)

# bad whitespace and missing docstring
class badClass:
  def __init__(self):
    self.x=1
    self.y=2