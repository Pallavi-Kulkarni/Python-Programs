# Write a python program to read a file and write into another file.

fhand=open('seventyfile.txt','r')
text=open('seventyonefile.txt','w')
for line in fhand:
    text.write(line)
fhand.close()
text.close()