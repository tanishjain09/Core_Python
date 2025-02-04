# marks1 = 94.4
# marks2 = 87.9
# marks3 = 78.1
# marks4 = 89.1  ->very hard to store large data in this manner

#List : A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes,
# lists are defined by having values between square brackets [ ]
marks = [94.4,87.5,95.2,66.4,45.1]
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

#list in python can store element in  different types(int,float,str)
#while in java we can't

student = ["Tanish",19,178.7,"Vadodara"] #list having more than one data type in it
print(student[0])
#student[1] = 20 ->possible because list are mutable in python
print(student)
