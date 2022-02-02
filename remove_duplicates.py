# How to Remove Duplicates From a Python List

def remove_duplicates(A):
    return list(dict.fromkeys(A))

''' Explanation

Create a dictionary, using the List items as keys. 
This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
Then, convert the dictionary back into a list: