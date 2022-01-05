def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr
    
myarr=[34,13,45,23,1,4,56,3,5,78,5,42,4]
print(insertion_sort(myarr))