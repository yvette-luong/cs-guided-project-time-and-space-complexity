'''
Time and Space Complexity 
'''
def foo(n):
    for i in range(n):
        print(i)

foo(10) # 10 prints, if this takes a certain amount of time
foo(20) # 20 prints, how much more time does this take?
foo(10000) # 10000 prints

'''
foo(n) n prints
->  O(n) Order n : Linear
'''


def bar(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

bar(10) # 100 prints
bar(20) # 400 prints
bar(10000)  # 100,000,000 prints

'''
bar(n) -> n^2 prints 
->  O(n^2)
'''

'''
What is Big O: It's a way to measure how well an algorithm scales. 
'''


def foo(a):
    for elem in a:  # O(n) over length of a, n refers to the length of a
        print(elem)

foo([1,2,3,4])
foo([1,2,3,4,5,6,7,8])

def bar(a):
    print(a[0])     # O(1) over the length of a, "Constant Time"

bar([1,2,3,4])
bar([1,2,3,4,5,6,7,8])

def baz(a):
    for i in range(100000000): # O(1) over the length of 'a'
        print(a[0])

bar([1,2,3,4])
bar([1,2,3,4,5,6,7,8])
bar([1,2,3,4,5,6,7,8,9,10,11,12])

def qux(n):
    for i in range(n // 2):     #   O(n/2) == O(1/2 * n) == O(n)
        print(i) 


"""
Login
"""
def search(name, lst):
    for elem in lst: # O(n) over the length of lst
        if name == elem: # O(m) over the length of the compared strings 
            return True
    
    return False

'''
O(n) over the length of the lst
O(n*m) where n is the length of the list, and m is the length of the strings in the list
'''

# def foo(n):
#     for i in range(math.sqrt(n)):
#         print(i)

"""

Binary Search 
-------------

When you cut the space in half, hints that it's O(log(n))
 
10000
5000
2500
1250
6250
3125
1563
782
391
195
97
48
24
12
6
3
1

100 names, 16 comparisons

"""