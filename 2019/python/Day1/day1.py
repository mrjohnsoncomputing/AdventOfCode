import johnson

johnson.welcome(1)
puzzle_input = johnson.readfile("data.txt")


def calculatefuel(weight):
    total = (int(weight) // 3) - 2
    if total > 0:
        return total
    else:
        return 0


def simplefuel():
    total = 0
    for i in range(len(puzzle_input)):
        total += calculatefuel(puzzle_input[i])
    return total


def recursivefuel():
    total = 0
    for i in range(len(puzzle_input)):
        fuel = calculatefuel(puzzle_input[i])
        while fuel > 0:
            total += fuel
            fuel = calculatefuel(fuel)
    return total


johnson.solution("The sum of the fuel requirements is:", simplefuel())
johnson.solution("The sum of the corrected fuel requirements is:", recursivefuel())

