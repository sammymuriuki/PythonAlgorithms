
# How to Slice Lists/Arrays and Tuples in Python
a = [1, 2, 3, 4, 5, 6, 7, 8]

#  Now let's say that we really want the sub-elements 2, 3, and 4 returned in a new list. How do we do that?

print(a[1:4])

# Advanced Python Slicing (Lists, Tuples and Arrays) Increments
print(a[1:4:2])  # That last colon tells Python that we'd like to choose our slicing increment. By default, Python sets this increment to 1, but that extra colon at the end of the numbers allows us to specify what we want it to be.
# Python Slicing (Lists, Tuples and Arrays) in Reverse
print(a[::-1])   # It means to increment the index every time by -1, meaning it will traverse the list by going backwards. 
# If you wanted the even indexes going backwards, you could skip every second element and set the iteration to -2. Simple.
print(a[::-2]) 

# Using Python Slice Objects
# sliceObj = slice(1, 3)
print(a[slice(1, 3)])

print(a[:])
print(sum(a))
print(sum(a[0:3]))
b = [1]
print(sum(b[0:2]))
for i in range(2,len(b)):
    print(b[i])