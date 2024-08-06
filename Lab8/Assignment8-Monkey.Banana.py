i = 0


def Monkey_go_box(monkey_location, box_location):
    global i
    i += 1
    print(f"Step {i}: Monkey at {monkey_location} goes to {box_location}")


def Monkey_move_box(box_location, banana_location):
    global i
    i += 1
    print(f"Step {i}: Monkey moves the box from {box_location} to {banana_location}")


def Monkey_on_box():
    global i
    i += 1
    print(f"Step {i}: Monkey climbs up the box")


def Monkey_get_banana():
    global i
    i += 1
    print(f"Step {i}: Monkey picks the banana")


codeIn = input("Enter the locations of the monkey, banana, and box: ")
codeInList = codeIn.split()

monkey_location = codeInList[0]
banana_location = codeInList[1]
box_location = codeInList[2]

print("The steps are as follows:")

Monkey_go_box(monkey_location, box_location)
Monkey_move_box(box_location, banana_location)
Monkey_on_box()
Monkey_get_banana()
