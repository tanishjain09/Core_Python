#'is' vs '==' in Python
# In Python, is and == are both comparison operators that can be used to check if two values are equal.
# However, there are some important differences between the two that you should be aware of.
#
# The is operator compares the identity of two objects, while the == operator compares the values of the objects.
# This means that is will only return True if the objects being compared are the exact same object in memory(exact same memory location), while == will return True if the objects have the same value.

a = [1,2,43]
b = [1,2,43]

print(a is b)
print(a == b)

# One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed.
# This means that, for strings and integers, is and == will always return the same result:

a1 = 4
b1 = 4

print(a1 is b1)
print(a1 == b1)
