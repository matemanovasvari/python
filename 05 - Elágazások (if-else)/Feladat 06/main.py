numberOne :int = None
numberTwo :int = None
numberThree :int = None

print("Kérek egy számot!:")
numberOne = int(input())

print("Kérek egy számot!:")
numberTwo = int(input())

print("AdjonKérek egy számot!:")
numberThree = int(input())

if (numberOne > numberTwo and numberOne > numberThree and numberTwo > numberThree):
    print(numberOne,numberTwo,numberThree)

elif (numberOne > numberTwo and numberOne > numberThree and numberThree > numberTwo):
    print(numberOne,numberThree,numberTwo)

elif (numberTwo > numberOne and numberTwo > numberThree and numberOne > numberThree):
    print(numberOne,numberThree,numberTwo)

elif (numberTwo > numberOne and numberTwo > numberThree and numberThree > numberOne):
    print(numberTwo,numberThree,numberOne)

elif (numberThree > numberOne and numberThree > numberTwo and numberTwo > numberOne):
    print(numberOne,numberThree,numberTwo)

elif (numberThree > numberOne and numberThree > numberTwo and numberOne > numberTwo):
    print(numberOne,numberThree,numberTwo)