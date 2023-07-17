# Pallindrome number or not

def palindrome(n):
    x=n
  
    rem=0
    while(x>0):
        rev=x%10
        rem=rev*10+rem
        x=x//10







n=int(input("Enter the number: "))