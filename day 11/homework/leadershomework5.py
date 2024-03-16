#Check for even or odd: Write a program that prompts the user for a number and prints whether it is even or odd.
user_number = int(input("Enter number here: "))

if user_number % 2 == 0:
    print(user_number, "is even.")
else:
    print(user_number, "is odd.")
