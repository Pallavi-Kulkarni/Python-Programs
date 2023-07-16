# Python program to accept 3 digits and print all possible combination from digits

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

d=[]
d.append(a)
d.append(b)
d.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            print(d[i],d[j],d[k])