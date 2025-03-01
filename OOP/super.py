# class ParentClass:
#     def parent_methos(self):
#         print("This is the parent method.")
#
# class ChildClass(ParentClass):
#     # def parent_methos(self):
#     #     print("Tanish")
#     #     super().parent_methos()
#     def child_methos(self):
#         print("This is the child method.")
#
# child_obect = ChildClass()
# child_obect.child_methos()
# child_obect.parent_methos()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

tanish = Employee("Tanish Sethiya","420")
rohan = Programmer("Rohan","420","Java")

print(rohan.name)