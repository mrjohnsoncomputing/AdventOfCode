with open("day3data.txt", "r") as datafile:
    data = datafile.read()

def move(p,m):
    if m == "^":
        p[1] += 1
    elif m == "v":
        p[1] -= 1
    elif m == "<":
        p[0] -= 1
    elif m == ">":
        p[0] += 1
    else:
        print("Invalid Direction: ", m)
    return p

def part1():
    pos = [0,0]
    positions = []
    houses = 0
    for i in range(len(data)):
        pos = move(pos, data[i])
        try:
            j = positions.index(pos)
        except:
            positions.append(pos)
            houses += 1
    print(houses)

def part2():
    pos = [[0,0],[0,0]]
    positions = []
    houses = 0
    for i in range(0,len(data)-1, 2):
        for j in range(2):
            pos[j] = move(pos[j], data[i+j])
            try:
                p = positions.index(pos[j])
            except:
                positions.append(pos[j][0:2])
                houses += 1
    print(houses)
part2()

