#In python, we can raise custom errors by using the raise keyword.
salary = int(input("Enter salary amount: "))
if not 200 < salary < 5000:
    raise ValueError("not a valid salary")