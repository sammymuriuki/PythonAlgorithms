def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
    
ar=[23,45,6,3,567,2,56,7,33,3,77,9,44,5]
print(bubble_sort(ar))