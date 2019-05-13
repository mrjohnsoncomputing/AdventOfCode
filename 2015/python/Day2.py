with open("day2data.txt", "r") as datafile:
    data = [[int(j) for j in i.split("x") ] for i in datafile.read().split("\n") if i] 

def getWrappingPaper():
    answer = 0
    for dims in data:
        w=dims[0] * dims[1] * 2
        h=dims[1] * dims[2] * 2
        l=dims[0] * dims[2] * 2
        answer += w+h+l+int(min([w/2,h/2,l/2]))
    print(answer)

def getRibbon():
    answer = 0
    for dims in data:
        answer += dims[0] * dims[1] * dims[2]
        dims.remove(max(dims))
        answer += dims[0]*2 + dims[1]*2
    print(answer)
