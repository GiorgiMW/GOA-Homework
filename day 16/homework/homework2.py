#Create a function that calculates the sum of odd and even numbers separately, return a list where these sums are inserted,
def even_or_odd(lst):
    number = 0
    number1 = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            number = number + lst[i]
        elif i % 2 != 0:
            number1 = number1 + lst[i]
    return number,number1

#input data [1,2,3,4,5] ---- output data [6, 9]
my_lst = [1,2,3,4,5]
print(even_or_odd(my_lst))