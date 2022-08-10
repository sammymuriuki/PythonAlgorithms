'''
For this question, you will write a program that, given a positive integer M and a list of 
integers L, outputs the list element M links away from the end of the list. 
For this program, we will use 1-indexing. That means mth_to_last(1) is the "1st-to-last"
 element, or simply the last element in the list.
'''
def solution(M, L):
    lenL = len(L)
    if(M>lenL):
        print('NIL')
    else:
        o = L[-M]
        if o:
            print(o)
        else:
            print('NIL')

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = 2
solution(M, L)
