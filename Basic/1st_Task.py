a=int(input("Enter 1st number for the operation: "))
b=int(input("Enter 2nd number for the operation: "))
c=str(input("Enter the operator (+,-,*,/): "))
def addition(a,b):
    print ("The sum of the numbers is: ",a+b)
def subtraction(a,b):
    print ("The subtraction of the numbers is: ",a-b)
def multiplication(a,b):
    print ("The multiplication of the numbers is: ",a*b)
def division(a,b):
    if b==0:
        print("Error, can't divide by 0.")
    else:
        print ("The division of the numbers is: ",a/b)
match c:
    case "+":
        addition(a,b)
    case "-":
        subtraction(a,b)
    case "*":
        multiplication(a,b)
    case "/":
        division(a,b)
