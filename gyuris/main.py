from cmath import sqrt
import math


a: int=None
b: int=None
c: int=None
x1: int=None
x2: int=None

print("Kérem adja meg az értéket")
a=int(input())

print("Kérem adja meg az értéket")
b=int(input())

print("Kérem adja meg az értéket")
c=int(input())

x1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)1

print(f"A másodfokú egyenlet két megoldása {x1} és {x2}")

