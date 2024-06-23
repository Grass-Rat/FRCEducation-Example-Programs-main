# Get user input for the list of numbers
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in numbers.split()]

# Calculate the average, minimum, and maximum values
average = sum(numbers) / len(numbers)
minimum = min(numbers)
maximum = max(numbers)

# Print the results
print("The average is " + str(average))
print("The minimum is " + str(minimum))
print("The maximum is " + str(maximum))