# Python program to combine each line from first file with the corresponding line in second file.

fhandone=open('seventythreefileone.txt','r')
fhandtwo=open('seventythreefiletwo.txt','r')

for lineone,linetwo in zip(fhandone,fhandtwo):
    print(lineone+linetwo)