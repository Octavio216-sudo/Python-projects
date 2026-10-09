#lambda functions are anonymous functions that can take any number of arguments but can only have one expression.
#They are most often used as small, throwaway functions that are not meant to be reused elsewhere in the code.
choose = int(input("enter a number to test a specific code snippet: "))
#--------------------------------------------------------------------------------------------------------------------1
if choose == 1:
    def print_function(args, fun):
        for x in args:
            print('f(', x,')=', fun(x), sep='')

    print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)  #This is more optimal than defining a function and invoking it here

#----------------------------------------------------------------------------------------------------------------------2
#This is how the almbda function works with the map function. The map function takes a function and an iterable as arguments and applies the function to each item 
#in the iterable, returning a new iterable with the results.
if choose == 2:
    list1 = [1, 2, 3, 4, 5]
    list2 = list(map(lambda x: x ** 2, list1)) #Takes each element in list1 to the power of 2 and returns a new list with the results
    print(list1, "turned into", list2)  #Output: [1, 4, 9, 16, 25]

#----------------------------------------------------------------------------------------------------------------------3
#This is how the lambda function works with the filter function. The filter function takes a function and an iterable as arguments and applies the 
#function to each item. Unlike the map function, the filter function returns a new iterable with only the items that return True when passed to the function.
if choose == 3:
    list1 = [1, 2, 3, 4, 5]
    list2 = list(filter(lambda x: x % 2 == 0, list1)) #Takes each element in list1 and returns a new list with only the even numbers
    print(list1, "filtered to", list2)  #Output: [2, 4]