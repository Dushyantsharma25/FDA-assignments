def bubblesort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        p = i
        for j in range(i+1, n):
            if l[p] > l[j]:
                p = j
        l[i], l[p] = l[p], l[i]
    return l

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def shell_sort(arr,k):
    while(k>=1):
        k=k//2
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - k
            while j >= 0 and key < arr[j]:
                arr[j + k] = arr[j]
                j -= k
            arr[j + k] = key


l = []
n=int(input("Enter the number of Students = "))

for i in range (n):
    print("Enter marks of ",i+1," Student")
    x=float(input())
    l.append(x)

sorted_list_bubble = bubblesort(l.copy()) 
print("Bubble Sort result:", sorted_list_bubble)

sorted_list_selection = selection_sort(l.copy())  
print("Selection Sort result:", sorted_list_selection)

a=l
insertion_sort(a)
print("Insersion Sort result:",a)

b=l
k=n
shell_sort(b,k)
print("Shell_Sort result:",b)


print("Top 5 Students are - ",b[0:5])
