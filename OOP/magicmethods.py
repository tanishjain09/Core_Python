class Employee:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        i= 0
        for c in self.name:
            i = i+1
        return i
    def __str__(self):
        return f"The emoployee name is {self.name}"


e = Employee("Tanish")
print(e.name)

#__str__ and __repr__
#The str and repr methods are both used to convert an object to a string representation.
# The str method is used when you want to print out an object,
# while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

print(str(e))
print(repr(e))

#__call__
# The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called.