# 10. Write a Python program to check if a set is a subset of another set.


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {2, 3}

print (A.issubset (B))
print (A.issubset (C))

print (B.issubset (A))
print (B.issubset (C))

print (C.issubset (A))
print (C.issubset (B))
