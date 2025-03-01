
# dir():
# The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
# It is a useful tool for discovering what you can do with an object.x = [1,2,3]

x=[1,2,3]
# print(dir(x))

# _dict__:
# The __dict__ attribute returns a dictionary representation of an object's attributes.
# It is a useful tool for introspection.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version =  1
p = Person("John",20)
# print(p.__dict__)

# help():
# The help() function is used to get help documentation for an object,
# including a description of its attributes and methods

print(help(Person))