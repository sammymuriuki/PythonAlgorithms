def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[min_index] > A[j]:
               min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

A = [34,2,35,5,6,765,3,35,6,78,765,89,8,76,543,4]

print(selection_sort(A))