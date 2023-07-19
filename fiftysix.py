# Python program to find the sum of natural numbers up to n using recursive function

def findsum(n):
    if n==0:
        return 0
    return n+findsum(n-1)
    
       

n=int(input("Enter the number: "))
print(findsum(n))