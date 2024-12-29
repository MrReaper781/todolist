#program to implement variable length argument
#Author: Vaibhav
#Date: 10-12-2024
def average(name,*args):
    '''This function gives average of given subjects'''
    result = 0
    for num in args:
        result = result + num
    result = result/len(args)
    round(result,2)
    print(f"{name} has average: {result}")
    print("Docstring is:", average.__doc__)
#average("Parul",50,60,70)


# Keyword arguments -> **kwargs

def display(name, **kwargs):
    #{name, marks}
    for subject, marks in kwargs.items():
        print("Name of subject ", subject)
        print("Marks: ", marks)
display("Sandip", Maths=50, History=70, Science = 80)
print("Docstring is ", display.__doc__)

