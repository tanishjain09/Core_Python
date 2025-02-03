

str = "i am currently in 4th semester"

#.endswith() -> give boolean
print(str.endswith("ter"))

#.capitalize() ->capitalize the first char (make new string)
print(str.capitalize())

#.replace(old value,new value)
print(str.replace("4th","5th"))

#.find() ->search first occrence of char we are searching
print(str.find("c"))

#.count() -> count the occurence of substr in the str
print(str.count("currently"))

#.spilt()->  given string at the specified instance and returns the separated strings as list items.
print(str.split(" "))

#center() -> The center() method aligns the string to the center as per the parameters given by the user.
print(str.center(50))
print(str.center(50,"-"))
#many more function are there in the Python.....