#Enter a negative number for the user.
negative_number = int(input("Enter a negative number: "))
list = []

#Add all negative numbers from this number to 0 to the list
while negative_number < 0:
    list.append(negative_number)
    negative_number = negative_number + 1

#Finally print the list.
print("List of negative numbers from", negative_number, "to 0:", list)