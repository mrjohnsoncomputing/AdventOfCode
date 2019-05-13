import helper
import re
data = helper.getData("7")
chains = []

class Chain:
  def __init__(self, item1, item2):
    self.chain = [item1, item2]

  def checkMember(self, checkChar):
    for i in range(len(self.chain)):
      if self.chain[i] == checkChar:
        return True
    return False

  def combineChains():
    

def parseData():
  reg = re.compile(r" [a-zA-Z] ")
  for i in range(len(data)):
    l = reg.findall(data[i])
    c = Chain(l[0].strip(), l[1].strip())
    chains.append(c)
    
def combineChains():
  for i in range(len(chains)):

    for j in range(i+1, len(chains)):
      if 


def main():
  print("Starting Day 7")
  parseData()
  helper.printArray(chains)