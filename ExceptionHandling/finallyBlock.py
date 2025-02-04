# The finally block is executed irrespective of the outcome of try……except…..else blocks
# One of the important use cases of finally block is in a function which returns a value. here is the example
def func1():
    try:
        list = [0,2,3,4]
        i = int(input("Enter the index: "))
        print(list[i])
        return 1;
    except:
        print("Some error occured")
        return 0;
    # print("I am always executed")  if we write this it will not run as the function is return
    finally:
        print("I am always executed") #this will executed even after function returned
x = func1()
print(x)