import math

a: int = None
b: int = None
menü: str = None
eredmeny: int = None

print("Kérem adja meg az a értékét!")
a = int(input())
print("Kérem adja meg a b értékét!")
b = int(input())
print("Kérem válasszon műveletet: t--terület\nk--kerület\na--átló")
menü = str(input()).lower().strip()

match menü:
    case "t":
        eredmeny = a * b
        print(eredmeny)
    case "k":
        eredmeny = 2 * (a + b)
    case "a":
        eredmeny = math.pow(a,2) + math.pow(b,2)
        print(eredmeny)