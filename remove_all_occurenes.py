'''
The task is to perform the operation of removing all the occurrences of a given item/element present in a list.

Examples :

input :
1 1 2 3 4 5 1 2
1
Output :
2 3 4 5 2

Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
After removing the item, the output list is [2, 3, 4, 5, 2]

''''

def remove_all(arr, el):
    res = [i for i in arr if i != el]
    return res
test_list = [1, 3, 4, 6, 5, 1]
item =1
print(remove_all(test_list, item))