"""Python serial number generator."""
#MAYBE IMPORT COUNTER?   from collections import Counter  ??
#input a number and it should return the next sequential number

class SerialGenerator:
  #serial = SerialGenerator(start=100)
   ## """Machine to create unique incrementing serial numbers.
   # 
   # 
   # >>> serial = SerialGenerator(start=100)
#
   # >>> serial.generate()
   # 100
#
   # >>> serial.generate()
   # 101
#
   # >>> serial.generate()
   # 102
#
   # >>> serial.reset()
#
   # >>> serial.generate()
   # 100
   # #"""
  def __init__(self, start):
    #won't work with a third variable...
    #self.start = self.next = start  FROM THE SOLUTION....no idea this could be done.
    self.start = start
    self.next = start

  def generate(self):
    #return self.start + 1
    self.next += 1
    return self.next - 1
    
  # no use for this: def update_org(self):

  def reset(self):
    self.next = self.start




