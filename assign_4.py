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


tmat1=[[0]*3]*z
tmat2=[[0]*3]*y

a1=[0]*(c1)
for i in range (1,z+1):
    a1[smat1[i][1]]+=1

a2=[0]*(c2)
for i in range (1,y+1):
    a2[smat2[i][1]]+=1

x=a1[0]
a1[0]=1
for i in range (1,c1):
    a1[i]=x+a1[i-1]

x=a2[0]
a2[0]=1
for i in range (1,c2):
    a2[i]=x+a2[i-1]

print(a1)
print(a2)