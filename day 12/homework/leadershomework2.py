#Write an algorithm that offers the user two operations: kilometer - mile, mile - kilometer. The user must select one of them, and then ask for the numerical value to work on,
print("Choose an operation:")
print("1. Kilometer to Mile")
print("2. Mile to Kilometer")

user_choice = input("Enter your choice (1 or 2): ")

if user_choice == "1":
    km = float(input("Type how many Kilometers you want to convert into Miles: "))
    mile = km * 1.6
    print(f"the answer is {mile}")
elif user_choice == "2":
    mile = float(input("Type how many Miles you want to convert into Kilometers: "))
    km = mile / 0.6
    print(f"The answer is {km}")

#and finally print the already converted value. If the user does not choose the correct operation, print "Wrong decision"
else:
    print("Wrong operation")