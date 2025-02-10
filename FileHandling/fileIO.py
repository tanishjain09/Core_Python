#Before we can perform any operations on a file, we must first open it.
# Python provides the open() function to open a file. It takes two arguments:
# the name of the file and the mode in which the file should be opened



# modes in file
#1 read(r) -> This mode opens the file for reading only and gives an error if the file does not exist
#2 write(w) -> This mode opens the file for writing only and creates a new file if the file does not exist.
#3 append(a) -> This mode opens the file for appending only and creates a new file if the file does not exist.
#4 create(x)-> This mode creates a file and gives an error if the file already exists.
#5 text(t) -> Apart from these modes we also need to specify how the file must be handled.
# t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default.
# The default mode is 'r' (open for reading text, synonym of 'rt' ).
#6 bianry(b) -> used to handle binary files (images, pdfs, etc).

#read from a file
# f = open("myfile.txt",'r')
# text = f.read()
# print(text)
# f.close()

#writing a file
# f = open("myfile.txt",'a')
# f.write("Hello, world!")
# f.close()

#with statement: not needed to close() the file
with open('myfile.txt','a') as f:
    f.write("Hello world")
