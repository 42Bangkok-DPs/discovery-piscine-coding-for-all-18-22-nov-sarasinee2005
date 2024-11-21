def multiplication_table():
    number = int(input("Enter a number"))

    for i in range(10):
        result = number * i
        print(f"{i} x {number} = {result}")

if __name__ == "_main_":
    multiplication_table()