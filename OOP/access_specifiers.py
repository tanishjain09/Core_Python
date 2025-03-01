#Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
#Types of access specifiers
# Public access modifier
# Private access modifier
# Protected access modifier
class Employee:
    def __init__(self):
        self.__name = "Harry" #__variablename behave like private access modifier

a = Employee()
# print(a.name) cant access directly but can access by other way
print(a._Employee__name)#can be access indirectly
#thisi is called name mangling in python
print(a.__dir__())

#protected access modifier ->
class Student:
    def __init__(self):
        self.name = "Harry"
    def _funName(self): #protected method
        return "CodeWithHarry"
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj.name)
print(obj._funName())

print(obj1.name)
print(obj1._funName())
print(dir(obj))