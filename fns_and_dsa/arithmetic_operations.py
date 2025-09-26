def perform_operation(num1: float, num2: float, operation: str):
    result = None
    match (operation):
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        
        case "multipy":
            result = num1 * num2

        case "divide":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2

    return result


