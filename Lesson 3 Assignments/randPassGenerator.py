import random
import string

# Get user input for the password length and criteria
length = int(input("Enter the password length: "))
has_uppercase = input("Include uppercase letters? (yes/no): ")
has_numbers = input("Include numbers? (yes/no): ")
has_special_chars = input("Include special characters? (yes/no): ")

# Generate the password
password = ""
if has_uppercase.lower() == "yes":
    password += string.ascii_uppercase
if has_numbers.lower() == "yes":
    password += string.digits
if has_special_chars.lower() == "yes":
    password += string.punctuation
password = ''.join(random.choice(password) for _ in range(length))

# Print the password
print("The generated password is " + password)