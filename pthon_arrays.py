'''
Problem: Given array A consisting of N integers, return the reversed array.
Solution: We can iterate over the first half of the array and exchange the elements with
those in the second part of the array.
'''

def reverse_array(A):
    n = len(A)
    for i in range(n//2):
        k = n-i-1
        A[i],A[k] = A[k],A[i]
    return A

arr=[12,234,2,13,456,6]
print(reverse_array(arr))
arr.reverse()
print(arr)