def LS(a):
    for i in range (10):
        if(x==a[i]):
            print("Element Found at index = ")
            return i+1
    print("Element not found at any index")


def BS(b):
    b.sort()
    left=0
    right=len(b)-1
    while(left<=right):
        mid=left+(right-left)//2
        if(b[mid]==x):
            print("Element Found at index = ")
            return mid+1
        elif(b[mid]<x):
            left=mid+1
        else:
            right=mid-1
        

def SS(c):
    c.append(x)
    for i in range (11):
        if(c[i]==x):
            index=i
            break
    if(index<len(c)):
        print("Element Found at index = ")
        return index+1
    else:
        print("Element Not found at any index")

def FS(d):
    n=len(d)
    m2=0
    m1=1
    m=m1+m2
    

    while(m<n):
        m2=m1
        m1=m
        m=m1+m2
    
    offset =-1

    while(m>1):
        i=min(offset+m2,n-1)
        if(d[i]<x):
            m=m1
            m1=m2
            m2=m-m1
            offset=i
        elif(d[i]>x):
            m=m2
            m1=m1-m2
            m2=m-m1
        else:
            return i


            
    

    
a=[]
for i in range (10):
    print("Enter a element")
    x=float(input())
    a.append(x)

print("Enter a elemet to search")
x=float(input())

# By linier search

print(LS(a))

# By Binary search
b=a
print(BS(b))

# By Sentinal search
c=a
print(SS(c))