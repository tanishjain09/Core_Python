#class Method:
# A class method is a type of method that is bound to the class and not the instance of the class.
# In other words, it operates on the class as a whole, rather than on a specific instance of the class.
# Class methods are defined using the "@classmethod" decorator, followed by a function definition.

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company id {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)