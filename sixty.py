# Apply import,from, * and other module related concepts to create a module called “calc” consists of 4 function 
#that should return sum, division, multiplication and subtraction. 
#Write another module caller “user”,import the calc module and illustrate the use of all the functions of calc module.

from calc import *

m=int(input("Enter first number: "))
n=int(input("Enter second number: "))


print(add(m,n))
print(sub(m,n))
print(mul(m,n))
print(div(m,n))

