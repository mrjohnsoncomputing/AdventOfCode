import helper

def part1(target, data):
    found = False
    for i in range(len(data)-1):
        first_number = int(data[i])

        for j in range(i+1, len(data)):
            second_number = int(data[j])

            # print(first_number, second_number)
            if first_number + second_number == target:
                print("First Number: {}\nSecond Number: {}".format(first_number, second_number))
                print("Product:", first_number * second_number)
                found = True
                break
        if found:
            break

def part2(target, data):
    found = False
    # Loop through the array up to the third to last element
    for i in range(len(data)-2):
        first_number = int(data[i])
        # Get the three consecutive numbers from position i onwards
        
        for j in range(i+1, len(data)-1):
            second_number = int(data[j])
                
            for k in range(j+1, len(data)):
                third_number = int(data[k])

                # Check to see whether they add up to the target
                if first_number + second_number + third_number == target:
                    print("First Number: {}\nSecond Number: {}\nThird Number: {}".format(first_number, second_number,third_number))
                    product = first_number * second_number * third_number
                    print("Product:", product)
                    return product
    print("Nothing Found")

print("Advent of Code: Day 1")

# find the two entries that sum to 2020 and then multiply those two numbers together.

test_data = [979, 675, 1456, 299, 1721, 366]
puzzle_data = helper.readfile("2020/day1data.txt")

target = 2020
#part1(target, puzzle_data)
part2(target, puzzle_data)


        