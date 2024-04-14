#Save your first and last name in the list. Using the capitalize method,
listn = ["giorgi", "motsonelidze"]
listn2 = []
def cap(lst):
    for i in listn:
        listn2.append(i.capitalize())
    return listn2

#work on all elements of the array and finally print the already changed list.
print(cap(listn))
