import os
#a = append: add data to the end of the file and creats file if it doesnt already exist.
#r = read: read the contents of the file. Also the default mode if no mode is specified.
#x = create: create a new file. If the file already exists, the operation will fail.
#w = write: write data to the file, overwriting existing content instead of just adding to it like a. 
#t = text file, b = binary file: Specifies the type of file to be opened. The default is text mode.

test_pick = input("enter the number corresponding to the operation you want to perform on the file: ")
#----------------------------------------------------------------------------------------------------------------1
if test_pick == "1":
    #to read the entire contents of a file, we can use the read() method of the file object.
    stream = open("File.txt") #To open a file: <name> = open(<"filename">, <a combination of the above letters>)
    print(stream.read()) #read and print the file
    stream.close() #close the file after reading it.
#----------------------------------------------------------------------------------------------------------------2
if test_pick == "2":
    #to read a specified number of characters from the file, we can pass the number of characters as an argument to the read() method.
    stream = open("File.txt") #open the file in read mode.
    print(stream.read(10)) #read and print the first 10 characters of the file. 
    stream.close() #close the file after reading it.

    #warning: if this command is used directly after a read() command, it will read the next 10 characters of the file, not the first 10 characters. 
    #This is because the read() method moves the file pointer to the end of the file

#----------------------------------------------------------------------------------------------------------------3
if test_pick == "3":
    #to read a single line from the file, we can use the readline() method of the file object.
    stream = open("File.txt") #open the file in read mode.
    print(stream.readline()) #read and print the first line of the file.
    print(stream.readline()) #read and print the second line of the file. This is because the readline() method moves the file pointer
    print(stream.readlines())# read and print all the lines of the file as a list. This is because the readlines() method moves the file pointer to the end of the file.
    stream.close() #close the file after reading it.

#----------------------------------------------------------------------------------------------------------------4
if test_pick == "4":
    #to iterate through the lines of a file, we can use a for loop to iterate through the file object.
    stream = open("File.txt") #open the file in read mode.
    for line in stream: #iterate through the lines of the file.
        print(line) #print each line of the file.
    stream.close() #close the file after reading it.

#----------------------------------------------------------------------------------------------------------------5
if test_pick == "5":
    #to use the try, except, and finally block to ensure that the file is closed after reading it, we can use the following code:
    try:
        stream = open("File.txt") #open the file in read mode.
        print(stream.read()) #read and print the entire contents of the file.
    except: #catch any exceptions that may occur while reading the file.
        print("An error occurred while reading the file.")
    finally:
        stream.close() #close the file after reading it. This will ensure that the file is closed even if an exception occurs while reading it.

#----------------------------------------------------------------------------------------------------------------6
if test_pick == "6":
    #the a parameter in the open() function is used to create files that dont exist yet and add data to them. It is used with the write() method of the file object.
    stream = open("File.txt", "a") #open the file in append mode.
    stream.write("\nThis is a new line.") #add a new line to the file.
    stream.close() #close the file after writing to it.
    stream = open("File.txt", "r") #open the file in read mode.
    print(stream.read()) #read and print the entire contents of the updated file.
    stream.close() #close the file after writing to it.

#----------------------------------------------------------------------------------------------------------------7
if test_pick == "7":
    #the w parameter in the open() function is like the a paremeter but it overwrites the entire contents of the file instead of adding to it.
    stream = open("File.txt", "w") #open the file in write mode.
    stream.write("This is a new line.") #overwrite the file with the new line.
    stream.close() #close the file after writing to it.
    stream = open("File.txt", "r") #open the file in read mode.
    print(stream.read()) #read and print the entire contents of the updated file.
    stream.close() #close the file after writing to it.

#----------------------------------------------------------------------------------------------------------------8
if test_pick == "8":
    #to iterate through the characters of a file, we can use a for loop to iterate through the file object.
    stream = open("File.txt") #open the file in read mode.
    for char in stream: #iterate through the characters of the file.
        print(char, end="") #print each character of the file.
    stream.close() #close the file after reading it.
    #another way to iterate through the characters of a file is to use the read() method of the file object to read the entire contents of the file
    with open("File.txt", "r") as f:
        while True:
            char = f.read(1)   # read a single character
            if not char:       # end of file
                break
            print(char, end="")
    stream.close() #close the file after reading it.

#----------------------------------------------------------------------------------------------------------------9
if test_pick == "9":
    #to use the x parameter in the open() function to create a new file, we can use the following code:
    stream = open(input("Enter the name of the file to create: "), "x") #open the file in create mode. This will create a new file called NewFile.txt.
    stream.close() #close the file after creating it.

#----------------------------------------------------------------------------------------------------------------10
if test_pick == "10":
    #to delete files, we can use the os.remove() method of the os module. This method takes the name of the file to be deleted as an argument.
    os.remove(input("Enter the name of the file to delete: ")) #delete the specified file.

#----------------------------------------------------------------------------------------------------------------11
#stream lab: iterate through a dictionary and count the number of times each letter appears in a file.
if test_pick == '11':
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    stream = open("File.txt")
    for char in stream.read():
        if char.lower() in alphabet:
            alphabet[char.lower()] += 1
    stream.close()
    for letter, count in sorted(alphabet.items(), key=lambda x: x[1], reverse=True): #sorts the dictionary by the number of times each letter appears in the file and prints the results.
        print(f"{letter}: {count}")

#----------------------------------------------------------------------------------------------------------------12
#another lab
class StudentsDataException(Exception):
    pass
class BadLine(StudentsDataException):
    pass
class FileEmpty(StudentsDataException):
    pass
if test_pick == '12':
    file_name = input("Enter the name of the file to read: ")
    if file_name == "File.txt":    
        students = {}
        try:
            with open("File.txt") as stream:
                lines = stream.readlines()
                if not lines:  # file is empty
                    raise FileEmpty("The file is empty.")

                for line in lines:
                    parts = line.split()
                    if len(parts) != 3:  # not exactly name, surname, score
                        raise BadLine(f"Bad line format: {line.strip()}")

                    full_name = parts[0] + " " + parts[1]
                    try:
                        score = float(parts[2])
                    except ValueError:
                        raise BadLine(f"Score is not a number: {parts[2]}")

                    students[full_name] = students.get(full_name, 0) + score

        except FileEmpty as e:
            print("Error:", e)
        except BadLine as e:
            print("Error:", e)
        except StudentsDataException as e:
            print("General student data error:", e)
        except Exception as e:
            print("Unexpected error:", e)
        else:
            print(students)
