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


num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符 （+,-,*,/）：")
num2 = float(input("请输入第二个数字："))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator =="/":
    result = num1 / num2
else:
    result = "无效运算，请输入正确的运算符"
print("结果：", result)