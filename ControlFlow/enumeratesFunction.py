#The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string)
# and get the index and value of each element in the sequence at the same time.
# Here's a basic example of how it works:

fruits = ['apple','banana','graphes']
for index,fruit in enumerate(fruits):
    print(index,fruit)

for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
