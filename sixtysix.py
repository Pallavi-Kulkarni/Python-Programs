# Print the lines starting with ‘I’

fhand=open('sixtysixfile.txt','r')
for line in fhand:
    if line.startswith('I'):
        print(line)
fhand.close()