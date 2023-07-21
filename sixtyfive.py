# Write a Python program to count number of characters, words and lines in a file

fhand=open('sixtyonefile.txt','r')
linecount=0
wordcount=0
charcount=0
for line in fhand:
    linecount+=1
    wordlist=line.split()
    wordcount+=len(wordlist)
    charcount+=len(line)
print("linecount: ",linecount)
print("wordcount: ",wordcount)
print("charcount: ",charcount)