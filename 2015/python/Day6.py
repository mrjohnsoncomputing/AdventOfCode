with open("day6data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "turn"] for i in datafile.read().split("\n") if i]

grid = [[0]*1000]
grid = grid * 1000
print(grid[500])
#for instruction in data:
    #if instruction[0] == "on":

    #elif instruction[0] == "off":

    #elif instruction [0] == "toggle":
