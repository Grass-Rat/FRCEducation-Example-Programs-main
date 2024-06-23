# Get user input for length and width
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Calculate the area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Print the results
print("The area is " + str(area))
print("The perimeter is " + str(perimeter))