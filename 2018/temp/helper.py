import re
import math

def getDifference(i, j):
  if i > j:
    return i-j
  else:
    return j-i

def printArray(stuff):
  for i in stuff:
    print(i)

def splitString(inp,str):
  l = re.split(inp,str)
  l = [x for x in l if x != '']
  return l

def AlphabetDictionary():
  results = {
              "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,
            }
  return results

def largestDicInt(dic):
  record = 0
  index = ""
  for i in dic:
    if dic[i] > record:
      record = dic[i]
      index = i
  return index

def smallestDicInt(dic):
  record = math.inf
  index = ""
  for i in dic:
    if dic[i] < record:
      record = dic[i]
      index = i
  return index

def arrayReplace(the_list, val):
   return [value for value in the_list if value != val]

def createSizedArray(size, elem):
  arr = []
  for i in range(size+1):
    arr.append(elem)
  return arr

def getData(day_number):
  raw_data = open("Day" + day_number + "Data.txt", "r")
  data = raw_data.read()
  data = data.splitlines()
  raw_data.close()
  return data

def sortDictionaryArray(arr, key):
  for i in range(len(arr)-1):
    for j in range(len(arr)-1):
      if arr[j+1][key] < arr[j][key]:
        arr = swap(arr, j)
  return arr

def swap(arr, i):
  temp = arr[i]
  arr[i] = arr[i + 1]
  arr[i+1] = temp
  return arr