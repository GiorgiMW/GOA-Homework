#Manual Min Function: Define a function named manual_min that iterates through list, updating a variable with the minimum value,.
def manual_min(lst):
    min_value = lst[0]
    for num in lst[1:]:
        if num < min_value:
            min_value = num
    
    return min_value
#then returns the minimum value found. Use for loop for this task
my_list = [3, 7, 2, 10, 5]
print("Minimum value in the list:", manual_min(my_list))
