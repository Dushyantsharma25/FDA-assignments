mat1=[]
mat2=[]
r1=int(input("Enter the rows of first matrix = "))
c1=int(input("Enter the colomns of first matrix = "))
r2=int(input("Enter the rows of second matrix = "))
c2=int(input("Enter the colomns of second matrix = "))
z=0
for i in range (r1):
    x=[]
    for j in range (c1):
        a=int(input("ENTER for mat1 = "))
        if(a!=0):
            z+=1
        x.append(a)
    mat1.append(x)

y=0
for i in range (r2):
    x=[]
    for j in range (c2):
        a=int(input("ENTER for mat2 = "))
        if(a!=0):
            y+=1
        x.append(a)
    mat2.append(x)



smat1=[[r1,c1,z]]
smat2=[[r2,c2,y]]

for i in range (r1):
    for j in range (c1):
        if(mat1[i][j]!=0):
            smat1.append([i,j,mat1[i][j]])

for i in range (r2):
    for j in range (c2):
        if(mat2[i][j]!=0):
            smat2.append([i,j,mat2[i][j]])

tmat1=smat1
tmat2=smat2
for i in range (1,len(smat1)):
    tmat1[i][0],tmat1[i][1]=tmat1[i][1],tmat1[i][0]

for i in range (1,len(smat2)):
    tmat2[i][0],tmat2[i][1]=tmat2[i][1],tmat2[i][0]


del tmat1[0]
del tmat2[0]
tmat1=sorted(tmat1,key=lambda x:x[0])
tmat2=sorted(tmat2,key=lambda x:x[0])

tmat1=[[c1,r1,z]]+tmat1
tmat2=[[c2,r2,y]]+tmat2



print("Transpose of mat1 is = ")
print(tmat1)
print("Transpose of mat2 is = ")
print(tmat2)


sum1=smat2

for i in range (1,len(sum1)):
    for j in range (1,len(smat1)):
        if(sum[i][0]==mat1[j][0]&sum[i][1]==mat1[j][1]):
            sum[i][2]=sum[i][2]+mat1[j][2]

sum2=smat1

for i in range (1,len(sum2)):
    for j in range (1,len(smat2)):
        if(sum[i][0]==mat2[j][0]&sum[i][1]==mat2[j][1]):
            sum[i][2]=sum[i][2]+mat2[j][2]
            
set1=sum1
set2=sum2
set3=set1+set2