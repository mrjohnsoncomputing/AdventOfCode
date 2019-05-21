print("Welcome to data file creator 5000, Advent of Code edition.")
while True:
    day = input("Enter Day: ")
    try:
        if int(day) > 31 or int(day) < 0:
            print("Invalid day, please try again")
        break
    except ValueError:
        print("Please enter a valid day number")

finished = ""
data = ""
while finished != "y":
    finished = input("Enter Data:\n")
    if finished == "y":
        break
    data += "\n"+finished
    print("Finished: ", finished)
    
filename = "day" + day + "data.txt"
with open(filename, "w") as file:
    file.write(data)
print("Thanks for using file creator 5000")
