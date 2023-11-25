import sys

# Prompt Start
print("This is a calculator based on Python, please enter Y to start calculating, enter N to exit.")

# Read the input
usr_input = input()

# Yes or No?
if usr_input == 'Y':
    # user start to cal
    print("user start to cal")
elif usr_input == 'N':
    sys.exit(0)


num1 = float(input("Please enter the first number："))
operator = input("Please enter an operator （+,-,*,/）：")
num2 = float(input("Please enter the second number："))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator =="/":
    result = num1 / num2
else:
    result = "Please enter the correct operator"
print("The result is：", result)

while True:
    answer = input("Do you want to continue? (yes/no) ")
    if answer.lower() == 'yes':
        num1 = float(input("Please enter the first number："))
        operator = input("Please enter an operator （+,-,*,/）：")
        num2 = float(input("Please enter the second number："))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = "Please enter the correct operator"
        print("The result is：", result)

    else:
        break
