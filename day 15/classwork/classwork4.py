#Create a function that takes a list as an argument and prints the sum of the numbers in the list, don't use sum.
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    print("The sum of all list is:", total)

my_list = [1,2,3,4,5,]
calculate_sum(my_list)