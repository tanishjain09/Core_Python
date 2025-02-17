#1. seek():
# The seek() function allows you to move the current position within a file to a specific point.
# The position is specified in bytes,
# and you can move either forward or backward from the current position.

with open('myfile.txt','r') as f:
    print(type(f))
    #move to the 10th byte in the file
    f.seek(10)

    #read the next 5 bytes
    data = f.read(5)
    print(data)

#2.tell():
# The tell() function returns the current position within the file, in bytes.
# This can be useful for keeping track of your location within the file or for seeking to a
# specific position relative to the current position.
# current_position = f.tell()
# print(current_position)

#3. truncate()

with open('sample.txt','w') as f:
    f.write('Hello world')

    f.truncate(5) #-> WILL truncate the file to 5bytes and will have 'HELLO' in the file

with open('sample.txt','r') as f:
    print(f.read())