#Manual Len Function: Develop a function named manual_len that iterates through list, counting each element,
def manual_len(lst):
    length = 0
    
    for _ in lst:
        length += 1
    return length
#and returns the count as the length of the list. Use for loop for this task
my_list = [3, 7, 2, 10, 5]
print("Length of the list:", manual_len(my_list))
