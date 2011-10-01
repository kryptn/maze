#!/usr/bin/python

import Image, random

class Node(object):
   def __init__(self, x=None, y=None):
      self.location = None
      if x and y:
         self.location = (x,y)
      self.visited = False
      self.up = False
      self.down = False
      self.left = False
      self.right = False

   @property
   def top(self):
      return [1,int(self.up),1]
   
   @property
   def mid(self):
      return [int(self.left),0,int(self.right)]
   
   @property
   def bottom(self):
      return [1,int(self.down),1]
   
   def __repr__(self):
      return str(self.location)

class Maze(object):
   def initialize(self, height, width,):
      grid = list()
      for x in xrange(height):
         grid.append(list())
         for y in xrange(width):
            grid[x].append(Node(x, y))
      return grid

   def show(self):
      data = list()
      for row in self.grid:
         top, mid, bottom = list(), list(), list()
         for node in row:
            top += node.top
            mid += node.mid
            bottom += node.bottom
         data += top + mid + bottom
      im = Image.new('1', (self.width*3, self.height*3))
      im.putdata(data)
      im.save('maze.png')
      im.show()

   def make(self):
      pass

   def __init__(self, x, y):
      self.height = x
      self.width = y
      self.grid = self.initialize(self.height, self.width)


class PoC(Maze):
   def make(self):
      print __name__
      for row in self.grid:
         for node in row:
            node.up = True
            node.down = True

class Drunk(Maze):

   def pickDirection(self, x, y):
      pass

   def make(self):
      nodes = self.height * self.width
      visited = 0
      rx = random.randint(0, self.width)
      ry = random.randint(0, self.height)
      location = (rx, ry)
      self.grid[rx][ry].visited = True
      while visited < nodes:
      	pass
         