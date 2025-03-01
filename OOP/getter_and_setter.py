#getter ->
# Getters in Python are methods that are used to access the values of an object's properties
# They are used to return the value of a specific property, and are typically defined using the @property decorator.

class Myclass :
    def __int__(self,value):
        self._value = value
    def show(self):
        print(f"vlaue id {self.value}")
    @property
    def value(self):
        return self._value


obj = Myclass(10)
obj.show()