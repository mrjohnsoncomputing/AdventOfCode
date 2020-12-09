import helper
print("Advent of Code: Day 9")

def check_number_is_sum(list_of_numbers, test_number):
    # ["35","20","15","25","47"]
    # print(list_of_numbers, test_number)
    for i in range(0, len(list_of_numbers)-1):
        for j in range(1, len(list_of_numbers)):
            sum = int(list_of_numbers[i]) + int(list_of_numbers[j])
            if sum == int(test_number):
                return True
    return False

def part1(data):
    preamble_size = 25
    for i in range(preamble_size, len(data)):
        list_of_numbers = data[i-preamble_size:i]
        result = check_number_is_sum(list_of_numbers, data[i])
        if result == False:
            print("Day 9, Part 1:", data[i])
            return int(data[i])

def sum_list(list_of_numbers, target_number, position):
    total = 0
    start_position = position
    end_position = position
    while total < target_number and end_position < len(list_of_numbers):
        total += int(list_of_numbers[end_position])
        end_position = end_position + 1
    if total == target_number:
        return list_of_numbers[start_position:end_position]
    else:
        return False

def part2(data):
    invalid_number = part1(data)
    for i in range(len(data)):
        result = sum_list(data, invalid_number, i)
        if result != False:
            answer = int(min(result)) + int(max(result))
            print("Day 9, Part 2:", answer)
            break


# To find the encryption weakness, 
# add together the smallest and largest number in this contiguous range; 
# in this example, these are 15 and 47, producing 62.

# What is the encryption weakness in your XMAS-encrypted list of numbers?


test_data = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576"
    ]

puzzle_data = helper.readfile("2020/day9data.txt")

part2(puzzle_data)
