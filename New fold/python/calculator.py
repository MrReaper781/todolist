import calcfun as func
a,b = 5,3
n = int(input("Enter the number between 1-5: "))
if n == 1:
    print("Addition:",func.sum(a,b))
elif n == 2:
    print("Subtraction:",func.substraction(a,b))
elif n == 3:
    print("Multiplication:",func.multiplication(a,b))
elif n == 4:
    print("Divison:",func.divison(a,b))
elif n == 5:
    print("Factorial:",func.fact(a))
else:
    print("Wrong choice, try again")