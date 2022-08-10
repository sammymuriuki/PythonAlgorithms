'''
Given a positive integer n, how can we count the number of digits in its decimal
representation? One way to do it is convert the integer into a string and count the characters.
Here, though, we will use only arithmetical operations instead. We can simply keep dividing
the number by ten and count how many steps are needed to obtain 0.
'''
n = +10
result = 0
while n > 0:
   n = n//10
   result += 1
print(result)
