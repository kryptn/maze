#!/usr/bin/python
import Image, random, time

class Node(object):
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
      grid = list()
      for x in xrange(height):
         grid.append(list())
         for y in xrange(width):
            grid[x].append(Node(x, y))
      return grid

   def show(self):
      data = (self.width*2+2) * [1]
      for row in self.grid:
         mid, bottom = [1], [1]
         for node in row:
         	mid += [0, int(node.right)]
         	bottom += [int(node.down), 1]
         data += mid + [0] + bottom + [0] 
      data[self.width*2+2]
      data[-1] = 1
      data += (self.width*2+2) * [0]
      im = Image.new('1', (self.width*2+2, self.height*2+2))
      im.putdata(data)
      im.save('maze.png')
      im.show()

   def make(self):
      pass

   def nextBranch(self, x, y, limitNew=False, debug=False):
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

      if debug:
         return valid

      if valid:
         return random.choice(valid)[:2]
      else:
         return False
      
   def connect(self, p, c):
      x1, y1 = p
      x2, y2 = c

      if x1 == x2:
         if y1 > y2: #down
            self.grid[x1][y1].down = True
            self.grid[x2][y2].up = True
         else: #up
            self.grid[x1][y1].up = True
            self.grid[x2][y2].down = True
      else:
         if x1 > x2: #right
            self.grid[x1][y1].right = True
            self.grid[x2][y2].left = True         
         else: #left
            self.grid[x1][y1].left = True
            self.grid[x2][y2].right = True



   def __init__(self, x, y):
      self.height = x
      self.width = y
      self.grid = self.initialize(self.height, self.width)


class PoC(Maze):
   def make(self):
      pass

class Drunk(Maze):
   def make(self):
      nodes = self.height * self.width
      visited = 1
      rx = random.randint(0, self.width)
      ry = random.randint(0, self.height)
      location = (rx, ry)
      self.grid[rx][ry].visited = True
      while visited < nodes:
         next = self.nextBranch(rx, ry)
         if next[2] == 'up':
            self.grid[rx][ry].up = True
            self.grid[next[0]][next[1]].down = True
         if next[2] == 'down':
            self.grid[rx][ry].down = True
            self.grid[next[0]][next[1]].up = True
         if next[2] == 'left':
            self.grid[rx][ry].left = True
            self.grid[next[0]][next[1]].right = True
         if next[2] == 'right':
            self.grid[rx][ry].right = True
            self.grid[next[0]][next[1]].left = True
         visited += 1

class BTS(Maze):
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


def t():
	m = PoC(300,300)
	m.make()
	m.show()

m = Maze(10,10)
