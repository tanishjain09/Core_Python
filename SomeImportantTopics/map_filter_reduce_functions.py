#higher order function - function which take another function as an argument

# def cube(x):
#     return x*x*x
# print(cube(2))


l = [1,2,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))

#map:if we want to apply function on each individual element of list than we can use map function
#which return map object so we can convert it into list as shown below
#map(function,iterable)

# newl = list(map(cube,l))
# print(newl)

newl = list(map(lambda x: x*x*x,l))
print(newl)

#filter :
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and
# returns a new sequence containing only the elements that meet the predicate.
# The filter function has the following syntax:
# filter(predicate,iterable)

# def filter_function(a):
#     return a>=3
# newnewl = list(filter(filter_function,l))
# print(newnewl)

newnewl = list(filter(lambda x: x>=3,l))
print(newnewl)

from functools import reduce
#reduce
def mysum(x,y):
    return x+y
sum = reduce(mysum,l)
print(sum)

