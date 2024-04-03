#Comparing Numbers: Write a program that asks the user for two numbers and compares them.
num1 = int(input("Enter first number here: "))
operator = input("type which operation you want: ")
num2 = int(input("Enter first number here: "))

if operator == ">":
    print(num1 > num2)
elif operator == "<":
    print(num1 < num2)
elif operator == "=":
    print(num1 == num2)


