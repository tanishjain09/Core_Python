
#for can iterate over a sequence of iterable objects in python,iterate over sequence is nothing but iterate over string,list,tuple,sets and dictionaries

name = "tanish"
for i in name: #for loop iterating over string
    print(i)

list = ['yello','green','black','red']
for i in list: #for loop iterating over list
    print(i)

#range() ->if we want to use loop for any specific no. of times then we use

print("Table of 5")
for i in range(1,11):
    print(f"5 X {i} = {i*5}")

#for loop with else statment
list = []
for i in list:
    print(list[i])
else:
    print("List is empty")
