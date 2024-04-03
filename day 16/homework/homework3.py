#Create a function that returns the number of elements in the list, input data: [1,2,3,4,5] ---- output data (result): 5
def count_elements(input_list):
    return len(input_list)

my_lst = [1, 2, 3, 4, 5]
answer = count_elements(my_lst)
print(answer)