while True:
    try:
        digit1 = float(input("Enter first digit: "))
        break
    except ValueError:
        print("\033[1;31mPlease enter a valid number\033[0m")
math_opp = input("Enter operator: ")
while True:
    try:
        digit2 = float(input("Enter last digit: "))
        break
    except ValueError:
        print("\033[1;31mPlease enter a valid number\033[0m")

if math_opp == "+":
    result = digit1 + digit2

elif math_opp == "-":
    result = digit1 - digit2

elif math_opp == "%":
    result = digit1 % digit2

elif math_opp == "*":
    result = digit1 * digit2

elif math_opp == "/":
    result = digit1 / digit2

elif math_opp == "//":
    result = digit1 // digit2

elif math_opp == "**":
    result = digit1 ** digit2

else:
    print("404 operator" + " " + f"\033[1;31m{math_opp}\033[0m not found." + "Try again with a valid operator :)")
    result = None

if result is not None:
    print(f"\033[32mAnswer = {round(result, 3)}\033[0m")

