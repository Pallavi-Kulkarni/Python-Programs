# Program to check prime number or not

n=int(input("Enter a number: "))
is_prime=True
if(n>1):   
    for i in range(2,n):
        if n%i==0:
            is_prime=False
else:
    exit()

if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")
