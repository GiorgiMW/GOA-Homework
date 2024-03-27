#Create a function to pass to the list. Your task is to print the arithmetic mean (sum / length) of this list.
def arithmetical_operation(lst):
    total_sum = sum(lst)
    answer = total_sum / len(lst)
    print("answer is:", int(answer))

my_list = [1,2,3,4,5]
arithmetical_operation(my_list)