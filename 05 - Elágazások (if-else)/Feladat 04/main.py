firstNumber: int = None
secondNumber: int = None

print("Kérem az első számot!:")
firstNumber = int(input())

print("Kérem a második számot!:")
secondNumber = int(input())

if (firstNumber > secondNumber):
    print(f"A nagyobb szám: {firstNumber}")

elif (secondNumber > firstNumber):
    print(f"A kisebb szám: {firstNumber}")