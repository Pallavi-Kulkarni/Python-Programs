# Python program to compute a polynomial equation given that the coefficients of the polynomial are stored in List.

import math

# ax^3+bx^2+cx+d->

l=[]
for i in range(0,4):
    a=int(input("Enter the coefficient value: "))
    l.append(a)
x=int(input("Enter the value of x: "))
j=3
sum=0

for i in range(0,3):
    while(j>0):
        sum=sum+(l[i]*math.pow(x,j))
        break
    j=j-1

sum=sum+l[3]

print("The final answer of polynomial equation is: ",sum)
