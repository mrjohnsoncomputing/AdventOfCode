import Binary as b
import time
with open("day7data.txt", "r") as datafile:
    data = [[j for j in i.split(" ") if j != "->"] for i in datafile.read().split("\n") if i]

def printObject(o, n):
        print("\n" + ("--" * n) ,n, o.value)
        print("--" * n, o.op, o.children)
        for i in range(len(o.children)):
            if isinstance(o.children[i], operation):
                printObject(o.children[i], n+1)

def countObjects(o):
    total = 0
    for i in range(len(o.children)):
            if isinstance(o.children[i], operation):
                total += 1
                total += countObjects(o.children[i])
    return total
    
class operation():
    def __init__(self, value, op, values):
        self.value = value
        self.op = op
        self.children = values

def checkChildren(op, value, new_op):
    for i in range(len(op.children)):
        if op.children[i] == value:
            op.children[i] = new_op
            return True
        elif isinstance(op.children[i], operation):
             if checkChildren(op.children[i], value, new_op):
                 return True
    return False

def buildTree(operations):
    removals = []
    for op in operations:
        found = False
        for check in operations:
            if op != check:
                found = checkChildren(check, op.value, op)
                if found:
                    removals.append(op)
                    break
                for child in check.children:
                    if isinstance(child, operation):
                        found = checkChildren(child, op.value, op)
                        if found:
                            removals.append(op)
                            break
            if found:
                break
        if found:
            break
    for r in removals:
        try:
            operations.remove(r)
        except:
            print("Not in List")

def performOp(op):
    answer = ""
    if op.op == "AND":
        answer = b.bitwiseAND(op.children[0], op.children[1])
    elif op.op == "OR":
        answer = b.bitwiseOR(op.children[0], op.children[1])
    elif op.op == "NOT":
        answer = b.complement(op.children[0])
    elif op.op == "assign":
        return op.children[0]
    elif op.op == "LSHIFT":
        answer = b.leftShift(op.children[0])
    elif op.op == "RSHIFT":
        answer = b.rightShift(op.children[0])
    else:
        print("Unknown operation")
        return
    return b.toDenary(answer)
    

def traverseTree(op):
    for i in range(len(op.children)):
        if type(op.children[i]) == str:
            try:
                op.children[i] = int(op.children[i])
            except:
                print("Can't convert", op.children[i], "to integer")
    for i in range(len(op.children)):
        if isinstance(op.children[i], operation):
            op.children[i] = traverseTree(op.children[i])
    return performOp(op)

operations = []
print("Start Data Length: ", len(data))
for d in data:
    #print(d)
    value = d[len(d)-1]
    
    if len(d) == 4:
        new_op = operation(value, d[1], [d[0], d[2]])
    elif len(d) == 3:
        new_op = operation(value, d[0], [d[1]])
    elif len(d) == 2:
        new_op = operation(value, "assign", [d[0]])
    else:
        print("Length out of range")

    if len(operations) == 0:
        print("Adding first operation", new_op.value)
        operations.append(new_op)
    else:
        found = False
        for op in operations:
            found = checkChildren(op, value, new_op)
            if found:
                break
        if not found:
            operations.append(new_op)

start = time.time()
print("Number of operations: ", len(operations))
print("Building Tree...")
for i in range(1000):
    buildTree(operations)
print("Time taken to build tree: ", time.time() - start)

##removals = []
##for op in operations:
##    for check in operations:
##        if op != check:
##            found = checkChildren(check, op.value, op)
##            if found:
##                removals.append(op)
##                break
##
##            
##for r in removals:
##        try:
##            operations.remove(r)
##        except:
##            print("Not in List")
    

total = 0
for i in range(len(operations)):
    total += 1
    total += countObjects(operations[i])
    #printObject(operations[i], 1)
print("Number of operations: ", len(operations))
print("Total operation objects: ", total)

traverseTree(operations[1])

#lw ly lx lz ma a            
