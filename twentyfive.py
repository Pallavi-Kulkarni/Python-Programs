# Program to find minimum amongst 3 numbers

def minnum(a,b,c):
    if a<b and a<c:
        print("a is minimum")
    elif b<a and b<c:
        print("b is minimum")
    else:
        print("c is minimum")


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
minnum(a,b,c)