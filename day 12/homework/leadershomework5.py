user_number = int(input("Enter your number here: "))

if user_number < 1 or user_number > 9:
    print("wrong number, you must choose from 1 to 9")

for i in range(1,51):
    if i % user_number == 0:
        print(i)