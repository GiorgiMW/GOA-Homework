#Check whether the number entered by the user is exactly divisible by 2 and 4
user_number = int(input("type number here: "))

if user_number % 2 == 0 and user_number % 4 == 0: 
    print("correct")
else:
    print("incorrect")

