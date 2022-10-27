myNumber: int = None

print("Kérek egy számot!:")
myNumber = int(input())

if ((myNumber % 2 and myNumber % 3) == 0):
    print("A szám osztható kettővel és hárommal is!")

elif ((myNumber % 2 and myNumber / 3) == 0):
    print("A szám csak kettővel osztható!")

elif ((myNumber % 2 and myNumber / 3) == 0):
    print("A szám csak hárommal osztható!")

else:
    print("A szám semelyikkel sem osztható!")