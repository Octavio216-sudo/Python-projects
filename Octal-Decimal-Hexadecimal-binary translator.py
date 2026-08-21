# Ask for the number as a string (so binary/hex input works)
target_number = input("Type a number: ")

# Ask what base the input number is in
input_base = int(input("What base is your number in? (2 for binary, 8 for octal, 10 for decimal, 16 for hex): "))

# Convert the input string into a decimal integer
decimal_number = int(target_number, input_base)

# Now ask what system to translate it to
num_system = int(input("What would you like to translate it to? (2 for binary, 8 for octal, 10 for decimal, 16 for hex): "))

if num_system == 2:
    print(target_number, "in decimal is:", decimal_number)
    print(decimal_number, "in binary is:", bin(decimal_number))
elif num_system == 16:
    print(target_number, "in decimal is:", decimal_number)
    print(decimal_number, "in hexadecimal is:", hex(decimal_number))
elif num_system == 8:
    print(target_number, "in decimal is:", decimal_number)
    print(decimal_number, "in octal is:", oct(decimal_number))
elif num_system == 10:
    print(target_number, "in decimal is:", decimal_number)
