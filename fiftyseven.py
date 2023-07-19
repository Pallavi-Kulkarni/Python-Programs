# Python program to display the Fibonacci sequence up to n-th term using recursive functions
def fibonacci(n,n1,n2):
    if(n==0):
        exit()
        
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    return fibonacci(n-1,n1,n2)
       

n=int(input("Enter the number: "))
print(0,1,end=" ")
print(fibonacci(n-2,0,1))