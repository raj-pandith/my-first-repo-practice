try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))   
    op= input("Enter operator + * - /:")
    if op == "+":
        print("result: " ,  num1 + num2)
    elif op == "*":
        print("result: " ,  num1 * num2)
    elif op == "-":
        print("result: " ,  num1 - num2)
    elif op == "/":
        print("result: " ,  num1 / num2)
    else:
        print("Invalid operator")
except ValueError:
    print("Please enter only numbers")
except  ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("Thank you for using the calculator!")
        