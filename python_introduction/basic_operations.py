number1 = 10
number2 = 5
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
output = lambda op, x, y, result: f"{op} of {x} and {y} is {result}"
print(output("Addition", number1, number2, sum))
print(output("Substraction", number1, number2, difference))
print(output("Multiplication", number1, number2, product))
