'''
The Fibonacci numbers4 form a sequence of integers defined recursively in the
following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. The first few elements in this sequence are: 0,
1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, not exceeding
a given integer n.
We can keep generating and printing consecutive Fibonacci numbers until we exceed n.
In each step it’s enough to store only two consecutive Fibonacci numbers.
'''
a=0
b=1
n =100
while a <= n:
    print(a)
    c = a+b
    a = b
    b = c