import os

def op(num1,operation,num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "**":
        return num1 ** num2
    
while True:
    print("Enter an equation:")
    equation = input(">>>")
    if "clear" in equation or "Clear" in equation:
        os.system("cls")
    else:
        equation = list(equation.split(" "))
        print("{0} {1} {2} = {3}".format(equation[0],equation[1],equation[2],op(equation[0],equation[1],equation[2])))
