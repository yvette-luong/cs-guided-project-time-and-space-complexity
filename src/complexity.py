# Example of constant time code 
# `array` input could be small, or it could be large 
def returns_in_constant_time():
#     # getting an element from an array via its index 
#     # return array[0]
#     # return array[-1]
#     # return dictionary['key']

#     # constant time loop 
    for i in range(1000000):
        print(i)
# ​
    for i in range(10):
        print(i)
# ​
# ​
# regardless of whether this array holds 10 elements
# or if it holds 1_000_000 elements,
# this function will run in the same amount of time 
# ​
# put another way, the time this function takes to run
# is independent of the size of the input 

def prints_in_constant_time(array):
    print(array[0])  # constant * constant 
    print(array[-1])
    print(array[3])
# ​
'''
Examples of constant time operatations 
​
1. Accessing array elements via their index 
2. Printing 
3. Accessing dictionary values via their keys
4. Adding an element to the back of an array 
   (using the `append` or `push` methods)
5. Initializing variables / empty data structures 
6. Equality checks 
7. Arithmetic operations 
8. Setting a key-value pair in a dictionary
'''

# ​
def runs_in_linear_time_1(n):
    for i in range(n):
        print(i)
# ​
def runs_in_linear_time_2(array):
    # if array has 10 elements, then we know that 
    # there will be 10 loop iterations 
# ​
    # if array has 1_000_000 elements, then we know 
    # that there will be 1_000_000 loop iterations 
    # for item in array:
    #     print(item)
# ​
    # this is still looping over all the array elements
    # and adding them to the copy list 
    copy = [item for item in array] 
# ​
    # copy = [] 
    
    # # linear * constant == linear 
    # for item in array:
    #     copy.append(item)
# ​
    return copy 
# ​
# len(array) == 100   
def runs_in_quadratic_time(array):
    # linear * linear == quadratic 
    # 10 * 10 == 100 
    # 100 * 100 == 10000
    # 1000 * 1000 == 1000000
    # linear loop proportional to the length of `array`
    for i in range(len(array)): # 10 
        # linear loop proportional to the length of `array` 
        for j in range(len(array)): # 10 
            print(i, j)
