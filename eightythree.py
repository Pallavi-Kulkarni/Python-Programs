# Define a Python function ascending(ls) that returns True if each element in its input list is at least as big as the one before it.
# For empty list, it should be True. 
#Here are someexamples to show how your function should work.
#>>> ascending([]) #returns True
#>>> ascending([3,3,4]) #returns True
#>>> ascending([7,18,17,19]) #returns False

def ascending(ls):
    mylist=[]
    if len(ls)==0:
        return True      
    mylist.append(ls[0])
    
    count=0
    for i in range(1,len(ls)):
        if ls[i]>=mylist[i-1] or mylist==0:
            mylist.append(ls[i])
            count+=1              
        else:
            mylist.append(ls[i])
            count-=1
    if count==(len(ls)-1):
        return True
    else:
        return False

list=[]
print(ascending(list))