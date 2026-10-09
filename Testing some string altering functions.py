function_number = int(input("enter a number to test a specific function: "))
test_string = input("enter a string to test the function: ")
ord_list = []

#--------------------------------------------------------------------------------------------------------------------------------------------------1
#strings are sequence types in python, so we can use many commands you would use on lists to manipulate  or get info about strings.
#example: len(test_string) will return the length of the string, and test_string[0] will return the first character of the string.
if function_number == 1:
    print("the length of the string is: ", len(test_string))
    for i in range(len(test_string)):
        print(f"element {i} of the string is: {test_string[i]}") 

#-------------------------------------------------------------------------------------------------------------------------------------------------2
#You can see the code point of a character in a string using the ord() function. You can also convert a code point back to a character using the chr() function.
if function_number == 2:
    for i in test_string:
        ord_list.append(ord(i))
        print(f"the code point of {i} is: {ord(i)}")
    for i in ord_list:
        print(f"the character of code point {i} is: {chr(i)}")

#-------------------------------------------------------------------------------------------------------------------------------------------------3
#You can use the list(), min(), and max() functions to get a list of the characters in a string, as well as the minimum and maximum characters 
#based on their code points. If it appears that nothing has been returned for min or max that is probably a space character
if function_number == 3:
    char_list = list(test_string)
    print(f"the list of characters in the string is: {char_list}")
    print(f"the minimum character in the string is: {min(char_list)}", ord(min(char_list)))
    print(f"the maximum character in the string is: {max(char_list)}", ord(max(char_list)))

#-------------------------------------------------------------------------------------------------------------------------------------------------4
#There are many commands that can be used to check the data in a string. These include isalnum(), isalpha(), isdigit(), islower(), isupper(), isspace(), 
#startswith(), and endswith(). These commands will return True or False depending on the data in the string.
if function_number == 4:
    start_string = input("enter a string to check if the test string starts with it: ")
    end_string = input("enter a string to check if the test string ends with it: ")
    print(f"the string is alphanumeric: {test_string.isalnum()}")
    print(f"the string is alphabetic: {test_string.isalpha()}")
    print(f"the string is a digit: {test_string.isdigit()}")
    print(f"the string is lowercase: {test_string.islower()}")
    print(f"the string is uppercase: {test_string.isupper()}")
    print(f"the string is whitespace: {test_string.isspace()}")
    print(f"the string starts with {start_string}: {test_string.startswith(start_string)}")
    print(f"the string ends with {end_string}: {test_string.endswith(end_string)}")

#-------------------------------------------------------------------------------------------------------------------------------------------------5
#The rfind(), find(), and index() functions can be used to find the index of a character or substring in a string. 
#The count() function can be used to count the number of occurrences of a character or substring in a string.
if function_number == 5:
    search_string = input("enter a string to search for in the test string: ")
    print(f"the index of the first occurrence of {search_string} is: {test_string.find(search_string)}")
    print(f"the index of the last occurrence of {search_string} is: {test_string.rfind(search_string)}")
    print(f"the index of the first occurrence of {search_string} is: {test_string.index(search_string)}")
    print(f"the number of occurrences of {search_string} is: {test_string.count(search_string)}")

#-------------------------------------------------------------------------------------------------------------------------------------------------6
#Commands that alter cases include the capitalize(), lower(), upper(), title(), and swapcase() functions
if function_number == 6:
    print(f"the string with the first character capitalized is: {test_string.capitalize()}")
    print(f"the string in lowercase is: {test_string.lower()}")
    print(f"the string in uppercase is: {test_string.upper()}")
    print(f"the string in title case is: {test_string.title()}")
    print(f"the string with the case of each character swapped is: {test_string.swapcase()}")

#-------------------------------------------------------------------------------------------------------------------------------------------------7
#Commands that remove or replace characters include the strip(), lstrip(), rstrip(), and replace() functions
if function_number == 7:
    replace_string = input("enter a string to replace in the test string: ")
    replacement_string = input("enter a string to replace it with: ")
    print(f"the string with {replace_string} replaced with {replacement_string} is: {test_string.replace(replace_string, replacement_string)}")
    print(f"the string with leading and trailing whitespace removed is: {test_string.strip()}")
    print(f"the string with leading whitespace removed is: {test_string.lstrip()}")
    print(f"the string with trailing whitespace removed is: {test_string.rstrip()}")

#-------------------------------------------------------------------------------------------------------------------------------------------------8
#Commands that split or join characters include the split() and join() functions
if function_number == 8:    
    split_char = input("enter a character to split the test string on: ")
    print(f"the string split on {split_char} is: {test_string.split(split_char)}")
    join_char = input("enter a character to join the test string on: ")
    print(f"the string joined on {join_char} is: {join_char.join(test_string)}")

#-------------------------------------------------------------------------------------------------------------------------------------------------9
#Commands that change the order of characters in the string or the position of the string itself include the reversed(), sort(), sorted(), and center() functions
#It is recommended to use these with the join function
if function_number == 9:
    print(f"the string reversed is: {''.join(reversed(test_string))}")
    print(f"the string sorted is: {''.join(sorted(test_string))}") #sort() and sorted() do mostly the same thing but sort() changes the origin list while sorted() makes a new one
    print(f"the string centered with a width of 20 is: {test_string.center(20)}")