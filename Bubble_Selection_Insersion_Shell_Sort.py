import time
def bubblesort(l):
    start = time.time()
    d=0
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            d+=1
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print("No of Comparations in bubble sort",d,"\n")
    end = time.time()
    print(end - start)
    return l

def selection_sort(l):
    start = time.time()
    d=0
    n = len(l)
    for i in range(n-1):
        p = i
        for j in range(i+1, n):
            d+=1
            if l[p] > l[j]:
                p = j
        l[i], l[p] = l[p], l[i]
    print("No of Comparations in selection sort",d,"\n")
    end = time.time()

    print(end - start)
    return l

def insertion_sort(arr):
    start = time.time()
    d=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            d+=1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end = time.time()
    print(end - start)
    print("No of Comparations in insertion sort",d,"\n")


def shell_sort(b,k):
    start = time.time()
    d=0
    while(k>=1):
        k=k//2
        for i in range(1, len(b)):
            key = b[i]
            j = i - k
            while j >= 0 and key < b[j]:
                d+=1
                b[j + k] = b[j]
                j -= k
            b[j + k] = key
    end = time.time()
    print(end-start)
    print("No of Comparations in shell_sort",d,"\n")


l = []
n=int(input("Enter the number of Students = "))

for i in range (n):
    print("Enter marks of ",i+1," Student")
    x=float(input())
    l.append(x)
b=l
k=n
sorted_list_bubble = bubblesort(l.copy()) 
print("Bubble Sort result:", sorted_list_bubble)

sorted_list_selection = selection_sort(l.copy())  
print("Selection Sort result:", sorted_list_selection)

a=l
insertion_sort(a)
print("Insersion Sort result:",a)


shell_sort(b,k)
print("Shell_Sort result:",b)


print("Top 5 Students are - ",b[0:5])
