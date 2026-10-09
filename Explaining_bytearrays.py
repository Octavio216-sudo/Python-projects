#bytearrays are mutable sequences of bytes, which means that you can modify their contents after they are created.
from base64 import decode
choose = int(input("choose what to test: "))
#---------------------------------------------------------------------------------------------------------------------1
#bytearrays when used with strings
if choose == 1:
    ba = bytearray(b'Hello, World!')  # Creating a bytearray using the bytearray() constructor
    print(ba)  # Output: bytearray(b'Hello, World!')
    for i in range(len(ba)):
        print(chr(ba[i] - 1), end='') # Output: Gdssj, Vnqkc!
#---------------------------------------------------------------------------------------------------------------------2
#bytearrays when used with ints
if choose == 2:
    ba = bytearray([65, 66, 67, 68])  # Creating a bytearray using a list of integers
    print(ba)  # Output: bytearray(b'ABCD')
    for i in range(len(ba)):
        print(chr(ba[i]), end='')  # Output: ABCD

#---------------------------------------------------------------------------------------------------------------------3
#Using raw bytearrays to write to a binary file
if choose == 3:
    from os import strerror
    data = bytearray(10)#this bytearray contains 10 bytes, all initialized to zero. They are equivalent to a list of 10 integers, each with a value of 0.
    for i in range(len(data)):
        data[i] = 10 + i
    try:
        bf = open('file.bin', 'w+b')  # Open the file in read and write binary mode
        bf.write(data)  # Write the bytearray to the file
        bf.close()
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))
