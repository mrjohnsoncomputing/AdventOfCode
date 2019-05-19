#List comprehension
with open("day6data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "turn"] for i in datafile.read().split("\n") if i]
grid = [[0]*1000]
grid = grid * 1000
lightson = 0
for instruction in data:
    #print(instruction)
    c1 = [int(i) for i in instruction[1].split(",")]
    c2 = [int(i) for i in instruction[3].split(",")]
    #print(c1,c2)
    action = instruction[0]
    if c1[0] > c2[0]:
        xmax = c1[0]
        xmin = c2[0]
    else:
        xmax = c2[0]
        xmin = c1[0]
        
    if c1[1] > c2[1]:
        ymax = c1[1]
        ymin = c2[1]
    else:
        ymax = c2[1]
        ymin = c1[1]
        
    for y in range(ymin,ymax+1):
        for x in range(xmin, xmax+1):
            if action == "on":
                if grid[y][x] == 0:
                    lightson += 1
                grid[y][x] = 1
            elif action == "off":
                if grid[y][x] == 1:
                    lightson -= 1 
                grid[y][x] = 0
            elif action == "toggle":
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    lightson -= 1
                elif grid[y][x] == 0:
                    grid[y][x] = 1
                    lightson += 1
                else:
                    print("Toggle Error")
            else:
                print("Action error")
    #print(lightson, action)

print(lightson)
lightson = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            lightson+=1
print(lightson)
