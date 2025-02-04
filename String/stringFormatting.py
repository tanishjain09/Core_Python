# String formatting in Python is the process of creating a new string by embedding variables or expressions within a string template.
#eg.
#1. .format method->
letter = "Hey my name is {0} and i am from {1}"
name = "tanish"
county = "India"

print(letter.format(name,county))
print("Hey my name is {} and i am from {}".format(name,county))


#2.F-string->
name1 = "tanish"
age = 19
print(f"Hello my name is {name1} and i am {age} years old")
print(f"4 x 4 is : {4*4}")
