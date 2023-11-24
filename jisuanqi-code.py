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


