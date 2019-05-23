## Class Declarations ##
class Location:
    def __init__(self, location):
        self.location = location
        self.destinations = []

    def addDestination(self, node):
        self.destinations.append(node)

class Destination:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance

class Journey:
    def __init__(self, start):
        self.start = start
        self.distance = 0
        self.route = []

    def travel(self, destination):
        this.route.append(destination.destination)
        this.distance += int(destination.distance)
        
## Function Declarations ##
def printNodes():
    for node in nodes:
        print("Node:", node.location)
        for i in range(len(node.destinations)):
            print("     ",i+1, "Destination:", node.destinations[i].destination, " "*(15 - len(node.destinations[i].destination)),"| Distance:", node.destinations[i].distance)

def parseData(data):
    nodes = []
    for d in data:
        logged = False
        if (len(nodes) > 0):
            for node in nodes:
                if node.location == d[0]:
                    destination = Destination(d[1], d[2])
                    node.addDestination(destination)
                    logged = True
        if logged == False:
            location = Location(d[0])
            destination = Destination(d[1],d[2])
            location.addDestination(destination)
            nodes.append(location)
    return nodes

def getPlaces(nodes)
    p = {nodes[0].location}
    for n in nodes:
        p.add(n.location)
        for d in n.destinations:
            p.add(d.destination)
    return p

## Program ##
with open("day9data.txt", "r") as datafile:
    dataset = [[j for j in i.split(" ") if j != "=" and j != "to"] for i in datafile.read().split("\n") if i]

nodes = parseData(dataset)
places = getPlaces(nodes)

## Need to adapt algorithm to run backwards through destinations to
## compile full destination map

## For any given start location
## Next location <- destination with shortest distance
## While next destination is already visited
## ## Next location <- destination with next shortest distance
## If 
## 
printNodes()
            
