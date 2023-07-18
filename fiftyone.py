# Python function to check  whether x is even or odd

def check(x):
    if x%2==0:
        print("The number is even")
    else:
        print("The number is odd")

x=int(input("Enter the number: "))
check(x)