import re
with open("day5data.txt", "r") as datafile:
    data = [i.strip() for i in datafile.read().split("\n") if i]

def isNice1(s):
    lastchar = ""
    blank = ""
    v = 0
    dbl = False
    vowels = ["a", "e", "i", "o", "u"]
    banned = ["ab", "cd", "pq", "xy"]
    for c in s:
        try:
            test = banned.index(lastchar+c)
            return False
        except:
            blank = ""
        try:
            test = vowels.index(c)
            v += 1
        except:
            blank = ""
        try:
            test = string.index(c+c)
            dbl = True
        except:
            blank = ""
                    
        lastchar = c
    if v >= 3 and dbl:
        return True
    else:
        return False

def part1():
    n = 0
    for string in data:
        if isNice1(string):
            n+=1
    print(n)

def isNice(s):
    couples = False
    sandwiches = False
    #print(s)
    for i in range(len(s)-1):
        couple = s[i:i+2]
        for j in range(i+2,len(s)-1):
            c = s[j:j+2]
            #print(couple, c)
            if c == couple:
                couples = True
        if i < len(s)-2:
            sandwich = s[i:i+3]
            if sandwich[0] == sandwich[2]:
                sandwiches = True
    return couples and sandwiches
    
def part2():
    n = 0
    for string in data:
        if isNice(string):
            n+=1
    print(n)

part2()
