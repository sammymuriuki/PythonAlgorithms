def cyclic_rotation(k, arr):
    n = len(arr)
    if n<1:
        return arr
    for i in range(k):
        temp = arr[n-1]
        for j in range(n-1, 0, -1):
            arr[j]=arr[j-1]
        arr[0]=temp
    return arr

A = [3, 8, 9, 7, 6]
K = 3
print(cyclic_rotation(K, A))