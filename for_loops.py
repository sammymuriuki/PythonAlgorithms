'''
Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
should consist of n rows, where n is a given positive integer, and consecutive rows should
contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:

* 

* *

* * *

* * * *

'''
n = 4
for i in range(n):
    for j in range(i+1):
        print(" * ", end='')
    print("\n")

