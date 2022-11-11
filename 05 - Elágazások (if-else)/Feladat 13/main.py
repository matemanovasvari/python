myNumber: int = None

print("Kérek egy számot!:")
myNumber = int(input())

if (myNumber >= 0 and myNumber <= 9):
    print("A szám egyjegyú!")
elif (myNumber >= 10 and myNumber <= 99):
    print("A szám kétjegyű!")
elif (myNumber >= 100 and myNumber <= 999):
    print("A szám háromjegyű!")