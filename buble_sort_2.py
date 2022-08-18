def buble_sort(A):
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1], A[j]
    return A
print(buble_sort([6,3,7,34,8,9,11,3,45,1,0,2]))
