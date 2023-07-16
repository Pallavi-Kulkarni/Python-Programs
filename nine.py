# Write a program to check if a string is pallindrome or not

s=input("Enter a string: ")
if s[::]==s[::-1]:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")