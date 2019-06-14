#### Class Declarations ##
##class Location:
##    def __init__(self, location):
##        self.location = location
##        self.destinations = []
##
##    def addDestination(self, node):
##        self.destinations.append(node)
##
##class Destination:
##    def __init__(self, destination, distance):
##        self.destination = destination
##        self.distance = distance
##
##class Journey:
##    def __init__(self, start):
##        self.start = start
##        self.distance = 0
##        self.route = []
##
##    def travel(self, destination):
##        this.route.append(destination.destination)
##        this.distance += int(destination.distance)
##        
#### Function Declarations ##
##def printNodes():
##    for node in nodes:
##        print("Node:", node.location)
##        for i in range(len(node.destinations)):
##            print("     ",i+1, "Destination:", node.destinations[i].destination, " "*(15 - len(node.destinations[i].destination)),"| Distance:", node.destinations[i].distance)
##
##def parseData(data):
##    nodes = []
##    for d in data:
##        logged = False
##        if (len(nodes) > 0):
##            for node in nodes:
##                if node.location == d[0]:
##                    destination = Destination(d[1], d[2])
##                    node.addDestination(destination)
##                    logged = True
##        if logged == False:
##            location = Location(d[0])
##            destination = Destination(d[1],d[2])
##            location.addDestination(destination)
##            nodes.append(location)
##    return nodes
##
##def getPlaces(nodes)
##    p = {nodes[0].location}
##    for n in nodes:
##        p.add(n.location)
##        for d in n.destinations:
##            p.add(d.destination)
##    return p
##
#### Program ##
##with open("day9data.txt", "r") as datafile:
##    dataset = [[j for j in i.split(" ") if j != "=" and j != "to"] for i in datafile.read().split("\n") if i]
##
##nodes = parseData(dataset)
##places = getPlaces(nodes)
##
#### Need to adapt algorithm to run backwards through destinations to
#### compile full destination map
##
#### For any given start location
#### Next location <- destination with shortest distance
#### While next destination is already visited
#### ## Next location <- destination with next shortest distance
#### If 
#### 
##printNodes()

from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


graph = Graph([("Faerun", "Norrath", 129), ("Faerun", "Tristram", 58), ("Faerun", "AlphaCentauri", 13),
               ("Faerun", "Arbre", 24), ("Faerun", "Snowdin", 60), ("Faerun", "Tambi",71), ("Faerun", "Straylight", 67),
               ("Norrath", "Tristram", 142), ("Norrath", "AlphaCentauri", 15), ("Norrath", "Arbre", 135),
               ("Norrath", "Snowdin", 75), ("Norrath", "Tambi", 82), ("Norrath", "Straylight", 54), ("Tristram", "AlphaCentauri", 118),
               ("Tristram", "Arbre", 122), ("Tristram", "Snowdin", 103), ("Tristram", "Tambi", 49), ("Tristram", "Straylight", 97), ("AlphaCentauri", "Arbre", 116),
               ("AlphaCentauri", "Snowdin", 12), ("AlphaCentauri", "Tambi", 18), ("AlphaCentauri", "Straylight", 91), ("Arbre", "Snowdin", 129), ("Arbre", "Tambi", 53),
               ("Arbre", "Straylight", 40), ("Snowdin", "Tambi", 15), ("Snowdin", "Straylight", 99), ("Tambi", "Straylight", 70)])

print(graph.dijkstra("Faerun", "Tambi"))
