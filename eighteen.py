# "Program to perform simulation of simple calculator for basic operations like +,-, *, /, % etc. 
#(Hint: Read a character +, - etc as operator from the user. Perform
#respective operation based on the operator. And Display the result)"

def mycalc(p,q):
    n=input("Enter the operator to perform operation: ")
    match n:
        case '+':
            r=p+q
            print(r)
        case '-':
            r=p-q
            print(r)
        case '*':
            r=p*q
            print(r)
        case '/':
            r=p/q
            print(r)
        case '%':
            r=p%q
            print(r)
        case _:
            print("Enter the right operator to proceed with operation")

while True:
    print("-----------Welcome to Calculation --------------")
    a=int(input("Enter any number: "))
    if a>0:
        p=int(input("Enter the first number: "))
        q=int(input("Enter the second number: "))        
        mycalc(p,q)
    else:
        break
    








