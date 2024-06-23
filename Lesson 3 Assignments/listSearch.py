# Get user input for the list of numbers and the target value
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in numbers.split()]
target = float(input("Enter the target value: "))

# Find the first occurrence of the target value
for i, num in enumerate(numbers):
    if num == target:
        print("The target value is at index " + str(i))
        break
    else:
        print("The target value is not in the list")