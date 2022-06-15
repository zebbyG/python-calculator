digit1 = float(input("Enter first digit: "))
mathopp = input("Enter operator: ")
digit2 = float(input("Enter last digit: "))
if mathopp == '+':
    print(digit1 + digit2)

elif mathopp == '-':
    print(digit1 - digit2)

elif mathopp == '%':
    print(digit1 % digit2)

elif mathopp == '*':
    print(digit1 * digit2)

elif mathopp == '/':
    print(digit1 / digit2)

elif mathopp == '//':
    print(digit1 // digit2)

elif mathopp == '**':
    print(digit1 ** digit2)

else:
    print("404 operator not found. Try again with a different opperator :)")
