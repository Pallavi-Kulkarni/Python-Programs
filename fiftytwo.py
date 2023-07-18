# Python program to find the H.C.F of two input number

def hcf(m,n):
    list=[]
    r=max(m,n)
    for i in range(2,r):
        if(i==m):continue
        if m%i==0 and n%i==0:
            list.append(i)
    print(max(list))


m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
hcf(m,n)