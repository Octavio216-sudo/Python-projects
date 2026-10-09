import os
import platform
import subprocess #replacement of os.system() command.
choose = int(input("choose what you want to test: "))
if choose == 1:
    os.mkdir('new_directory')#You know linux. You know what this does.
    os.rmdir('new_directory')#You know linux. You know what this does.
    os.makedirs('new_directory/sub_directory')#Allows you to create a directory and subdirectory in one go. Python version of mkdir -p command.
    os.removedirs('new_directory/sub_directory')#Allows you to remove a directory and subdirectory in one go. Python version of rmdir -p command.
if choose == 2:
    os.rename('old_file.txt', 'new_file.txt')#Python version of mv command. You know linux. You know what this does.
if choose == 3:
    print(platform.uname()) 
    #Return the following: systemname — stores the name of the operating system; nodename — stores the machine name on the network; 
    #release — stores the operating system release; version — stores the operating system version; machine — stores the hardware identifier, e.g., x86_64.
if choose == 4:
    print(os.getcwd())#Python version of pwd command. You know linux. You know what this does.
    os.chdir('new_directory')#Python version of cd command. You know linux. You know what this does.
if choose == 5:
    print(os.listdir())#Python version of ls command. You know linux. You know what this does.
    print(dir(os))#Same thing in a different way.
if choose == 6:
    print(os.environ)#Prints all the environment variables.
if choose == 7:
    print(os.path.exists('file.txt'))#Checks if the file exists. 
    print(os.path.isfile('file.txt'))#Checks if the file is a file.
    print(os.path.isdir('directory'))#Checks if the directory exists.
if choose == 8:
    print(os.name)#Prints nt if the OS is Windows, posix if the OS is Linux or Mac, and java if the OS is Java platform.