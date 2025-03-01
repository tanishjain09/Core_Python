# Static methods in Python are methods that belong to a class rather than an instance of the class.
# They are defined using the @staticmethod decorator
# and do not have access to the instance of the class (i.e. self).

class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b

# result = Math.add(2,3)
# print(result)

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(1,4))
print(a.add(7,6))