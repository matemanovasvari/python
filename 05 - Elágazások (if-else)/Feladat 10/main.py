myNumber: int = None

print("Kérek egy számot!:")
myNumber = int(input())

if (myNumber % 2 == 0 and myNumber % 3 == 0):
    print("ZIZI")
elif (myNumber % 2 == 0):
    print("BIZ")
elif (myNumber % 3 == 0):
    print("BAZ")
else:
    print("A szám semelyikkel sem osztható!")
    