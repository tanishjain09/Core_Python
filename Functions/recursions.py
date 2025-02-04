def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fiboSequence(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fiboSequence(n-1) + fiboSequence(n-2)

print(fiboSequence(3))

def prinFibo(n):
    for i in range(n):
        print(fiboSequence(i),end = " ")
prinFibo(24)