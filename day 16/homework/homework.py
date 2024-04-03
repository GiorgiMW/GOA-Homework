#Create a function that will return the sum of the numbers in the list at even indices,
def even_nums(lst):
    total = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            total = total + lst[i]
    return total

#input data: [1,2,3,4,5] ---- output data (result): 9
my_lst = [1,2,3,4,5]
print(even_nums(my_lst))