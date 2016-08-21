import csv
import sys
import numpy as np
data=np.empty((59382,128),dtype=object)
f = open('train.csv', 'rt')
i=0
try:
    reader = csv.reader(f)
    for row in reader:
	for x in range(128):
#       		print row[x]
		data[i,x]=row[x]
	i=i+1
finally:
    f.close()
first=data[1,2]
second=data[1,2]
print("The input taken is",data[:,2])
print("test = ", first[0])
print("test = ", second[1])
print("test = ", first[0])
characters=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z'])

char2int=(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14','15', '16', '17', '18', '19', '20', '21','22', '23', '24', '25', '26'])

print("********  TESTING   **********")
print("first character = ",len(data[:,2]))

for i in range(len(data[:,2])):
	first=data[i,2]
	second=data[i,2]
	for j in range(26):
		if first[0]==characters[j]:
			first=char2int[j]
			cat=first+second[1]
	data[i,2]=cat

print("*********   TESTING   *******")	
print("** Replaced the alphabet with char **")
print("data[1,2] = ",data[1,2])



	
