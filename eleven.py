# Write a program to count the frequency of characters in a string

s="Pallavi"
mydict={}

for i in s:
    if i in mydict:
        mydict[i]+=1
    else:
        mydict[i]=1

for key, value in mydict.items():
    print(key,value)



    










# s='Pallavi'
# print([*s])
# #output: ['P', 'a', 'l', 'l', 'a', 'v', 'i']

# s='Pallavi'
# mylist=[]
# for i in s:
#     mylist.append(i)
# #output: ['P', 'a', 'l', 'l', 'a', 'v', 'i']

# s="Pallavi"
# print([*s])
#same output

# s="Pallavi"
# mylist=[]
# for i in s:
#     mylist.append(i)
# print(mylist)
#same output