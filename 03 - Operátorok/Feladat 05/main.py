firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None
forthNumber: int = None
result: float = None

print("Kérem az első számot!:")
firstNumber = int(input())

print("Kérem a második számot!:")
secondNumber = int(input())

print("Kérem a harmadik számot!:")
thirdNumber = int(input())

print("Kérem a negyedik számot!:")
forthNumber = int(input())

result = (firstNumber + secondNumber) / (thirdNumber - forthNumber)

print(f"Az eredmény: {result}")