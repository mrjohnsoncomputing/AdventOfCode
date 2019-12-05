import time

MIN = 272091
MAX = 815432



def has_double(string):
    for j in range(10):
        if str(j) * 2 in string:
            return True
            break
    return False


def has_increasing(string):
    last = []
    for k in range(len(string)):
        for l in range(len(last)):
            if int(string[k]) < last[l]:
                return False
        last.append(int(string[k]))
    return True


def separate_doubles(string):
    start = 0
    end = 1
    groups = []
    group = ""
    while end < len(string):
        if len(group) == 0:
            group = string[start]
        elif group[0] == string[end]:
            group += string[end]
            end += 1
        else:
            #print("String: {}\nSubstring: {}".format(string, group))
            #time.sleep(1)
            groups.append(group)
            group = ""
            start = end
            end = start + 1

    if start != len(string):
        #print("String: {}\nSubstring: {}".format(string, group))
        groups.append(string[start:end])
    return groups


def valid_doubles(string):
    doubles_array = separate_doubles(string)
    doubles = 0
    aboves = 0
    for double in doubles_array:
        if len(double) == 2:
            doubles += 1
        elif len(double) > 2:
            aboves += 1
    if aboves > 0 and doubles == 0:
        return False
    else:
        return True


def main():
    valid_day1 = []
    valid_day2 = []
    for i in range(MIN, MAX):

        string = str(i)

        if has_double(string):

            if has_increasing(string):
                valid_day1.append(string)

                if valid_doubles(string):
                    valid_day2.append(string)

    print("Day 1 Answer: {}\nDay 2 Answer: {}".format(len(valid_day1), len(valid_day2)))


main()
