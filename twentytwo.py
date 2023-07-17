# Program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged

def myfunc(s):
    if s.startswith('Is'):
        return s
    else:
        new='Is'+s
        return new

s=input("Enter the string: ")
print(myfunc(s))