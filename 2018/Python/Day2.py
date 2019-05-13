day = "Day2"
raw_data = open(day + "Data.txt", "r")
data = raw_data.read()
data = data.splitlines()
raw_data.close()

def parseString(s):
    results = {}
    for i in range(len(s)):
        letter = s[i]
        if (letter in results):
            results[letter] += 1
        else:
            results[letter] = 1
    return results

def parseLetters(d):
    key_bin = []
    for key in d:
        if d[key] != 2 and d[key] != 3:
            key_bin.append(key)
    for i in range(len(key_bin)):
        del d[key_bin[i]]
    return d

def getChecksum():
    twos = 0
    threes = 0
    for d in data:
        count2 = False
        count3 = False
        letter_set = parseString(d)
        set = parseLetters(letter_set)
        for key in set:
            if set[key] == 2 and count2 == False:
                twos += 1
                count2 = True
            elif set[key] == 3 and count3 == False:
                threes += 1
                count3 = True
    print(twos* threes)

def checkTwoBoxIds(id1, id2):
    similarity = 0
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            similarity += 1
    if (len(id1) - similarity == 1):
        return True
    else:
        return False

def getBoxIds():
    for d in data:
        for i in range(1,len(data)):
            if (checkTwoBoxIds(d, data[i])):
                return [d, data[i]]


def main():
    getChecksum()
    print(getBoxIds())