# Script: iszero.py

# Prompt the user for a number
number = input("Enter a number: ")

# Try to convert the input to an integer
try:
    number = int(number)
    # Check if the number is equal to zero
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")