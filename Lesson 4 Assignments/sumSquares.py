def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

# Get user input for the list of numbers
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in numbers.split()]

# Calculate the sum of squares
result = sum_of_squares(numbers)

# Print the result
print("The sum of squares is " + str(result))