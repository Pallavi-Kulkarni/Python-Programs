# Amstrong number or not

import math

def armstnum(n):
    x=n
    sum=0
    while(x>0):
        d=x%10
        sum+=math.pow(d,3)
        x=x//10
    if(n==sum):
        print("The number is armstrong number")
    else:
        print("The number is not armstrong number")

n=int(input("Enter the number: "))
armstnum(n)