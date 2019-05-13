import helper
import math
import turtle
data = helper.getData("6")

# Trying to get Turtle to visualise the data. Unable to get turtle to do what I want!

def createCoords(arr):
  for i in range(len(arr)):
    coords = helper.splitString(", ", arr[i])
    c = {"x":int(coords[0]), "y":int(coords[1])}
    arr[i] = c
  print("Coords Created")
  return arr

def getRange(arr):
  x = 0
  y = 0
  for i in arr:
    if i["x"] > x:
      x = i["x"]
    if i["y"] > y:
      y = i["y"]
  return {"x":x, "y":y,}

def createGrid(locations):
  rang = getRange(locations)
  grid = helper.createSizedArray(rang["y"], None)
  for i in range(len(grid)):
    grid[i] = helper.createSizedArray(rang["x"], None)
  j = 0
  for i in locations:
    y = i["y"]
    x = i["x"]
    if grid[y] == None:
      grid[y] = helper.createSizedArray(rang["x"], None)
    grid[y][x] = str(j)
    j += 1
  print("Grid Created")
  return grid

def calculateManhattanDistance(point1, point2):
  x = helper.getDifference(point1["x"], point2["x"])
  y = helper.getDifference(point1["y"], point2["y"])
  return x + y

def findNearestLocation(locations, point):
  distances = []
  for i in range(len(locations)):
    d = calculateManhattanDistance(point, locations[i])
    distances.append({"distance":d, "index":i})
  distances = helper.sortDictionaryArray(distances, "distance")
  if distances[0]["distance"] == distances[1]["distance"]: 
    return "."
  else:
    return distances[0]["index"]

def calculateGridDistances(grid, locations):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      point = {"x":j, "y":i}
      if grid[i][j] == None:
        grid[i][j] = findNearestLocation(locations, point)
  return grid

def drawGrid(grid):
  print("Drawing Grid")
  #Create turtle canvas
  wn = turtle.Screen()
  wn.setup(len(grid[0]), len(grid), 0,0)
  #Set canvas background colour
  wn.bgcolor("white")
  wn.title("Advent of Code - Day 6")
  wn.exitonclick()         
  #Create new turtle
  t = turtle.Turtle()
  t.pensize(5)
  for i in range(len(grid)):
    t.pu()
    t.goto(0, i)
    t.pd()
    for j in range(len(grid[i][j])):
      x = grid[i][j]
      if x != ".":
        t.color("blue")
      else:
        t.color("black")
      t.fd(1)
    
    



def main():
  print("Beginning Day 6")
  locations = createCoords(data)
  grid = createGrid(locations)
  grid = calculateGridDistances(grid, locations)
  drawGrid(grid)
  