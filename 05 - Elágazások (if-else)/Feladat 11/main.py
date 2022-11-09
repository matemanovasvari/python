myNumber: int = None

print("Kérek egy számot!:")
myNumber = int(input())

if (myNumber % 2 == 0):
    print("A szám páros!")
else:
    print("A szám páratlan!")

if (myNumber < 0):
    print("A szám negatív!")
else:
    print("A szám pozitív!")

if (myNumber % 5 == 0):
    print("A szám osztható öttel!")
else: 
    print("A szám nem osztható öttel!")