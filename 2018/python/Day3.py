import re

day = "Day3"
raw_data = open(day + "Data.txt", "r")
data = raw_data.read()
data = data.splitlines()
raw_data.close()

fabric = 1000
claims = []

class Claim:
	def __init__(self,idd,x,y,w,h):
		self.id = idd
		self.pos = {"x":x-1,"y":y-1}
		self.size = {"x":w,"y":h}
        
	def markFabric(self, fabric):
		for i in range(self.pos["y"], self.pos["y"] + self.size["y"]):
			for j in range(self.pos["x"], self.pos["x"] + self.size["x"]):
				fabric[i][j] += 1
		return fabric
	
	def checkClaim(self, marked_fabric):
		for i in range(self.pos["y"], self.pos["y"] + self.size["y"]):
			for j in range(self.pos["x"], self.pos["x"] + self.size["x"]):
				if(marked_fabric[i][j] > 1):
					return False
		return True

def parseData():
    reg = re.compile(r"\d+")
    for d in data:
        l = reg.findall(d)
        c = Claim(l[0], int(l[1]), int(l[2]), int(l[3]), int(l[4]))
        claims.append(c)
    return claims

def createFabric():
	n = 1000
	fabric = []
	for i in range(n):
		f = [0] * n
		fabric.append(f)
	return fabric

def makeClaims(fabric):
	claims = parseData()
	f = fabric
	for i in range(len(claims)):
		f = claims[i].markFabric(f)
	return f

def checkOverlap(marked_fabric):
	total = 0
	for i in range(len(marked_fabric)):
		for j in range(len(marked_fabric[i])):
			if (marked_fabric[i][j] > 1):
				total += 1
	return total

def checkClaims(marked_fabric):
	for i in range(len(claims)):
		bool = claims[i].checkClaim(marked_fabric)
		if (bool):
			return claims[i].id
	return False

def main():
	fabric = createFabric()
	marked_fabric = makeClaims(fabric)
	overlaps = checkOverlap(marked_fabric)
	print(overlaps)
	single_claim = checkClaims(marked_fabric)
	print(single_claim)
    
    
