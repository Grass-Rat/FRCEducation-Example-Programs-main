# Get user input for unit and value
unit = input("Enter the unit (inches or feet): ")
value = float(input("Enter the value: "))

# Convert the unit
if unit.lower() == "inches":
    converted_value = value / 12
    print(str(value) + " inches is equal to " + str(converted_value) + " feet")
elif unit.lower() == "feet":
    converted_value = value * 12
    print(str(value) + " feet is equal to " + str(converted_value) + " inches")
else:
    print("Error: Invalid unit!")