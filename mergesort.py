def merge_sort(A):
    if len(A)<=1:
        return A
    middle = len(A)//2
    left_half = A[:middle]
    right_half = A[middle:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return sort_em(left_half, right_half)
    
def sort_em(left_side, right_side):
    res = []
    i=j=0
    while(i<len(left_side) and j<len(right_side)):
        if left_side[i]<right_side[j]:
            res.append(left_side[i])
            i+=1 
        else:
            res.append(right_side[j])
            j+=1
    res+=left_side[i:]
    res+=right_side[j:]
    return res

myA=[345,2,52, 6,33,3,45,7,33,8,99,4 ]
print(merge_sort(myA))