# Write a program to list out all prime numbers between two integers m and n. And sum of prime numbers

m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
sum=0
for val in range(m,n+1):
    if val>1:
        is_prime=True

        for n in range(2,val):
            if(val%n)==0:
                is_prime=False
                break
        if is_prime:
            sum+=val
print("The sum of prime number's is: ",sum)
