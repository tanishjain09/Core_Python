import time

# def usingWhile():
#     i = 0
#     while i<50000:
#         i = i+1
#         print(i)
#
#
# def usingFor():
#     for i in range(50000):
#         print(i)
#
# init = time.time()
# usingFor()
# t1 = time.time() - init
# usingWhile()
# t2 = time.time() - init
# print(t1)
# print(t2)

# print(4)
# time.sleep(3)
# print("This is printed after 3seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)