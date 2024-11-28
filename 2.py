def BS(p):
    for i in range (len(p)):
        d=0
        for j in range(len(p)-i-1):
            if(p[j]>p[j+1]):
                p[j],p[j+1]=p[j+1],p[j]
                d=1
        if(d==0):
            break
    print("Bubble Sort Result is = ")
    return p

def SS(q):
    for i in (0,len(q)-1):
        p=i
        v=q[i]
        for j in range (i+1,len(q)):
            if(v>q[j]):
                v=q[j]
                p=j
        q[p],q[i]=q[i],q[p]
    
    print("Selection Sort result is = ")
    return q


def IS(r):
    for i in range (1,len(r)):
        key = r[i]
        j=i-1
        while(j>=0 and key < r[j]):
            r[j+1]=r[j]
            j-=1
        r[j+1]=key
    
    print("Insersion Sort Result is = ")
    return r

def SHS(x):
    k=len(a)
    while(k>=1):
        k=k//2
        for i in range (k,len(r)):
            key = r[i]
            j=i-k
            while(j>=0 and key < r[j]):
                r[j+k]=r[j]
                j-=k
            r[j+k]=key
    
    print("Shell Sort Result is = ")
    return x


a=[]
for i in range(10):
    print("Enter a Element")
    x=int(input())
    a.append(x)

# by Bubble Sort
p=a
print(BS(p))

# by Selection Sort
q=a
print(SS(q))

# by Insertion Sort
r=a
print(IS(r))

# by shell sort
x=a
print(SHS(x))

# by radix sort