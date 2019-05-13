day = "Day1"
raw_data = open(day + "Data.txt", "r")
data = raw_data.read()
data = data.splitlines()
raw_data.close()

def sumFreq(str, total):
    value = int(str[1:])
    if (str[0] == "+"):
        total = total + value
    elif (str[0] == "-"):
        total = total - value
    return total

def resultingFrequency(arr):
    total = 0
    for item in arr:
        total = sumFreq(item, total)
    return total

def repeatingFrequency(arr):
    totals = [0]
    total = 0
    attempts = 0
    while (True):
        for item in arr:
            total = sumFreq(item, total)
            try: 
                i = totals.index(total)
                print("Total: " + str(total) + " | Index: " + str(i))
                return total
            except ValueError:
                attempts += 1
                totals.append(total)
    #return "Not Found: " + str(attempts) + " attempts made"


test_data = ["+1", "-2", "+3", "+1", "+1", "-2"]
def main():
    print(resultingFrequency(data))
    print(repeatingFrequency(data))
