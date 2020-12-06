# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
import helper

print("Advent of Code: Day 4")

def check_passport_fields(passport):
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in passport_fields:
        if field not in passport:
            return False
    return passport

def check_passports_have_valid_fields(passports):
    valid_passports = []
    for passport in passports:
        isValid = check_passport_fields(passport)
        if isValid != False:
            valid_passports.append(passport)
    return valid_passports

def check_passports_have_valid_data(passports):
    valid_passports = []
    for passport in passports:
        isValid = check_passport_data(passport)
        if isValid != False:
            valid_passports.append(passport)
    return valid_passports

def check_passport_data(passport):
    for field in passport:
        if field == "byr":
            byr = int(passport[field])
            if byr > 2002 or byr < 1920:
                return False
        elif field == "iyr":
            iyr = int(passport[field])
            if iyr > 2020 or iyr < 2010:
                return False
        elif field == "eyr":
            eyr = int(passport[field])
            if eyr > 2030 or eyr < 2020:
                return False
        elif field == "hgt":
            hgt = passport[field]
            if hgt[0:len(hgt)-2] == "":
                return False
            number = int(hgt[0:len(hgt)-2])
            if "cm" in hgt:
                # If cm, the number must be at least 150 and at most 193.
                if number < 150 or number > 193:
                    return False
            elif "in" in hgt:
                # If in, the number must be at least 59 and at most 76.
                if number < 59 or number > 76:
                    return False
            else:
                return False
        elif field == "hcl":
            hcl = passport[field]
            if hcl[0] != "#" or len(hcl) != 7:
                return False
            valid_letters = ["#", "a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for letter in hcl:
                if letter not in valid_letters:
                    return False
        elif field == "ecl":
            ecl = passport[field]
            valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if ecl not in valid_colours:
                return False
        elif field == "pid":
            pid = passport[field]
            if len(pid) != 9:
                return False
        elif field == "cid":
            continue
        else:
            print("Unknown field: " + field)
    return True

def make_passport(passport_data):
    passport = {}
    for line in passport_data:
        entry = line.split(" ")
        for item in entry:
            if item != "":
                field = item.split(":")
                # print(field)
                passport[field[0]] = field[1]
    return passport

def make_passports(raw_data):
    passports = []
    current_position = 0
    for i in range(len(raw_data)):
        if i >= current_position:
            if (i == len(raw_data)-1 or (raw_data[i+1] == "" and raw_data[i] != "")):
                passport_data = []
                for j in range(current_position, i+1):
                    passport_data.append(raw_data[j])
                
                passport = make_passport(passport_data)
                passports.append(passport)
                current_position = i+2
    return passports

puzzle_data = helper.readfile("2020/day4data.txt")
test_data = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"]

# passport = {
#     "ecl": "gry",
#     "pid": "860033327",
#     "byr": "1999"
# }

passports = make_passports(puzzle_data)
passports = check_passports_have_valid_fields(passports)
print("Part 1: There are {} valid passports".format(len(passports)))
passports = check_passports_have_valid_data(passports)
print("Part 2: There are {} valid passports".format(len(passports)))