print("Enter rows of first matrix")
r1=int(input())
print("Enter colomns of first matrix")
c1=int(input())
print("Enter rows of second matrix")
r2=int(input())
print("Enter colomns of second matrix")
c2=int(input())

mat1=[]
mat2=[]


for i in range(0,r1):
    x=[]
    for j in range(0,c1):
        y=int(input("Enter the Elemenet = "))
        x.append(y)
    mat1.append(x)

for i in range(0,r2):
    z=[]
    for j in range(0,c2):
        y=int(input("Enter the Elemenet = "))
        z.append(y)
    mat2.append(z)
    
g=1
if(r1==c1):
    for i in range(0,r1):
        for j in range(0,c1):
            if(i>j):
                if(mat1[i][j]!=0):
                    g=0
                    break
        if(g==0):
            break
    if(g==1):
        print("Mat1 is Upper Triangular matrix")
else:
    print("Mat1 is not Upper triangular matrix")

if(r1==c1):
    sum=0

    for i in range(0,r1):
        for j in range(0,c1):
            if(i==j):
                sum=sum+mat1[i][j]
        
    print("Left Diagnol sum of Mat1 is = ",sum)


    sum=0

    for i in range(0,r1):
        for j in range(0,c1):
            if(i+j==r1-1):
                sum=sum+mat1[i][j]
        
    print("Right Diagnol sum of Mat1 is = ",sum)
else:
    print("Diagnol sum not possible of mat1")

if(r2==c2):
    sum=0

    for i in range(0,r2):
        for j in range(0,c2):
            if(i==j):
                sum=sum+mat2[i][j]
        
    print("Left Diagnol sum of Mat2 is = ",sum)


    sum=0

    for i in range(0,r2):
        for j in range(0,c2):
            if(i+j==r2-1):
                sum=sum+mat2[i][j]
        
    print("Right Diagnol sum of Mat2 is = ",sum)
else:
    print("Diagnol sum is not possible of mat2")


rows1 = len(mat1)
cols1 = len(mat1[0])
rows2 = len(mat2)
cols2= len(mat2[0])

tmat1=[[0 for _ in range(rows1)] for _ in range(cols1)]
tmat2=[[0 for _ in range(rows2)] for _ in range(cols2)]

for i in range(0,rows1):
    for j in range(0,cols1):
        tmat1[j][i]=mat1[i][j]

print("Transpose of mat1 is = ",tmat1)

for i in range(0,rows2):
    for j in range(0,cols2):
        tmat2[j][i]=mat2[i][j]

print("Transpose of mat2 is = ",tmat2)
sum=mat1

if(r1==r2&c1==c2):
    for i in range(0,r1):
        for j in range(0,c1):
            sum[i][j]=mat1[i][j]+mat2[i][j]
    print("Sum of matrix is = ",sum)
else:
    print("Sum not possible")

if(r1==r2&c1==c2):
    for i in range(0,r1):
        for j in range(0,c1):
            sum[i][j]=mat1[i][j]-mat2[i][j]
    print("Subtract of matrix is = ",sum)
else:
    print("Subtract not possible")

C = [[0] * len(mat2) for _ in range(len(mat1))]
if(c1==r2):
    for i in range(0,r1):
        for j in range(0,len(mat1[0])):
            product = 0
            for k in range(0,len(mat2[0])):
                product += mat1[i][k] * mat2[k][j]
            C[i][j] = product
    print("Multiplication of matrix is = ",C)
else:
    print("Multiplication is not possible")






def find_sp(matrix):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    
    for i in range(m):
        mr = min(matrix[i])
        mi = matrix[i].index(mr)
        
        isp = all(matrix[j][mi] <= mr for j in range(m) if j != i)
        
        if isp:
            return (i, mi)
    
    return None

print("Saddle point of Matrix 1 is",find_sp(mat1))
print("Saddle poiint of Matrix 2 is",find_sp(mat2))