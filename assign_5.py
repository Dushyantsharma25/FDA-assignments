r=[]
n=int(input("enter number of present students "))
print("Enter roll number of students")
for i in range (0,n):
    z=int(input())
    r.append(z)


# by linier search


s=int(input("Enter the roll number of student to be cheacked"))
print("#by linier search")
f=0
g=0
for i in range (0,n):
    g=g+1
    if(s==r[i]):
        f=1
        print("Student was present")
        break
if(f==0):
    print("Student was not present")

print("No. of steps count = ",(g))
print("#by binary search")

r.sort()
x=0

def bs(r,s):
    left = 0
    right = len(r) - 1
    
    while left <= right:
        x=x+1
        mid = left + (right - left) // 2
        if r[mid] == s:
            return (1)
        elif r[mid] < s:
            left = mid + 1
        else:
            right = mid - 1
    return 0


result=bs(r,s)
if(result==1):
    print("Student was present")
else:
    print("Student was not present")


print("No. of steps count = ",x)