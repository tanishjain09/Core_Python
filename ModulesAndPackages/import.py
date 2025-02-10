# Importing in Python is the process of loading code from a Python module into the current script.
# This allows you to use the functions and variables defined in the module in your current script,
# as well as any additional modules that the imported module may depend on.

from math import  sqrt,pi

# result = math.sqrt(9)  when importing math module
# print(result)

#from keyword -> using this we can import only pi and sqrt function present in math module

result = sqrt(8)
a = pi
print(result+a)

#as keyword -> allows you to rename imported modules using the as keyword.
# This can be useful if you want to use a shorter or more descriptive name for a module

from math import sqrt as s
a = s(98)
print(a)

#dir() function ->
# Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module.
# This can be helpful for exploring and understanding the contents of a new module.

import math

print(dir(math))