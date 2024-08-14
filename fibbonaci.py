def fun(lst, target):
    n = len(lst)
    if n == 0:
        return -1

    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
    
    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    offset = -1
    
    while (fib > 1):
        i = min(offset + fib2, n - 1)
        
        if (lst[i] < target):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif (lst[i] > target):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    
    if (fib1 and offset + 1 < n and lst[offset + 1] == target):
        return offset + 1
    
    return -1

n = int(input("Enter size of list: "))
target = int(input("Enter element to find: "))
lst = []
print("Enter elements: ")
for i in range(n):
    lst.append(int(input()))

lst.sort()
index = fun(lst, target)
if index != -1:
    print("Element found at index =", index+1)
else:
    print("Element not found")
