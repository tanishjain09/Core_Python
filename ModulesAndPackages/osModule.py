import os

# # Corrected path
# file_path = r"C:\Coding\Core_Python\SomeImportantTopics\virtualEnvironment.txt"  # Ensure it is a file
#
# # Open the file safely
# f = os.open(file_path, os.O_RDONLY)
#
# # Read content
# contents = os.read(f, 1024)
#
# # Close the file
# os.close(f)
#
# # Print contents
# print(contents.decode())  # Convert bytes to string
#
folers = os.listdir("C:\Coding\Core_Python")


for foler in folers:
    print(foler)
