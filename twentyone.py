# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

def mysum(p,q,r):
    sum=p+q+r
    if p==q and q==r:
        return 3*sum
    else:
        return sum
    
p=int(input("Enter the first number: "))
q=int(input("Enter the second number: "))
r=int(input("Enter the third number: "))
print("The sum is: ",mysum(p,q,r))