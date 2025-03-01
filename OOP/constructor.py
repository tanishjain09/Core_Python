#constructor:
# A constructor is a special method in a class used to create and initialize an object of a class.
# There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class.
# The main purpose of a constructor is to initialize or assign values to the data members of that class.
# It cannot return any value other than None.

#contructor in python:

# class Demo:
#     def __init__(self):
#

#1. parameterized constructor
class Details:
    def __init__(self,animal,group):
        self.animal = animal
        self.group = group

obj1 = Details("cat","group 1")
print(obj1.animal,obj1.group)

#2. default constructor

# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor,

class Details1:
    def __init__(self):
        print("animal cat belong to group 2 ")

obj2 = Details1()
