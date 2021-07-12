# 11. Write a Python program to create a shallow copy of sets


import copy

A = {1, 2, 3, 4, 5}
print (copy.copy (A))


A = {1, 2, 3, 4, 5}
B = A.copy ()
print (B)
