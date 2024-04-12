#Manual Max Function: Define a function named manual_max that iterates through list, updating a variable with the maximum value,

def manual_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
#then returns the maximum value found. Use for loop for this task.
my_list = [3, 7, 2, 10, 5]
print("Maximum value in the list:", manual_max(my_list))