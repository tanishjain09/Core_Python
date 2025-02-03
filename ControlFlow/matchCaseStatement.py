#match case is just like switch case in other languages like c,c++ and java this help when we have multiple cases and condition in a program run a program

x=90

match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    case _ if x < 10: #empty case with if statement
        print("x is < 10")
        # default case(will only be matched if the above cases were not matched)
    case _:
        print(x)