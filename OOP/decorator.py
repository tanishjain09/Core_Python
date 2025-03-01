#decorator ->
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods.
# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
# The new function is often referred to as a "decorated" function.

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet   #-> greet(hello)()
def hello():
    print("Hello world")
@greet
def add(a,b):
    print(a+b)

hello()
add(1,8)

#practical use ->

import logging

def log_function_call(func):
    def decorated(*args,**kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args,**kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a,b):
    return a + b

my_function(5,5)