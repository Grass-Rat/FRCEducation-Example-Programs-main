def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input for the number
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print("The factorial of " + str(num) + " is " + str(result))