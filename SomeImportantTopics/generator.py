#generator:
# Generators in Python are special type of functions that allow you to create an iterable sequence of values.
# A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it.
# Generators are a powerful tool for working with large or complex data sets,
# as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

#creating generator
# In Python, you can create a generator by using the yield statement in a function.

def my_generator():
    for i in range(500000):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))

# The next() function is used to request the next value from the generator,
# and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.

for j in gen:
    print(j)