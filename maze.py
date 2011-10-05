#!/usr/bin/python
import Image, random, time

class Node(object):
   """ Represents a node in the grid """
   def __init__(self, x, y):
      self.location = (x,y)
      self.visited = False
      self.up = False
      self.down = False
      self.left = False
      self.right = False

   def __repr__(self):
      return str(self.location)

class Maze(object):
   def initialize(self, height, width,):
      """ makes the maze grid itself """
      grid = list()
      for x in xrange(height):
         grid.append(list())
         for y in xrange(width):
            grid[x].append(Node(x, y))
      return grid

   def show(self):
      """ makes maze to an image file """
      data = []
      for row in self.grid:
         mid, bottom = [], []
         for node in row:
         	mid += [0, int(node.right)]
         	bottom += [int(node.down), 1]
         data += mid + [0] + bottom + [0] 
      data[self.width*2+1] = 1
      data[-1] = 1
      data += (self.width*2) * [0]
      im = Image.new('1', (self.width*2+1, self.height*2+1))
      im.putdata(data)
      im.save('maze.png')
      im.show()
   
   def findDirection(self, p1, p2):
      x1, y1 = p1
      x2, y2 = p2

      if x1 == x2:
         if y1 > y2: #down
            return 'down'
         else: #up
            return 'up'
      else:
         if x1 > x2: #right
            return 'right'        
         else: #left
            return 'left'
   
   def makeBinaryTree(self, point, origin=None):
      pass

   def solve(self):
      pass

   def nextBranch(self, x, y, limitNew=False, returnList=False):
      """ finds next node to branch to """
      valid = list()
      if x > 0:
         valid.append((x-1, y, self.grid[x-1][y].visited))
      if x < self.width-1:
         valid.append((x+1, y, self.grid[x+1][y].visited))
      if y > 0:
         valid.append((x, y-1, self.grid[x][y-1].visited))
      if y < self.height-1:
         valid.append((x, y+1, self.grid[x][y+1].visited))
      
      if limitNew:
         actuallyValid = list()
         for coord in valid:
            if not coord[2]:
               actuallyValid.append(coord)
         valid = actuallyValid

      valid = map(lambda x: x[:2], valid)

      if returnList:
         return valid
      elif valid:
         return random.choice(valid)
      else:
         return False
      
   def connect(self, p, c):
      """ connects two nodes """
      x1, y1 = p
      x2, y2 = c
      d = self.findDirection(p, c)
      if   d == 'down':
         self.grid[x1][y1].down = True
         self.grid[x2][y2].up = True
      elif d == 'up':
         self.grid[x1][y1].up = True
         self.grid[x2][y2].down = True
      elif d == 'right':
         self.grid[x1][y1].right = True
         self.grid[x2][y2].left = True         
      elif d == 'left':
         self.grid[x1][y1].left = True
         self.grid[x2][y2].right = True

   def make(self):
      """
      placeholder make function, extend and 
      write your own algorithm
      """
      pass

   def __init__(self, x, y):
      """ m = Maze(width, height) """
      self.height = x
      self.width = y
      self.grid = self.initialize(self.height, self.width)
      self.randx = random.randint(0, self.height-1)
      self.randy = random.randint(0, self.width-1)
      #self.make()
      #self.show()

class Drunk(Maze):
   """ totally doesn't work yet """
   def make(self):
      nodes = self.height * self.width
      visited = 1
      rx = random.randint(0, self.width)
      ry = random.randint(0, self.height)
      location = (rx, ry)
      self.grid[rx][ry].visited = True
      while visited < nodes:
         pass

class RecursiveBacktrack(Maze):
   """ 
   Uses the Recursive Backtrack algorithm
   m = RecursiveBacktrack(width, height)
   """
   def make(self):
      stack, cont = list(), True
      rx = random.randint(0, self.width-1)
      ry = random.randint(0, self.height-1)
      self.grid[rx][ry].visited = True
      while cont:
         next = self.nextBranch(rx, ry, True)
         if next:
            stack.append((rx, ry))
            self.connect((rx, ry), next)
            rx, ry = next
            self.grid[rx][ry].visited = True
         else:
            if stack:
               rx, ry = stack[-1]
               stack.pop(-1)
            else:
               cont = False

class GrowingTree(Maze):
   """ not working yet """
   def make(self):
      rx = random.randint(0, self.width-1)
      ry = random.randint(0, self.height-1)
      self.grid[rx][ry].visited = True
      stack = [(rx, ry)]
      while stack:
         current = random.choice(stack)
         valid = self.nextBranch(current[0], current[1], True, True)
         if valid:
            next = random.choice(valid)
            self.grid[next[0]][next[1]].visited = True
            self.connect(current, next)
            stack += valid
         else:
            stack.pop(stack.index(current))

rb = RecursiveBacktrack