class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguauge(self):
        print("The default laguage is Python")


e1 = Employee("Rohan Das",420)
e1.showDetails()
e2 = Programmer("Tanish",67)
e2.showLanguauge()