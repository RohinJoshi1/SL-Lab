'''
Python: Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each
element in the original list is multiplied by 3. Use ‘lambda’ and ‘reduce’ function find the
sum of the elements of the original list as well as the new list.
'''

import functools


ls = [1,3,4,5,6,9]
ls2 = [3*i for i in ls]
lssum = functools.reduce(lambda x,y:x+y,ls)
print(lssum)
lssss = lssum = functools.reduce(lambda x,y:x+y,ls2)
print(lssss)