# from customModule import demoFunc,foo
# demoFunc()
#
# import customModule as cM
# print(cM.foo)
# print(cM.foo1)
#
# #this is how we can import one python file and there function and variable in different py program
import customModule
# there is a issue, if we called the demo function in the customModule file then
#if we only import the module the functon get called and if we import and call the function
#using customModule.demoFunc() the function is called 2 times to solve this we are using
# if __name__ = "__main__" so that the function called in the module doesn't call here automatiaclly it will get called when we call it only

customModule.demoFunc()
