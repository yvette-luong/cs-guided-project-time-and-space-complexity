'''
Space complexity, how much memory does the algorithm use?

Space complexity (includes) the original data

Auxiliary Space Complexity does not include the original data
'''

def foo(a):
    b = a.copy() # O(n) aux space complexity 
    return b
print(foo([1,2,3,4]))
print(foo([1,2,3,4,5,6,7,8]))

def bar(a):
    x = a[0]
    return x * 2 # O(1) aux space complexity over the length of a

print(bar([8,2,3,4]))
print(bar([9,2,3,4,5,6,7,8]))


'''    
-- Fibonacci sequence -- where every number is the sum of the previous 2 numbers

# 0 1 2 3 4 5 6 7 8 9 10  . (index numbers)
# 0 1 1 2 3 5 8 13 21 34 55 ... Fibonacci sequence

#  fib(0) : 0
#  fib(1) : 1
#  fib(n) : fib(n-1) + fib(n-2)
'''
cache = {} # Memorization
def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    if  n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

for i in range(1000):
    print(f"{1:3} {fib(i)}")