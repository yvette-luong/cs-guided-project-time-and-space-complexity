'''
Space complexity, how much memory does the algorithm use?

Space complexity (includes) the og data

Auxiliary Space Complexity does not include the original data
'''

# def foo(a):
#     b = a.copy() # O(n) aux space complexity 

# 0 1 2 3 4 5  6 7 8 9 10
# 0 1 1 2 3 5 8 13 21 34 55 ... Fibonacci sequence

#  fib(0) : 0
#  fib(1) : 1
#  fib(n) : fib(n-1) + fib(n-2)

cache = {} # Memorization
def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    if  n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

for i in range(1000):
    print(f"{1:3} {fib(i)}")