# Print the number of times a word is repeated in the sentence

s="Hello World, Lets start our Hello World Program"
word="start"
mylist=s.split(" ")
count=0
for i in range(len(mylist)):
    if word==mylist[i]:
        count+=1
print(count)