with open("day1data.txt", "r") as datafile:
    data = datafile.read()

floor = 0

for i in range(len(data)):
    if data[i] == "(":
        floor += 1
    elif data[i] == ")":
        floor -= 1
    if floor == -1:
        print("Basement: ", i+1)

print(floor)
