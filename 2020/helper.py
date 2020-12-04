def readfile(filename):
    with open(filename, "r") as file:
        data = file.read()
    data = data.split("\n")
    return data