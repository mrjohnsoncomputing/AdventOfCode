#List comprehension
with open("day6data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "turn"] for i in datafile.read().split("\n") if i]
grid = [[0]*1000]
grid = grid * 1000
lightson = 0
for instruction in data:
    #print(instruction)
    coord_1 = [int(i) for i in instruction[1].split(",")]
    coord_2 = [int(i) for i in instruction[3].split(",")]

    action = instruction[0]
        
    for y in range(coord_1[1],coord_2[1]):
        for x in range(coord_1[0],coord_2[0]):
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
