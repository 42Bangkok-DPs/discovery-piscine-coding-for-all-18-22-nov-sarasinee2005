num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

# Calculate the multiplication result
result = num1 * num2

# Display the multiplication result
print(f"{num1} x {num2} = {result}")

# Determine if the result is positive, negative, or zero
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")