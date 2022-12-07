weekDay: int = None

print("Hanyadik napja van a hétnek?:")
weekDay = int(input())

match weekDay:
    case 1:
        print("Hétfő")
    case 2:
        print("Kedd")
    case 3:
        print("Szerda")
    case 4:
        print("Csütörtök")
    case 5:
        print("Péntek")
    case 6:
        print("Szombat")
    case 7:
        print("Vasárnap")
    case _:
        print("Nincs ilyen nap!!!")