def toDenary(binary):
    binary = str(binary)
    exponent = 1
    denary = 0
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == "1":
            denary += exponent
        exponent *= 2
    return denary

def fromDenary(denary):
    exponent = 1
    while denary > exponent:
        exponent *= 2
    exponent = int(exponent/2)
    binary = ""
    while exponent > 0.5:
        if denary >= exponent:
            binary += "1"
            denary -= int(exponent)
        else:
            binary += "0"
        exponent/=2
    return binary

def complement(denary):
    binary = fromDenary(denary)
    new_binary = ""
    for bit in range(len(binary)):
        if binary[bit] == "0":
            new_binary += "1"
        else:
            new_binary += "0"
    return new_binary


def leftShift(denary):
    return denary * 2

def rightShift(denary):
    return denary/2

def getLonger(binary1, binary2):
    if len(binary1) > len(binary2):
        return [binary1, binary2]
    else:
        return [binary2, binary1]

def bitwiseAND(denary1, denary2):
    nums = getLonger(fromDenary(denary1), fromDenary(denary2))
    binary1 = nums[0]
    binary2 = nums[1]
    result = ""
    while len(binary1) > len(binary2):
        binary2 = "0" + binary2
    for i in range(len(binary1)):
        if binary1[i] == binary2[i] and binary1[i] == "1":
            result += "1"
        else:
            result += "0"
    return result

def bitwiseOR(denary1, denary2):
    nums = getLonger(fromDenary(denary1), fromDenary(denary2))
    binary1 = nums[0]
    binary2 = nums[1]
    result = ""
    while len(binary1) > len(binary2):
        binary2 = "0" + binary2
    for i in range(len(binary1)):
        if binary1[i] == "1" or binary2[i] == "1":
            result += "1"
        else:
            result += "0"
    return result











        
