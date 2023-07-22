# Write a python program to find the longest words

s="Surprised Discrimination anger"
list=s.split(" ")
mylist=[]
prev=0
for i in list:
    next=len(i)
    if(prev<next):
        mylist.append(i)
    prev=len(i)
print(mylist[-1])




    
   
    
        

  
    


