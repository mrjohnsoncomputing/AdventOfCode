# How many bag colors can eventually contain at least one shiny gold bag?
import helper
print("Advent of Code: Day 7")

class Bag:
    def __init__(self, bag_colour="", rules=[]):
        self.parent = ""
        self.children = {}
        self.colour = bag_colour
        self.rules = rules        

    def is_this_my_child(self, bag):
        if self.i_already_have_that_child(bag) == False:
            for rule in self.rules:
                for i in range(len(rule)):
                    quantity = rule[0]
                    colour = rule[1] + " " + rule[2]
                    if bag.colour == colour:
                        self.children[bag.colour] = bag
                        return True

            #for child in self.children:
            #    self.children[child].is_this_my_child(bag)
        else:
            return False
    
    def i_already_have_that_child(self, bag):
        if self.children.get(bag.colour) != None:
            return True
        else:
            return False

    def update_child(self, bag):
        if self.children[bag.colour] != None:
            self.children[bag.colour] = bag
    
    def check_children(self, TARGET):
        
        if self.children == {}:
            return False

        if self.children.get(TARGET) != None:
            return True
        
        contains_target = False
        for child in self.children:
            contains_target = self.children[child].check_children(TARGET)
            if contains_target:
                return True
        return contains_target           

    def print(self, number=0):
        print("#" * number, self.colour)
        number += 1
        for child in self.children:
            child.print(number)


class Luggage:
    def __init__(self, data):
        self.count = 0
        self.raw_data = data
        self.contains_target = []
        self.bags = []
        self.TARGET = "shiny gold"
        self.create_bags(self.raw_data)
        print("Created Bags")
        self.organise_bags()
        

    def create_bags(self, data):
        for item in data:
            bag_data = item.split(" ")
            bag_colour = bag_data[0] + " " + bag_data[1]
            rules = []
            for i in range(4, len(bag_data)):
                numbers = ["0","1","2","3","4","5","6","7","8","9"]
                if bag_data[i] in numbers:
                    rule = [bag_data[i], bag_data[i+1], bag_data[i+2]]
                    rules.append(rule)
            bag = Bag(bag_colour, rules)
            self.bags.append(bag)
            # ["light", "red", "bags", "contain", "1", "bright", "white", "bag,", "2", "muted yellow bags."]

    def print_bags(self):
        for bag in self.bags:
            bag.print()

    def organise_bags(self):
        length = len(self.bags)
        for i in range(0, length):
            parent = self.bags[i]
            
            for j in range(0, length):    
                potential_child = self.bags[j]
                is_child = parent.is_this_my_child(potential_child)

    def find_target(self):
        for bag in self.bags:
            self.count += bag.check_children(self.TARGET)
            #print(bag.colour, self.count)
        print(self.TARGET, self.count)
    

test_data = [
    "bright white bags contain 1 shiny gold bag.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "dotted black bags contain no other bags.",
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "faded blue bags contain no other bags.",
    "clear plastic bags contain 1 dark orange bag.",
    ]


# So, in this example, the number of bag colors that can eventually 
# contain at least one shiny gold bag is 4.
puzzle_data = helper.readfile("2020/day7data.txt")
luggage = Luggage(puzzle_data)
print("Created Luggage")
luggage.find_target()
#luggage.print_bags()
