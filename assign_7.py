def swap(x,y):
    d=y
    x=d
    y=x
def radix_bucket_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        
        for i in range(n):
            arr[i] = output[i]
    
    def get_max(arr):
        max_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
        return max_val
    
    max_val = get_max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def partition(b,l,h):
    pivot=b[l]
    i=l
    j=h

    while(i<j):
        while(b[i]<=pivot and i<=h):
            i+=1
        while(b[j]>pivot):
            j-=1
        if(i<j):
            swap(b[i],b[j])
    swap(b[l],b[j])
    return j
        
def quiksort(b,st,en):
    if(st<en):
        p=partition(b,st,en)
        quiksort(b,st,p-1)
        quiksort(b,p+1,en)

           

n=int(input("Enter number of Student :  "))
input_list = []
for i in range (n):
    x=int(input("Enter percentage of Student = "))
    input_list.append(x)
b=input_list
radix_bucket_sort(input_list)
print("Sorted list:", input_list)

quiksort(b,0,n-1)
print("Sorted list:", b)
print("Top five students percentage", input_list[n-5:n])