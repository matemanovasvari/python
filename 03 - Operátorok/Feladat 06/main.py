firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None
result: float = None

print("Kérem az első számot!:")
firstNumber = int(input())

print("Kérem a második számot!:")
secondNumber = int(input())

print("Kérem a harmadik számot!:")
thirdNumber = int(input())

result = ((firstNumber + 0.5) * (secondNumber - 0.7)) % thirdNumber

print(f"Az eredmény: {result:1.2f}")