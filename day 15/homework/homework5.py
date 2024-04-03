#Create a function to pass to the list. You should have both positive and negative numbers in this list.
def listn(numbers):
    number = 0
    my_list = []
    for i in numbers:
        if i >= 0:
            number = number + i 
        else:
            my_list.append(i)
    print("Length of negative numbers:", len(my_list))
    print("postive numbers sum is:", number)
    
#Your task is to find the sum of the negative numbers and the sum of the positive numbers (use a for loop on both)
my_list1 = [2,3,4,-5,-6,-9]
listn(my_list1)