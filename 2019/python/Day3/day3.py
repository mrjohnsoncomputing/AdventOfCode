import johnson, threading


class Wire:
    def __init__(self, inputs):
        self.inputs = inputs
        self.path = []
        self.pos = {
            "x": 0,
            "y": 0
        }
        self.parse_inputs()

    def parse_inputs(self):
        for i in range(len(self.inputs)):
            string = self.inputs[i]
            instruction = string[0]
            amount = int(string[1:len(string)])

            for j in range(1, amount+1):
                if instruction == "R":
                    coord = str(self.pos["x"]+j) + ":" + str(self.pos["y"])
                elif instruction == "L":
                    coord = str(self.pos["x"]-j) + ":" + str(self.pos["y"])
                elif instruction == "U":
                    coord = str(self.pos["x"]) + ":" + str(self.pos["y"]+j)
                elif instruction == "D":
                    coord = str(self.pos["x"]) + ":" + str(self.pos["y"]-j)
                else:
                    print("Error Parsing input")
                    exit(1)

                self.path.append(coord)

            if instruction == "R":
                self.pos["x"] += amount
            elif instruction == "L":
                self.pos["x"] -= amount
            elif instruction == "U":
                self.pos["y"] += amount
            elif instruction == "D":
                self.pos["y"] -= amount

# johnson.welcome(3)


def difference(coords):
    coords = coords.split(":")
    n1 = abs(int(coords[0]))
    n2 = abs(int(coords[1]))
    return n1 + n2


def part1():
    puzzle_input = johnson.readfile("data.txt")
    print("Input Imported")

    wire1 = Wire(puzzle_input[0].split(","))
    wire2 = Wire(puzzle_input[1].split(","))
    print("Wires Created")

    record = 999999999

    for i in range(len(wire1.path)):
        if wire1.path[i] in wire2.path:
            # intersections.append(wire1.path[i])
            dist = difference(wire1.path[i])
            if dist < record:
                record = dist
                print("i: {} -- Record: {}".format(i, record), end="\r", flush=True)

    print("Final Record: {}".format(record))


part1()

