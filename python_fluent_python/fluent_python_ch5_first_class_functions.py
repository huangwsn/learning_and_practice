# (P139) 
# “first-class object” as a program entity that can be:
#   - Created at runtime
#   - Assigned to a variable or element in a data structure
#   - Passed as an argument to a function
#   - Returned as the result of a function


# (P140) Example 5-1: 
# Example 5-1 shows that Python functions are objects. 
# Here wecreate a function, call it, read its __doc__ attribute, 
# and check that the function object
# itself is an instance of the function class.
print("\nExample 5-1")
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)
print(factorial(3))
print(factorial.__doc__)  # Print the docstring of the function
print(type(factorial))  # Print the type of the function


# TODO: Below - To be finished
# (P141) Example 5-2:
# Example 5-2 shows the “first class” nature of a function object. 
# Ex 5-1-a We can assign it a variable "fact" and call it through that name. 
# Ex 5-1-b We can also pass factorial as an argument to map. The map function returns an iterable where each item is the result of the application
# of the first argument (a function) to succesive elements of the second argument (an
# iterable), range(10) in this example.
print("\nExample 5-2")
fact = factorial
print(fact)
print(fact(5))
# map(factorial, range(11))
# <map object at 0x...>
# >>> list(map(fact, range(11)))
# [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
# TODO: Above - To be finished