# Write a Python program to assess if a file is closed or not.

fhand=open('seventythreefileone.txt','r')
print(fhand.closed)
fhand.close()
print(fhand.closed)