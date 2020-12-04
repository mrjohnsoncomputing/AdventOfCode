# How many passwords are valid according to their policies?
import helper

print("Advent of Code: Day 2")

def passwordIsValidInOldSystem(test_item):
    times = test_item[0].split("-")

    minimum_time = int(times[0])
    maximum_time = int(times[1])

    test_letter = test_item[1][0]
    password = test_item[2]
    count = 0

    for letter in password:
        if letter == test_letter:
            count += 1

    if count >= minimum_time and count <= maximum_time:
        return True
    else:
        return False

def passwordIsValid(test_item):
    positions = test_item[0].split("-")

    first_position = int(positions[0]) - 1
    second_position = int(positions[1]) - 1

    test_letter = test_item[1][0]
    password = test_item[2]
    

    if password[first_position] == test_letter and password[second_position] == test_letter:
        return False
    elif password[first_position] == test_letter or password[second_position] == test_letter:
        return True
    else:
        return False

puzzle_data = helper.readfile("2020/day2data.txt")

#test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
def check_passwords(data, system="new"):
    valid_passwords = 0

    for i in range(len(data)):
        test_password = data[i].split(" ")
        if system == "old":
            result = passwordIsValidInOldSystem(test_password)
        else:
            result = passwordIsValid(test_password)
        valid_passwords += result

    print("There are " + str(valid_passwords) + " valid passwords in the list for the " + system + "system")

check_passwords(puzzle_data, "old")
check_passwords(puzzle_data)