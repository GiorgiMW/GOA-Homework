def manual_replace(lst, string1, string2):
    
    listn = []
    for i in lst:
        if i != string1:
            listn.append(i)
        else:
            listn.append(string2)
    return listn

list1 = [1, 2, 3, 4, 5, 3, 6, 3, 7]
new_list = manual_replace(list1, 10, 9)
print(new_list) 
