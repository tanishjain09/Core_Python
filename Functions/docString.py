
#Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
#docstring attributes ->
# Whenever string literals are present just after the definition of a function, module, class or method,
# they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.
print(square.__doc__)
print(square(3))