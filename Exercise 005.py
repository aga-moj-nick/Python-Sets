# 5. Write a Python program to remove an item from a set if it is present in the set. 


set = {1, 2, 3, 4, 5}

def usuwanie (set):
    n = int (input ("Podaj element do usunięcia: "))
    if n in set:
        set.discard (n)
        return set
    else:
        print ("Nie ma takiej cyferki")
print (usuwanie (set))
