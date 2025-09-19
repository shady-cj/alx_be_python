num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# change the result to be printed at the end

match operation:
    case "+":
        result = str(num1 + num2) + "."
    case "-":
        result = str(num1 - num2) + "."
    case "*":
        result = str(num1 * num2) + "."
    case "/":
        if num2 != 0:
            result = str(num1 / num2) + "."
        else:
            error = "Cannot divide by zero."
    case _:
        error = "Invalid operation."

if error:
    print(error)
else:
    print(f"The result is {result}.")
