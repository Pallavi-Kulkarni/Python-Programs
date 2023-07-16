# Consider a string s=“Hello how are you?”. Write a program to display this string without spaces.

s="Hello how are you?"
mylist=s.split(" ")
print(mylist)
print(*mylist,sep="")
