'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def firstMissingPositive(arr, n):
 
    # Loop to traverse the whole array
    for i in range(n):
       
        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n
               and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
     
    # Checking any element which
    # is not equal to i+1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1
         
    # Nothing is present return last index
    return n + 1