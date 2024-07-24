a=[]
print("Enter Total number of students in class")
n=int(input())
print("Enter The students Gave Exam")
N=int(input())
for i in range (0,N):
    print("Enter marks of ",i+1," st student")
    s=int(input())
    a.append(s)

x=0
for i in range (0,N):
    x=x+a[i]
print("Average marks of students are = ",x/N)


h=n-N
print("Number of absent Students are = ",h)

import statistics
m= statistics.mode(a)
print("Highest frequent marks are =", m)



p=40
pa=0
fa=0
for i in range (0,N):
    if(a[i]>=p):
        pa=pa+1
    else:
        fa=fa+1

print("Pass percentage of class is = ",(pa/n)*100)
print("Fail percentage of class is = ",(fa/n)*100)