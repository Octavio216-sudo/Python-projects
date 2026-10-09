#closures are a python feature that allows you to use nested functions to get access to variables after their original scope has finished executing.
#this is useful for creating functions that can remember the state of their environment even after the outer function has completed.
def outer_function(outer_variable):
    def inner_function(inner_variable):
        return f"Outer variable: {outer_variable}, Inner variable: {inner_variable}"
    return inner_function

example_closure = outer_function("outside")
print(example_closure("inside"))  # Output: Outer variable: outside, Inner variable: inside