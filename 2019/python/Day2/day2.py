import johnson


johnson.welcome(2)


def part1(inp1=12, inp2=2):
    puzzle_input = johnson.readfile("data.txt", ",")
    puzzle_input[1] = inp1
    puzzle_input[2] = inp2

    for i in range(0, len(puzzle_input)-3, 4):
        int_code = int(puzzle_input[i])

        input_position_1 = int(puzzle_input[i + 1])
        input_position_2 = int(puzzle_input[i + 2])

        input1 = int(puzzle_input[input_position_1])
        input2 = int(puzzle_input[input_position_2])

        num3 = 0

        if int_code == 1:
            num3 = input1 + input2
        elif int_code == 2:
            num3 = input1 * input2
        elif int_code == 99:
            break
        else:
            print("{}: Something went wrong... Invalid Intcode".format(i))

        data_position = int(puzzle_input[i + 3])

        puzzle_input[data_position] = num3

    return puzzle_input[0]


def part2():
    TARGET = 19690720
    for i in range(99):
        for j in range(99):
            if part1(i, j) == TARGET:
                return 100 * i + j


print(part2())