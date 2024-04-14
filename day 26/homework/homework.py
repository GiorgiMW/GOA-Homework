#Manual Sum Function: Create a function called 
def sum_list(lst):
    result = 0
    for i in lst:
        result = result + i
    return result
#manual_sum that iterates over list and adds their sum in a variable, then returns variable. Use for loop for this task.
my_list = [1,2,3,4,5]
print(sum_list(my_list))