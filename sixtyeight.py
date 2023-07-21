# Write a Python program to append text to a file and display the text.

fhand=open('sixtysevenfile.txt','a+')
text=input("Enter the text: ")
fhand.write(text)
fhand.read()
fhand.close()