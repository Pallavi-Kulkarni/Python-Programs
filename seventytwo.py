# Python program to demonstrate seek() and tell() methods

fhand=open('seventytwofile.txt','r')
fhand.seek(13)  # seek function helps you to place the cursor for the position you want
print(fhand.tell()) # tell function tells you the position you are in
print(fhand.readline())# readline function prints the word from the cursor located in
fhand.close()