num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = "The result is: "

match operation:
    case "+":
        result += str(num1 + num2) + "."
    case "-":
        result += str(num1 - num2) + "."
    case "*":
        result += str(num1 * num2) + "."
    case "/":
        if num2 != 0:
            result += str(num1 / num2) + "."
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operation."

print(result)
