x: int = None
y: int = None
z: int = None

print("Kérek egy számot!:")
x = int(input())
print("Kérek egy számot!:")
y = int(input())
print("Kérek egy számot!:")
z = int(input())

if (x % y == 0 and x % z == 0):
    print("Mindkettővel osztható!")
elif (x % y == 0):
    print("Csak y-nal osztható!")
elif (x % z == 0):
    print("Csak x-el osztható!")
else:
    print("A szám semelyikkel sem osztható!")