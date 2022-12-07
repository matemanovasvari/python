math: str = None
firstNumber: int = None
secondNumber: int = None
result: int = None

print("Kérem az első számot!")
firstNumber = int(input())
print("Kérem a második számot!")
secondNumber = int(input())
print("Válassz műveltet +,-,*,/")
math = str(input())

match math:
    case "+":
        result = firstNumber + secondNumber
        print(result)
    case "-":
        result = firstNumber - secondNumber
        print(result)
    case "*":
        result = firstNumber * secondNumber
        print(result)
    case "/":
        result = firstNumber / secondNumber
        print(result)
    case _:
        print("Nincs ilyen művelet!!!")