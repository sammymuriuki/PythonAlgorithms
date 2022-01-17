# Find Second largest element in an array
# Given an array of integers, our task is to write a program that efficiently finds the second largest element present in the array. 
def solution(A):
    # elements must be more than 2
    lenA= len(A)
    if(lenA<2):
        return "Invalid input"
    A.sort()
    # Start from second last
    # element as the largest 
    # element is at last
    print(A)
    for i in range(lenA-2, -1, -1):
        if(A[i] != A[lenA-1]):
            return A[i]
    return
# time complexity Time Complexity: O(n log n). 
# Time required to sort the array is O(n log n).
# Auxiliary space: O(1). 
# As no extra space is required.
arr = [-2454635434, 2454635434]
print("solution 1: ",solution(arr))


## MORE EFFICIENT
# import sys
# sys.maxsize. Get the largest integer
#
def solution2(A):
    largest = second = -2454635434
    n = len(A)
    if(n<2):
        return
    # find the laregt number
    for i in range(n):
        largest = max(largest, A[i])
    # find the second largest
    for i in range(n):
        if A[i] != largest:
            second = max(second, A[i])
    if (second == -2454635434):
        return
    else:
        return second

print("solution 2 :",solution2(arr))