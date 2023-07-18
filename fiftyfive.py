# Python Program to find the L.C.M. of two input number

def lcmcalc(m,n):
    greater=max(m,n)
    while True:
        if greater%m==0 and greater%n==0:
            lcm=greater
            break
        greater+=1
    print(lcm)
       

m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
lcmcalc(m,n)

