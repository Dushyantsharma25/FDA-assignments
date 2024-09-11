import time
r=[]
l=r
n=int(input("enter number of present students "))
print("Enter roll number of students")
for i in range (0,n):
    z=int(input())
    r.append(z)




s=int(input("Enter the roll number of student to be cheacked"))
print("#by linier search")
start =time.time()
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
end = time.time()
print(end -start)
print("No. of steps count = ",(g))
print("#by binary search")
start = time.time()
r.sort()


x=0
left = 0
right = len(r) - 1
result =0
while left <= right:
    x=x+1
    mid = left + (right - left) // 2
    if r[mid] == s:
        result=1
        break
    elif r[mid] < s:
        left = mid + 1
    else:
        right = mid - 1
    result=0


if(result==1):
    print("Student was present")
else:
    print("Student was not present")

end = time.time()
print(end-start)
print("No. of steps count = ", x)


print("#by Sentinal Search")

start = time.time()
r=l
u=0
n = len(r)
r.append(s)
    
i = 0
while r[i] != s:
    u=u+1
    i += 1
r.pop()
    
if i < n:
    result= i
else:
    result = -1

if result != -1:
    print("Target value ",s,"found at index ",i)
else:
    print("Target value ",s," not found")
end = time.time()
print(end-start)
print("No. of step count are",u)

