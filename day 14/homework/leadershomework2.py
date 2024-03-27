#This task asks you to calculate the sum of the squares of numbers from 1 to 5 (or any specified range). You'll square each number and then add up all the results.
summation = 0

for i in range(1,6):
    summation = i ** 2 + summation
    print(summation)
print("the sum of the squares of numbers is:", summation)