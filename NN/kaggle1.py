import csv

file=open("train.csv", "r")
reader = csv.reader(file)
for line in reader:
#    t=line[1],line[2]
    print(line[1,1])
