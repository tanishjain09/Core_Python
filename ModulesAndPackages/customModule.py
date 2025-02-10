def demoFunc():
    print("This is demo function ")

foo = "Hii from the custom module"
foo1 = "demo variable 2"
pi = 3.14
print(__name__) #this will __main__ in this and if we imprt this file somewhere else then this will print the name of this file
if __name__ == "__main__":
    demoFunc()

