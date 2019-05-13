with open("day6data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "turn"] for i in datafile.read().split("\n") if i]

grid = [[0]*1000]
grid = grid * 1000
lightson = 0
for instruction in data:
    c1 = [int(i) for i in instruction[1].split(",")]
    c2 = [int(i) for i in instruction[3].split(",")]
    action = instruction[0]
    if c1[0] > c1[1]:
        xmax = c1[0]
        xmin = c1[1]
    else:
        xmax = c1[1]
        xmin = c1[0]
    if c2[0] > c2[1]:
        ymax = c2[0]
        ymin = c2[1]
    else:
        ymax = c2[1]
        ymin = c2[0]
    for x in range(xmin,xmax):
        for y in range(ymin, ymax):
            if action == "on":
                if grid[x][y] == 0:
                    lightson += 1
                grid[x][y] == 1
            elif action == "off":
                if grid[x][y] == 1:
                    lightson -= 1
                grid[x][y] == 0
                lightson -= 1
            elif action == "toggle":
                if grid[x][y] == 1:
                    grid[x][y] == 0
                    lightson -= 1
                else:
                    grid[x][y] == 1
                    lightson += 1

print(lightson)
