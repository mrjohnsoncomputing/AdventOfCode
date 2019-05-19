#List comprehension
with open("day6data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "turn"] for i in datafile.read().split("\n") if i]
grid = [[0] * 1000 for i in range(1000)]
bright_grid = [[0] * 1000 for i in range(1000)]
lightson = 0
brightness = 0
for instruction in data:
    coord_1 = [int(i) for i in instruction[1].split(",")]
    coord_2 = [int(i) for i in instruction[3].split(",")]
    action = instruction[0]
    for y in range(coord_1[1],coord_2[1]+1):
        for x in range(coord_1[0],coord_2[0]+1):
            if action == "on":
                if grid[y][x] == 0:
                    lightson += 1
                grid[y][x] = 1
                bright_grid[y][x] += 1
                brightness += 1
            elif action == "off":
                if grid[y][x] == 1:
                    lightson -= 1 
                grid[y][x] = 0
                if bright_grid[y][x] > 0:
                    bright_grid[y][x] -= 1
                    brightness -= 1
            elif action == "toggle":
                brightness += 2
                bright_grid[y][x] += 2
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
print("There are", lightson, "lights on.")
print("Brightness:", brightness)

