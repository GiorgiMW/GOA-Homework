num = int(input("Enter number here: "))


if num % 2 == 0 and num % 3 != 0:
    print("it can be divided into 2.")
elif num % 3 == 0 and num % 2 != 0:
    print("it can be divided into 3")
elif num % 2 == 0 and num % 3 == 0:
    print("it can be divided into 2 and also into 3")
else:
    print("it can't be divided into 2 and also into3")