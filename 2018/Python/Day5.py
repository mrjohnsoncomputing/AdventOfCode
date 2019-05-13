import helper

day = "Day5"
raw_data = open(day + "Data.txt", "r")
data = raw_data.read()
raw_data.close()

def strToArr(str):
  arr = []
  for i in range(len(str)):
    arr.append(str[i])
  #print(arr)
  return arr

def reactPolymer(string_input):
  calculating = True
  i = 0
  while calculating:
    char1 = string_input[i].lower()
    char2 = string_input[i+1].lower()
    if char1 == char2 and string_input[i] != string_input[i+1]: 
      del string_input[i]
      del string_input[i]
      if i > 0:
        i -= 1
    else:
      i += 1
    if i >= len(string_input)-1:
      calculating = False
  return len(string_input)

def reactSingleLetter(letter, string_input):
  calculating = True
  i = 0
  while calculating:
    char1 = string_input[i].lower()
    char2 = string_input[i+1].lower()
    if char1 == letter and letter == char2 and string_input[i] != string_input[i+1]: 
      del string_input[i]
      del string_input[i]
      if i > 0:
        i -= 1
    else:
      i += 1
    if i >= len(string_input)-1:
      calculating = False
  return string_input

def findBadCharacter():
  alphabet = helper.AlphabetDictionary()
  for i in alphabet:
    string_input = strToArr(data)
    string_input = helper.arrayReplace(string_input, i)
    string_input = helper.arrayReplace(string_input, i.upper())
    alphabet[i] = reactPolymer(string_input)
  return alphabet[helper.smallestDicInt(alphabet)]


def main():
  string_input = strToArr(data)
  part1 = reactPolymer(string_input)
  print("Part 1: ", part1)
  part2 = findBadCharacter()
  print("Part 2: ", part2)
