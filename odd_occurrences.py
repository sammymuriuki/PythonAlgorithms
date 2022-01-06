def getOddOccurrence(arr):
    
    for i in range(0,len(arr)):
        count = 0
        for j in range(0, len(arr)):
            if arr[i] == arr[j]:
                count+=1
            
        if (count % 2 != 0):
            return arr[i]
        
    return 
arr = []
print(getOddOccurrence(arr))