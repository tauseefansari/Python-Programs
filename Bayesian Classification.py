def check(a,b,x,y):
    c=0
    for i in range(0,len(x)):
        if x[i]==a and y[i].replace("\n","")==b:
            c+=1
    return c

with open("Data.txt","r") as f:
    fl=[]
    for line in f:
        line.split("\t")[4].replace("\n","")
        fl.append(line.split("\t"))

    print("Data : ")
    for i in fl:
        for j in i:
            print("\t",j,end="")

    data1=[]
    for i in fl:
        data1.append(i[1])

    data2 = []
    for i in fl:
        data2.append(i[2])

    data3 = []
    for i in fl:
        data3.append(i[3])

    data4 = []
    for i in fl:
        data4.append(i[4])

dy=0
for y in data4:
    if y.replace("\n","")=="YES":
        dy+=1

dn=0
for y in data4:
    if y.replace("\n","")=="NO":
        dn+=1

print("\n\nSTEP 1 : Calculate Probabilities\n")
print(data4[0])
print("P (YES) =",dy,"/",len(data4)-1, "\t\t\t","P (NO) =",dn,"/",len(data4)-1)

print("\n",data1[0],": ")
print("P (YES | YES) =",check("YES","YES",data1,data4),"/",dy, "\t\t\t","P (YES | NO) =",check("YES","NO",data1,data4),"/",dn)
print("P (NO | YES) =",check("NO","YES",data1,data4),"/",dy, "\t\t\t","P (NO | NO) =",check("NO","NO",data1,data4),"/",dn)

print("\n",data2[0],": ")
print("P (EMPLOYEED | YES) =",check("EMPLOYEED","YES",data2,data4),"/",dy, "\t\t\t","P (EMPLOYEED | NO) =",check("YES","NO",data2,data4),"/",dn)
print("P (BUSINESS | YES) =",check("BUSINESS","YES",data2,data4),"/",dy, "\t\t\t","P (BUSINESS | NO) =",check("BUSINESS","NO",data2,data4),"/",dn)
print("P (UNEMPLOYEED | YES) =",check("UNEMPLOYEED","YES",data2,data4),"/",dy, "\t\t\t","P (UNEMPLOYEED | NO) =",check("UNEMPLOYEED","NO",data2,data4),"/",dn)

print("\n",data3[0],": ")
print("P (HIGH | YES) =",check("HIGH","YES",data3,data4),"/",dy, "\t\t\t","P (HIGH | NO) =",check("HIGH","NO",data3,data4),"/",dn)
print("P (AVERAGE | YES) =",check("AVERAGE","YES",data3,data4),"/",dy, "\t\t","P (AVERAGE | NO) =",check("BUSINESS","NO",data3,data4),"/",dn)
print("P (LOW | YES) =",check("LOW","YES",data3,data4),"/",dy, "\t\t\t","P (LOW | NO) =",check("LOW","NO",data3,data4),"/",dn)

print("\n\t\t\t ( Use Uppercase Letters Only )")
homeowner=input("Enter Home Owner (either YES or NO) : ")
status=input("Enter Status (either EMPLOYEED or BUSINESS or UNEMPLOYEED) : ")
income=input("Enter Income (either HIGH or AVERAGE or LOW) : ")

print("\n\nTuple T = {",data1[0],"=",homeowner,",",data2[0],"=",status,",",data3[0],"=",income,"}")

print("\nSTEP 2 : Calculate Prior Probability\n")
print("P ( T |",str(data4[0]).replace("\n",""),"= YES ) = ","(",check(homeowner,"YES",data1,data4),"/",dy,")","x","(",check(status,"YES",data2,data4),"/",dy,")","x","(",check(income,"YES",data3,data4),"/",dy,")")
prior1=((check(homeowner,"YES",data1,data4)/dy)*(check(status,"YES",data2,data4)/dy)*(check(income,"YES",data3,data4)/dy))
print("\t\t\t  =",prior1)

print("\nP ( T |",str(data4[0]).replace("\n",""),"= NO ) = ","(",check(homeowner,"NO",data1,data4),"/",dn,")","x","(",check(status,"NO",data2,data4),"/",dn,")","x","(",check(income,"NO",data3,data4),"/",dn,")")
prior2=((check(homeowner,"NO",data1,data4)/dn)*(check(status,"NO",data2,data4)/dn)*(check(income,"NO",data3,data4)/dn))
print("\t\t\t =",prior2)

print("\nSTEP 3 : Calculate Class Probability\n")
print("P (",str(data4[0]).replace("\n",""),"= YES ) = ",dy,"/",len(data4)-1)
class1=(dy/(len(data4)-1))
print("\t\t      =",class1)
print("P (",str(data4[0]).replace("\n",""),"= NO ) = ",dn,"/",len(data4)-1)
class2=(dn/(len(data4)-1))
print("\t\t      =",class2)

print("\nSTEP 4 : Calculate Total Probability\n")
print("P (T) =  (",(check(homeowner,"YES",data1,data4)+check(homeowner,"NO",data1,data4)),"/",(dy+dn),") x (",(check(status,"YES",data2,data4)+check(status,"NO",data2,data4)),"/",(dy+dn),") x (",(check(income,"YES",data3,data4)+check(income,"NO",data3,data4)),"/",(dy+dn),")")
total=(check(homeowner,"YES",data1,data4)+check(homeowner,"NO",data1,data4))/(dy+dn)*(check(status,"YES",data2,data4)+check(status,"NO",data2,data4))/(dy+dn)*(check(income,"YES",data3,data4)+check(income,"NO",data3,data4))/(dy+dn)
print("      =",total)

print("\nSTEP 5 : Calculate Posteriar Probability\n")
print("P (",str(data4[0]).replace("\n",""),"= YES | T ) = (",prior1,"x",class1,") / (",total,")")
posteriar1=((prior1 * class1)/(total))
print("\t\t\t  =",posteriar1)
print("P (",str(data4[0]).replace("\n",""),"= NO | T ) = (",prior2,"x",class2,") / (",total,")")
posteriar2=((prior2 * class2)/(total))
print("\t\t\t =",posteriar2)

print("\nSTEP 6 : Result\n")
if posteriar1 > posteriar2:
    print("Class : ",data4[0].replace("\n", ""), " = YES \t\t\t Here ",posteriar1,">",posteriar2)
else:
    print("Class : ",data4[0].replace("\n", ""), " = NO \t\t\t Here ",posteriar1,"<",posteriar2)
