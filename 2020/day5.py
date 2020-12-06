import helper
import math
print("Advent of Code: Day 5")

def get_middle(big_num, small_num):
    difference = big_num - small_num
    middle = small_num + (difference / 2)
    return middle

def search_boarding_pass(boarding_pass):
    row_position = [0, 127]
    seat_position = [0, 7]
    for instruction in boarding_pass:
        if instruction == "B":
            # B means to take the upper half, keeping rows 32 through 63.
            middle = get_middle(row_position[1], row_position[0])
            middle = math.ceil(middle) 
            row_position[0] = middle
        elif instruction == "F":
            # F means to take the lower half, keeping rows 0 through 63.
            middle = get_middle(row_position[1], row_position[0])
            middle = math.floor(middle)
            row_position[1] = middle
        elif instruction == "R":
            # R takes upper half
            middle = get_middle(seat_position[1], seat_position[0])
            middle = math.ceil(middle) 
            seat_position[0] = middle
        elif instruction == "L":
            # L takes lower half
            middle = get_middle(seat_position[1], seat_position[0])
            middle = math.floor(middle) 
            seat_position[1] = middle
    return [row_position[0], seat_position[0]]

def search_boarding_passes(boarding_data):
    seat_ids = []
    for boarding_pass in boarding_data:
        seat = search_boarding_pass(boarding_pass)
        seatID = seat[0] * 8 + seat[1]
        seat_ids.append(seatID)
    return seat_ids

def is_two_apart(num1, num2):
    if num1 - num2 == -2 or num1 - num2 == 2:
        return True
    else:
        return False

def check_boarding_passes(boarding_pass_list):
    potential_seats = []
    length = len(boarding_pass_list)
    for i in range(0, length - 1):
        for j in range(1, length):
            if is_two_apart(boarding_pass_list[i], boarding_pass_list[j]):
                surrounding_passes = [boarding_pass_list[i], boarding_pass_list[j]]
                potential_seat = max(surrounding_passes) - 1
                if potential_seat not in boarding_pass_list:
                    potential_seats.append(potential_seat)
    print(potential_seats)

test_data = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
# row 70, column 7, seat ID 567.
# row 14, column 7, seat ID 119.
# row 102, column 4, seat ID 820.

puzzle_data = helper.readfile("2020/day5data.txt")

results = search_boarding_passes(puzzle_data)
print("The highest boarding pass ID is:", max(results))

check_boarding_passes(results)