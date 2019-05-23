import Binary as b
import time
with open("day7data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "->"] for i in datafile.read().split("\n") if i]

codes = {}
    
for i in range(len(data)):
    key = data[i][len(data[i])-1]
    value = data[i][0:len(data[i])-1]
    codes[key] = value

def operate(key, debug=False):
    l = len(codes[key])
    n1 = codes[key][l-1]
    n2 = 0
    #print("Key:", key, "n1:", n1)
    try:
        codes[key][l-1] = float(codes[key][l-1])
        n1 = codes[key][l-1]
        #n1 = float(n1)
    except ValueError:
        codes[key][l-1] = operate(codes[key][l-1], debug)
        n1 = codes[key][l-1]
        #n1 = operate(n1)
    except:
        print("Uncaught Exception at n1")
    if l == 1:
        return n1
    elif l == 2:
        return b.toDenary(b.complement(n1))
    elif l == 3:
        try:
            codes[key][0] = float(codes[key][0])
            n2 = codes[key][0]
            #n2 = float(n2)
        except ValueError:
            codes[key][0] = operate(codes[key][0], debug)
            n2 = codes[key][0]
            #n2 = operate(n2, debug)
        except:
            print("Uncaught exception at n2!")
    else:
        print("Unhandled Length")
    #print("Calculation\nKey:", key, "n1:", n1, "n2:", n2, "\n")
    #print(codes[key])
    if codes[key][1] == "OR":
        if debug == True:
            print("OR", key, codes[key], n1, n2, b.toDenary(b.bitwiseOR(n2,n1)))
        return b.toDenary(b.bitwiseOR(n2,n1))
    elif codes[key][1] == "AND":
        if debug == True:
            print("AND", key, codes[key], n1, n2, b.toDenary(b.bitwiseAND(n2,n1)))
        return b.toDenary(b.bitwiseAND(n2,n1))
    elif codes[key][1] == "LSHIFT":
        if debug == True:
            print("LSHIFT", key, codes[key], n1, n2, b.leftShift(n2,n1))
        return b.leftShift(n2,n1)
    elif codes[key][1] == "RSHIFT":
        if debug == True:
            print("RSHIFT", key, codes[key], n1, n2, b.rightShift(n2,n1))
        return b.rightShift(n2,n1)
    else:
        print("Bad Operator for l=3")
def main(debug=False):
    start = time.time()
    print("Beginning Program...")
    print(operate("a", debug))
    print("Program completed in:", time.time() - start)
