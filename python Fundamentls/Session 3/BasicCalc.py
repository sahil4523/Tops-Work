num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
oprtn = input("Enter operator (+, -, *, /): ")

if oprtn == "+":
    print("Result =", num1 + num2)
elif oprtn == "-":
    print("Result =", num1 - num2)
elif oprtn == "*":
    print("Result =", num1 * num2)
elif oprtn == "/":
    print("Result =", num1 / num2)
else:
    print("Invalid operator")