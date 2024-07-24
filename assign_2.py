print("Enter Total number of Computer group Students")
s=int(input())
print("Enter number of students of Group A")
A=[]
a=int(input())
for i in range (0,a):
    print("Enter")
    h=int(input())
    A.append(h)
print("Enter number of students of Group B")
B=[]
b=int(input())
for i in range (0,b):
    print("Enter")
    h=int(input())
    B.append(h)
print("Enter number of students of Group C")
C=[]
c=int(input())
for i in range (0,c):
    print("Enter")
    h=int(input())
    C.append(h)

set1=set(A)
set2=set(B)
set3=set(C)
print("Student play cricket and badminton = ",set1|set2)

print("students who play either cricket or badminton but not both are = ",(set1|set2)-(set1&set2))




U=set1|set2|set3

print("Students play nither badminton nor cricket are = ",list(U-(set1|set2)))

print("Students who play cricket and football but not badminton are = ",list(U-(set2)))
d=len(list(U))
print("Students don't play any game are = ",s-d)
print("Student play atleast one game are = ",U)
print("Student play all three games are = ",set1&set2&set3)