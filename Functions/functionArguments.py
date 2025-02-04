# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

#1. Default arguments -> when provide default value to argument while creating function ,we can also provide diff values to parameter while calling functions
def defaultArgument(a=9,b=0):
     print("a+b = ",a+b)

defaultArgument()
defaultArgument(a=4,b=1)

#2. Keyword argumnets ->
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.
# Hence, the the order in which the arguments are passed does not matter

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Bhaver", lname = "Sethiya", fname = "Tanish")

#3. Required arguments ->
#In case we don’t pass the arguments with a key = value syntax,
# then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

def name1(fname, mname, lname):
    print("Hello,", fname, mname, lname)

# name1("Peter", "Quill") -> will give error

#4. Variable-length arguments ->
#a. Arbitary arguments -> While creating a function, pass a '*' before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of tuple.

def arbitaryArguments(*a):
    print("Hello",*a,"\nhow are you") #i can also print values like a[0],a[1] but it will restrit me to insert no. of parameter as per the function

arbitaryArguments("Tanish","Sethiya")
arbitaryArguments("Rahul","Rajiv","Verma")


#Return statement
# The return statement is used to return the value of the expression back to the calling function.
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))