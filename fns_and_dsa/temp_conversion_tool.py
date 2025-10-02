FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        temperature = int(input("Enter the temperature to convert: "))
    except ValueError:
        raise Exception("Invalid temperature. Please enter a numeric value.")
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    result = None
    temp = None
    temperature = float(temperature)
    if temperature_unit == "F":
        result = f"{convert_to_celsius(temperature)}°C"
        temp = f"{temperature}°F"
    elif temperature_unit == "C":
        result = f"{convert_to_fahrenheit(temperature)}°F"
        temp = f"{temperature}°C"
    else:
        print("Enter a valid temperature unit")

    if result:
        print(f"{temp} is {result}")

if __name__ == "__main__":
    main()