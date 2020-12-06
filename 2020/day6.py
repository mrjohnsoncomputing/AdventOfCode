import helper
import math
print("Advent of Code: Day 6")

def part1(data):
    current_position = 0
    count = 0

    for i in range(len(data)):
        if current_position <= i:
            if i+1 == len(data) or data[i+1] == "":
                if i+1 == len(data):
                    group = data[current_position:]
                elif data[i+1] == "":
                    group = data[current_position:i+1]

                # group = ["abc"]
                unique_questions = []
                for person in group:
                    # person = "abc"
                    for question in person:
                        # question = "a"
                        if question not in unique_questions:
                            # print(current_position, question)
                            unique_questions.append(question)
                            count += 1
                current_position = i + 2

    print("Part 1 - Sum of counts:", count)


def get_shared_letters_from_group(array_of_strings):
    shared_letters = create_letter_array(array_of_strings)
    # array_of_strings = ["a","b", "c"]
    # shared_letters = ["a", "b", "c"]
    letters_to_remove = []
    for string in array_of_strings:
        for letter in shared_letters:
            if letter not in string:
                letters_to_remove.append(letter)

    if len(letters_to_remove) > 0:
        for letter in letters_to_remove:
            try:
                shared_letters.remove(letter)
            except:
                continue
    return shared_letters


def create_letter_array(array_of_strings):
    letter_array = []
    for string in array_of_strings:
        for letter in string:
            if letter not in letter_array:
                letter_array.append(letter)
    return letter_array


def part2(data):
    current_position = 0
    count = 0

    for i in range(len(data)):
        if current_position <= i:
            if i+1 == len(data) or data[i+1] == "":
                if i+1 == len(data):
                    group = data[current_position:]
                elif data[i+1] == "":
                    group = data[current_position:i+1]
                
                shared_letters = get_shared_letters_from_group(group)
                count += len(shared_letters)
               
                current_position = i + 2

    print("Part 2 - Sum of counts:", count)


test_data = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]
puzzle_data = helper.readfile("2020/day6data.txt")
part1(puzzle_data)
#print(get_shared_letters_from_group(["a","b","c"]))
part2(puzzle_data)