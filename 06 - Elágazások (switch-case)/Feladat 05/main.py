r1: int = None
r2: int = None
resistor: int = None
kapcs: str = None

print("Kérem az egyik ellenállás értékét!")
r1 = int(input())
print("Kérem a ellenállás értékét!")
r2 = int(input())
print("Milyen a kapcsolás? soros -- S, s párhuzamos -- P, p")
kapcs = str(input()).strip().lower()

match kapcs:
    case 'p' | 'P':
        resistor = (r1 + r2) / (r1 * r2)
        print(resistor)
    case 's' | 'S':
        resistor = r1 + r2
        print(resistor)