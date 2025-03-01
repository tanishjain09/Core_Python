#Instance variable:
#Instance variables are defined at the instance level and are unique to each instance of the class. They are
# defined inside the init method and are usually used to store information that is specific to each instance of the class.

#Class Variable:
# Class variables are defined at the class level and are shared among all instances of the class.
# They are defined outside of any method and are usually used to store information that is common to all instances of the class.
class Employee:
    companyName = "Apple"
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02 #instance variable
    def showDetail(self):
        print(f"The name of Employee is {self.name} and the raise in {self.companyName} amount is {self.raise_amount} ")

# Employee.showDetail(emp1)
emp1 = Employee("Tanish")
emp1.raise_amount = 0.3 #instance varible will be change
emp1.companyName = "Apple India"#this will become instance variable if this is presene and ifmnot present than check for class varible in emp1
emp1.showDetail()
emp2 = Employee("Rohan")
emp2.showDetail()
