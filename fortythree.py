# Pallindrome number or not

def palindrome(n):
    x=n
    rev=0
    while(x>0):
        rem=x%10
        rev=(rev*10)+rem
        x=x//10
    
    if n==rev:
        print("The number is Palindrome number")
    else:
        print("The number is not palindrome")

n=int(input("Enter the number: "))
palindrome(n)