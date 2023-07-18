# Write a program to take input string from the user and print that string after removing ovals.

list=['A','E','I','O','U','a','e','i','o','u']

n=input("Enter the string: ")
new=''
for i in n:
    if i not in list:
        new+=i
print(new)