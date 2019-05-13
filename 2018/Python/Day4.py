import re
import sort

day = "Day4"
raw_data = open(day + "Data.txt", "r")
data = raw_data.read()
data = data.splitlines()
raw_data.close()

class TimeStamp:
  def __init__(self,y,mon,d,h,min):
    self.year = y
    self.month = mon
    self.day = d
    self.hour = h
    self.minute = min

class Guard:
  def __init__(self, idd):
    self.id = idd
    self.sleep_times = []
  
  def addTime(self,y,mon,d,h,min):
    t = TimeStamp(y,mon,d,h,min)
    self.sleep_times.append(t)

def parseData():
    new_data = []
    for d in data:
      end = len(new_data)
      indexes = [1,2,4]
      l = re.split('[- : \[ \]]',d)
      l = [x for x in l if x != '']
      for i in range(len(indexes)):
        l[indexes[i]] = int(l[indexes[i]])
      if (end > 1):
        leave = False
        j = indexes[0]
        for i in range(end):
          if (new_data[i][j] > l[j]):
            new_data.insert(i, l)
            break
          elif ((new_data[i][j] == l[j])):
            j = indexes[1]
            for k in range(i, end):
              if (new_data[k][j] > l[j]):
                new_data.insert(k, l)
                leave = True
                break
              elif ((new_data[k][j] == l[j])):
                j = indexes[2]
                for m in range(k, end):
                  if (new_data[m][j] > l[j]):
                    new_data.insert(m, l)
                    leave = True
                    break
              if (leave):
                break
          if (leave):
            break
      else:
        new_data.append(l)
    print("Data Parsed")
    return new_data

def sortData():
  print()

def main():
  d = parseData()
  printArray(d)
  #data = sort.mergeSort(d)
  #print(data)

def printArray(a):
  for i in range(len(a)):
    print(a[i])