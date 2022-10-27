firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None
result: int = None

print("Kérem az első számot!:")
firstNumber = int(input())

print("Kérem a második számot!:")
secondNumber = int(input())

print("Kérem a harmadik számot!:")
thirdNumber = int(input())

result = (firstNumber - secondNumber) * thirdNumber

print(f"Az eredmény: {result}")