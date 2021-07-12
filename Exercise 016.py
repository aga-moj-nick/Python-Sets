# 16. Write a Python program to check if a given value is present in a set or not.


A = {1, 2, 3, 4, 5}
n = int (input ("Podaj cyferkę, którą chcesz odkryć: "))


if n in A:
    print ("Wybrana cyferka jest na liście")
else:
    print ("Wybranej cyferki nie ma na liście")
