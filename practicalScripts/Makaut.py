import os
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\ratul\\Documents')

workbook=openpyxl.load_workbook('exp.xlsx')
sheet=workbook.get_sheet_by_name('Book1')

names=[]
chars=['A','B','C','D','E','F','G']
chars2=['H','I','J','K']
subs=['Principles of management','Database management system','Computer Networking','Software engg','Computer Graphics','Discrete&Compiler Design']
labs=['DBMS','CN','SE','Seminar']
subject1=[]
subject2=[]
subject3=[]
subject4=[]
subject5=[]
subject6=[]
dbms=[]
cn=[]
se=[]
seminar=[]

for i in range(2,20):
    names.append(sheet[chars[0]+str(i)].value)
    subject1.append(sheet[chars[1]+str(i)].value)
    subject2.append(sheet[chars[2]+str(i)].value)
    subject3.append(sheet[chars[3]+str(i)].value)
    subject4.append(sheet[chars[4]+str(i)].value)
    subject5.append(sheet[chars[5]+str(i)].value)
    subject6.append(sheet[chars[6]+str(i)].value)
for i in range(2,20):
    dbms.append(sheet[chars2[0]+str(i)].value)
    cn.append(sheet[chars2[1]+str(i)].value)
    se.append(sheet[chars2[2]+str(i)].value)
    seminar.append(sheet[chars2[3]+str(i)].value)
sub_mean=[np.array(subject1),np.array(subject2),np.array(subject3),np.array(subject4),np.array(subject5),np.array(subject6),np.array(dbms),np.array(cn),np.array(se),np.array(seminar)]
print("Subjects\n")
print(seminar)
for i in range(0,6):
    plt.hist(sub_mean[i])
    plt.xlabel(subs[i])
    plt.savefig("C:\\Users\\ratul\\Desktop\\img{number}.png".format(number=str(i)))
    plt.show()
print("LAB\n")
k=0
for i in range(6,10):
    plt.hist(sub_mean[i])
    plt.xlabel(labs[k])
    plt.grid(True)
    plt.savefig("C:\\Users\\ratul\\Desktop\\img{number}.png".format(number=str(i)))
    plt.show()
    k+=1
