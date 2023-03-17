from colorama import init, Fore, Style
init()
"""
required modules
"""


class Calculator:
    """
    To calculate using different operations at a time
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
        :return: the summation of both digits
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

# first digit input
while True:
    try:
        digit1 = float(input("Enter first number: "))
        break
    except ValueError:
        print(Fore.RED + "Please enter a valid number" + Style.RESET_ALL)

# operator input
while True:
    math_opp = input("Enter operator(" + Fore.BLUE + "+, -, /, *, **, %, //" + Style.RESET_ALL + ")")
    if math_opp:
        break
    else:
        print(Fore.RED + "math operator cannot be empty" + Style.RESET_ALL)

# second digit input
while True:
    try:
        digit2 = float(input("Enter last number: "))
        break
    except ValueError:
        print(Fore.RED + "Please enter a valid number" + Style.RESET_ALL)

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
    print(Fore.RED + "404 operator" + Style.RESET_ALL + Fore.YELLOW + f"{math_opp}" + Style.RESET_ALL + Fore.RED + "not found\n" +
          "Try again with a valid operator" + Style.RESET_ALL)
    result = None

if result is not None:
    print(Fore.GREEN + f"Answer = {round(result, 3)}" + Style.RESET_ALL)

# math_history = input("To see math history press \033[1;34menter\033[0m")
# if math_history:
#     for calculation in calculator.history:
#         print(calculation)
