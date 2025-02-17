#1 readline()

# f = open('myfile.txt','r')
# while True:
#     line = f.readline ()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break

# f = open('marks.txt','r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in maths is: {m1}")
#     print(f"Marks of student {i} in SST is: {m2}")
#     print(f"Marks of student {i} in english is: {m3}")

#2 writeline() ->The writelines() method in Python writes a sequence of strings to a file.
# The sequence can be any iterable object, such as a list or a tuple.

f = open('myfile2.txt','w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()

