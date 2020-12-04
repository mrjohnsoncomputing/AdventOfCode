# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
import helper

print("Advent of Code: Day 3")

def update_position(position, max_width, x_increment, y_increment):
    position[0] = position[0] + y_increment
    position[1] = position[1] + x_increment
    if position[1] >= max_width:
        position[1] = position[1] - max_width
    return position

def has_collided_with_tree(position, map):
    x = position[1]
    y = position[0]
    # print(map[y][x])
    if map[y][x] == "#":
        return True
    else:
        return False

def part1(map_data, slope):
    width = len(map_data[0])
    height = len(map_data)
    trees_hit = 0
    current_position = [0,0]

    while current_position[0] < height:
        trees_hit += has_collided_with_tree(current_position, map_data)
        current_position = update_position(current_position, width, slope[0], slope[1])

    print("Part 1, Trees Hit: " + str(trees_hit))
    return trees_hit

def part2(map_data, slopes):
    tree_counter = 1
    for slope in slopes:
        tree_counter *= part1(map_data, slope)
    print("Part 2, Trees Hit:", tree_counter)

data = helper.readfile("2020/day3data.txt")
slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]]

test_data = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#" ]


part1(data, slopes[1])
part2(data, slopes)