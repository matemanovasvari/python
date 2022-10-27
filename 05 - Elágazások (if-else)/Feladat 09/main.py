x: int = None
y: int = None

print("Kérem az első számot!")
x = int(input())

print("Kérem a második számot!")
y = int(input())

if ((x % y) == 0):
    print("A második szám osztható az elsővel!")

else:
    print("A második szám nem osztható az elsővel!")