# Program to get a string made of the first 2 and the last 2 chars from a given string. 
# If the string length is less than 2, return empty string, otherwise return new string created

s=input("Enter a string: ")
length=len(s)

if length<2:
    print(" ")
else:
    print(s[0]+s[1]+s[length-2]+s[length-1])
    