dict={'name' : 'tanish','age':19,'eligible':True}

#methods:
#1 .update() -> updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
print(dict)
dict.update({'age' : 20})
dict.update({'DOB':'09/09/2005'})
print(dict)

#2 .clear() ->remove all the items from the list

# dict.clear()
# print(dict)

#3 .pop() ->remove the key value pair whose key is passed as parameter

dict.pop('eligible')
print(dict)

#4 .popitem() -> remove the last key-value pair from the dictonary

#we can also use 'del' keyword to delete the dict entirely

del dict
print(dict)
