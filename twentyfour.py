# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

def theyear(name,age):
    current_year=2023
    year=(2023-age)+100
    return year


name=input("Enter the name: ")
age=int(input("Enter the age: "))
print("The year you will be turning 100yrs old is: ",theyear(name,age))