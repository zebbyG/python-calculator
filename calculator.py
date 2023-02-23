class Calculator:
    """
    To calculate using different opperations at a time
    """
    def __init__(self):
        """
        direct initializing attribute history
        """
        self.history = []

    def add(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: the sumation of both digits
        """
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: the substraction of both digits
        """
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: the multiplication of both digits
        """
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result

    def divide(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: the division of both digits
        """
        result = x / y
        self.history.append(f"{x} / {y} = {result}")
        return result

    def power(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: x multiplying itself as many times as y
        """
        result = x ** y
        self.history.append(f"{x} ** {y} = {result}")
        return result

    def modular(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: the remainder after both digits are divided
        """
        result = x % y
        self.history.append(f"{x} % {y} = {result}")
        return result

    def nearest_whole_number(self, x, y):
        """
        :param x: first digit
        :param y: second digit
        :return: the nearest whole number after both digits are divided
        """
        result = x // y
        self.history.append(f"{x} // {y} = {result}")
        return result


calculator = Calculator()

while True:
    try:
        digit1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("\033[1;31mPlease enter a valid number\033[0m")
math_opp = input("Enter operator(\033[1;34m+, -, /, *, **, %, //\033[0m): ")
while True:
    try:
        digit2 = float(input("Enter last number: "))
        break
    except ValueError:
        print("\033[1;31mPlease enter a valid number\033[0m")

if math_opp == "+":
    result = calculator.add(digit1, digit2)

elif math_opp == "-":
    result = calculator.subtract(digit1, digit2)

elif math_opp == "%":
    result = calculator.modular(digit1, digit2)

elif math_opp == "*":
    result = calculator.multiply(digit1, digit2)

elif math_opp == "/":
    result = calculator.divide(digit1, digit2)

elif math_opp == "//":
    result = calculator.nearest_whole_number(digit1, digit2)

elif math_opp == "**":
    result = calculator.power(digit1, digit2)

else:
    print(f"\033[1;31m404 operator {math_opp}\033[0m not found." +
          "Try again with a \033[1;32m""valid operator :)\033[0m")
    result = None

if result is not None:
    print(f"\033[32mAnswer = {round(result, 3)}\033[0m")

math_history = input("To see math history press \033[1;34menter\033[0m")
if math_history:
    for calculation in calculator.history:
            print(calculation)
