number = input("Give me a number: ")

if '.' in number:
    try:
        
        float_number = float(number)
        print("This number is a decimal.")
    except ValueError:
        print("Invalid input.")
else:
    try:
        
        int_number = int(number)
        print("This number is an integer.")
    except ValueError:
        print("Invalid input.")
