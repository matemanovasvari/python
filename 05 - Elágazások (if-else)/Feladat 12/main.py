myNumber: int = None

print("Kérek egy számot!")
myNumber = int(input())

if ((myNumber >10 and myNumber <20) or (myNumber > -20 and myNumber < -10)):
    print("A szám a tartományban van!")

else: print("A szám nincs a tartományban!")