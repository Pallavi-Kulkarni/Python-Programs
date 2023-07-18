# program that takes input password string from user and display that string 
# if string contains at least one Uppercase character, one Lowercase character and one digit.

def check(p):
    u=0
    l=0
    d=0
    count=0
    for i in p:
       if i.isupper():
           u=1          

       if i.islower():
           l=1
                     
       if i.isdigit():
           d=1           
          
       if u and l and d:
           print(p)
           break
          
p=input("Enter the password: ")
check(p)