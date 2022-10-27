weight: float = None
height: float = None
tti: float = None

weight = float(input("Kérem a testtömegét!:"))
height = float(input("Kérem a magasságát(méter)!:"))

tti = weight / height**2

print(f"{tti:1.2f}")

if tti <= 16:
    print("Az ön testsúlyosztálya:\nsúlyos soványság")

elif tti > 16 and tti <= 17:
    print("Az ön testsúlyosztálya:\nmérsékelt soványság")

elif tti > 17 and tti <= 18.5:
    print("Az ön testsúlyosztálya:\nenyhe soványság")

elif tti > 18.5 and tti <= 25:
    print("Az ön testsúlyosztálya:\nnormális testsúly")

elif tti >  25 and tti <= 30:
    print("Az ön testsúlyosztálya:\ntúlsúlyos")

elif tti > 30 and tti <= 35:
    print("Az ön testsúlyosztálya:\nI. fokú elhízás")

elif tti > 35 and tti <= 40:
    print("Az ön testsúlyosztálya:\nII. fokú elhízás")

else:
    print("Az ön testsúlyosztálya:\nIII. fokú elhízás")