

def calculate(num1, num2, operator):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

calculating = True

while calculating:

    num1 = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    result = calculate(num1, num2, operator) 
    print(result)

    keep_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if keep_calculating != "y":
        calculating