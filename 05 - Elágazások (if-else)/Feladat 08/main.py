myNumber: int = None

print("Kérek egy számot!:")
myNumber = int(input())

if ((myNumber % 4 and myNumber % 6) == 0):
    print("A szám osztható néggyel és hattal is!")

elif ((myNumber % 4 and myNumber / 6) == 0):
    print("A szám csak néggyel osztható!")

elif ((myNumber % 6 and myNumber / 4) == 0):
    print("A szám csak hattal osztható!")

else:
    print("A szám semelyikkel sem osztható!")