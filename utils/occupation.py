import csv
import random

 #rid of header text


#reads file
def read(data):
    f = open(data, 'r')
    reader = csv.reader(f)
    return reader



#seperates into 2 lists
def dictCreate(reader):
    firstline= False
    jobs=[]
    chance=[]
    for row in reader:
        if firstline:
            jobs.append(row[0])
            chance.append(float(row[1]))
        else:
            firstline=True



    #rid of the total
    jobs=jobs[:-1]
    chance=chance[:-1]

    #creates the dict by combining list
    d = {}
    i=0
    while i < len(jobs):
        d[jobs[i]]=chance[i]
        i+=1
    return d



def jobGen(d):
    percent = random.uniform(0, 99.8)
    total=99.8
    for key in d:
        if (d[key] >= (total-percent)):
            return key
            break
        else:
            total-=d[key]
