zoldsegleves: bool = False
husleves: bool = False
gyumolcsleves: bool = False
eloetel: int = None

sültcsirkecomb: bool = False
sultcsirkemell: bool = False
rakottzoldseg: bool = False
spagetti: bool = False
pizza: bool = False
foetel: str = None

rizs: bool = False
paroltzoldseg: bool = False
gyumolcs: bool = False
sultkrumpli: bool = False
salata: bool = False
kola: bool = False
koret: str = None


print("Válasszon az előételek közül!:")
print("Zöldségleves - 1")
print("Húsleves - 2")
print("Gyümölcsleves - 3")
eloetel = int(input())

if (eloetel == 1):
    zoldsegleves = True
    eloetel = "Zöldségleves"
elif (eloetel == 2):
    husleves = True
    eloetel = "Húsleves"
elif (eloetel == 3):
    gyumolcsleves = True
    eloetel = "Gyümölcsleves"
elif (eloetel == 4):
    print("Nem teljes a menü!")

print("Válasszon a főételek közül!:")
print("Sültcsirkecomb - 1")
print("Sültcsirkemell - 2")
print("Rakottzöldség - 3")
print("Spagetti - 4")
print("Pizza -5")
foetel = int(input())

if (foetel == 1):
    sultcsirkecomb = True
    foetel = "Sültcsirkecomb"
elif (foetel == 2):
    sultcsirkemell = True
    foetel = "Sültcsirkemell"
elif (foetel == 3):
    rakottzoldseg = True
    foetel = "Rakottzöldség"
elif (foetel == 4):
    spagetti = True
    foetel = "Spagetti"
elif (foetel == 5):
    pizza = True
    foetel = "Pizza"

print("Válasszon a köretek közül")
print("Rizs - 1")
print("Párolt züldség -2")
print("Gyümölcs -3")
print("Sültkrumpli - 4")
print("Saláta - 5")
print("Kóla - 6")
koret = int(input())

if (koret == 1):
    rizs = True
    koret = "Rizs"
elif (koret == 2):
    paroltzoldseg = True
    koret = "Párolt zöldség"
elif (koret == 3):
    gyumolcs = True
    koret = "Gyümölcs"
elif (koret == 4):
    sultkrumpli = True
    koret = "Sültkrumpli"
elif (koret == 5):
    salata = True
    koret = "Saláta"
elif (koret == 6):
    kola = True
    koret = "Kóla"

if (eloetel != None or foetel != None or koret != None):
    print("A menü nem kiváló!")

print(f"{eloetel}")
print(f"{foetel}")
print(f"{koret}")