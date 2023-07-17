# "Program  to add 'ing' at the end of a given string (length should be at least 3) .If the given string already ends with 'ing' then add 'ly' instead. If the string
#length of the given string is less than 3, leave it unchanged"

def myfunc(s,length):
    if length<3:
        return s
    elif s.endswith('ing'):
        new=s.replace('ing','ly')
        return new
    else:
        new=s+'ing'
        return new

s=input("Enter the string: ")
length=len(s)
print(myfunc(s,length))


    
