
#Exception -> Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
# Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
a = input("Enter the number ")

print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid Input")

print("Other code of the progam")
print("End of program")

