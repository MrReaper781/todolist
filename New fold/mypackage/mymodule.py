def sum(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    a*b
    
def divison(a,b):
    if b != 0:
        return a/b

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)