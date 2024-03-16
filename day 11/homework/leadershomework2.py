#Sum of Numbers: Write a program that prompts the user for numbers continuously until they enter 0
summation = 0

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        break  
    else:
        summation = summation + num  

#Then print the sum of all the entered numbers.
print("The sum of all entered numbers is:", summation)
