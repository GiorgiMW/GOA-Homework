#Create a function that prints the minimum and maximum numbers from a specific list, do not use min and max. Use def, for, if/else, indexing, print.
def min_or_max(numbers):
    min_value = numbers[0]
    max_value = numbers[0]
    
    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    print(f"The lowest value is {min_value}")
    print(f"The highest value is {max_value}")

my_list = [1,2,3,4,5,]
min_or_max(my_list)