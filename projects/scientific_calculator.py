#scientific calculator
import math
def calculator():
    while True:

        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
        choice = input("""
        Choose operation:
        +
        -
        *
        /
        %
        sqrt
        power
        sin
        cos
        tan
        log
        Enter choice:
        """)

        if choice == "+":
            result = num1+num2
        elif choice == "-":
            result = num1-num2
        elif choice == "*":
            result = num1*num2
        elif choice == "%":
            result = num1%num2
        elif choice == "/":
            if num2 != 0:
                result = num1/num2
            else:
                result = "Cannot divide by zero"
        elif choice == "sqrt":
            result = math.sqrt(num1)
        elif choice == "power":
            result = num1 ** num2
        elif choice == "sin":
            result = math.sin(math.radians(num1))
        elif choice == "cos":
            result = math.cos(math.radians(num1))
        elif choice == "tan":
            result = math.tan(math.radians(num1))
        else:
            result = "invalid operation"

        print("Result =", result)
        again = input("Do you want another calculation? y/n: ")

        if again != "y":
            break

calculator()