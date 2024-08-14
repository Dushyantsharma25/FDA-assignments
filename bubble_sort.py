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

l = []
print("Original list:", l)
n=int(input("Enter the number of elemets = "))

for i in range (n):
    x=int(input("Enter = "))
    l.append(x)

sorted_list_bubble = bubblesort(l.copy()) 
print("Bubble Sort result:", sorted_list_bubble)

sorted_list_selection = selection_sort(l.copy())  
print("Selection Sort result:", sorted_list_selection)
