# Python program to find the sum of natural numbers up to n using recursive function

def findsum(n):
    
    res=n+findsum(n-1)
    
       

n=int(input("Enter the number: "))
findsum(n)