# Write a program to check whether a given number is palindrome or not.

n=int(input("Enter the number: "))
x=n
rev=0

while x>0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
if n==rev:
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")