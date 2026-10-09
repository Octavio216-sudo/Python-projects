#this code allows the user to type in a number and have it be represented by hashes
seven_display = {"1": "#\n#\n#\n#\n#", "2": "###\n  #\n###\n#  \n###", "3": "###\n  #\n###\n  #\n###", "4": "# #\n# #\n###\n  #\n  #", 
                 "5": "###\n#  \n###\n  #\n###", "6": "###\n#  \n###\n# #\n###", "7": "###\n  #\n  #\n  #\n  #", "8": "###\n# #\n###\n# #\n###", 
                 "9": "###\n# #\n###\n  #\n###", "0": "###\n# #\n# #\n# #\n###"}
selected_number = input("Please enter a number: ")
digits = [char for char in selected_number if char in seven_display]
for row in range(5):  # each digit has 5 rows
    print("  ".join(seven_display[digit].splitlines()[row] for digit in digits))