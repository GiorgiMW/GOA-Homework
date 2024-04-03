#Make 10 examples of comparison operators that are (> < >= <= == !=)
num1 = int(input("Type first number here: "))
operator = input("enter the operator: ")
num2 = int(input("Type second number here: "))


if operator == ">":
    print(num1 > num2)
elif operator == "<":
    print(num1 < num2)
elif operator == ">=":
    print(num1 >= num2)
elif operator == "<=":
    print(num1 <= num2)
elif operator == "==":
    print(num1 == num2)
elif operator == "!=":
    print(num1 != num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
else:
    print("wrong operator")
